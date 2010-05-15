import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from wad.lib.base import BaseController, render
from wad import model
from wad.model import meta

log = logging.getLogger(__name__)

class GuestsController(BaseController):

    def confirmation_list(self):
        c.guests = meta.Session.query(model.Guest).filter(
            model.Guest.invitation_id == session['invitation_id']
        ).all()
        return render('guests/confirmation_list.html')
