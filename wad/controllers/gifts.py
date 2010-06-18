import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to
import routes

from wad.lib.base import BaseController, render
from wad import model
from wad.model import meta

log = logging.getLogger(__name__)

class GiftsController(BaseController):

    def list(self):
        try:
            invitation_id = session['invitation_id']
        except KeyError:
            session['redir'] = routes.url_for(controller = 'gifts', action = 'list')
            session.save()
            redirect_to(controller = 'invitations', action = 'confirmation_form')

        c.gifts = meta.Session.query(model.Gift).filter(
            model.Gift.invitation_id == None
        )
        return render('/gifts/list.html')

