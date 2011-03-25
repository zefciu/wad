import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import validate

import formencode as fe

from wad.lib.base import BaseController, render
from wad import model
from wad.model import meta

log = logging.getLogger(__name__)

class ConfSchema(fe.Schema):
    guest = fe.foreach.ForEach(fe.validators.Int(), convert_to_list = True)

class GuestsController(BaseController):

    def confirmation_list(self):
        try:
            c.guests = meta.Session.query(model.Guest).filter(
                model.Guest.invitation_id == session['invitation_id']
            ).all()
        except KeyError:
            redirect(url(controller = 'invitations', action = 'confirmation_form'))
        return render('guests/confirmation_list.html')

    @validate(schema = ConfSchema(), form = 'confirmation_list')
    def submit_confirmations(self):
        try:
            meta.connection.execute(model.guests_table.update(
                (model.guests_table.c.id.in_(self.form_result['guest'])) &\
                (model.guests_table.c.invitation_id == session['invitation_id']),
                values = {model.guests_table.c.confirmed: True}
            ))
        except KeyError:
            redirect(url(controller = 'invitations', action = 'confirmation_form'))
            
        return render('guests/submit_confirmations.html')
