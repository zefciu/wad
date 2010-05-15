# vim: set fileencoding=utf-8
import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to
from pylons.decorators import validate

from wad.lib.base import BaseController, render
from wad import model
from  wad.model import meta
import random as rnd

from authkit.authorize.pylons_adaptors import authorize
from authkit.permissions import ValidAuthKitUser
import formencode as fe
from sqlalchemy import orm


log = logging.getLogger(__name__)

class CodeValidator(fe.validators.FancyValidator):
    def _to_python(self, value, state): 
        if len(value) != 8:
            raise fe.Invalid(
                u'Twój kod powinien mieć 8 znaków. Znajdziesz go na zaproszeniu',
                value, state
            )
        try:
            return meta.Session.query(model.Invitation).filter(
                model.Invitation.code == value
            ).one()
        except orm.exc.NoResultFound:
            raise fe.Invalid(
                u'Niestety nie ma takiego zaproszenia. Sprawdź kod ponownie',
                value, state
            )

class CodeSchema(fe.Schema):
    code = CodeValidator()

class InvitationsController(BaseController):

    CHARS = '23456789abcdefhkmnprstxyz'

    @authorize(ValidAuthKitUser())
    def generate_codes(self): 
        empty_inv = meta.Session.query(model.Invitation).filter(
            model.Invitation.code == ''
        ).all()
        for inv in empty_inv:
            inv.code = ''.join((rnd.choice(self.CHARS) for i in range(8)))
        meta.Session.commit()
        return 'ok'

    def confirmation_form(self):
        return render('/invitations/confirmation_form.html')

    @validate(schema = CodeSchema(), form='confirmation_form')
    def submit_code(self):
        session['invitation_id'] = self.form_result['code'].id
        session.save()
        redirect_to(controller = 'guests', action = 'confirmation_list')
