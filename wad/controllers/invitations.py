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


log = logging.getLogger(__name__)

class CodeSchema(fe.Schema):
    code = fe.validators.String(
        min = 8, max = 8, notEmpty = True
    )


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
       invitation = meta.Session.query(model.Invitation).filter(
           model.Invitation.code == self.form_result['code']
       ).all();
       if not len(invitation):
           return 'Nie ma takiego zaproszenia'
       else:
           return 'Zaproszenie znalezione'

