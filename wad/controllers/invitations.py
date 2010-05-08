import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from wad.lib.base import BaseController
from wad import model
from  wad.model import meta
import random as rnd

from authkit.authorize.pylons_adaptors import authorize
from authkit.permissions import ValidAuthKitUser


log = logging.getLogger(__name__)

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
        return self.render('/base.html')
