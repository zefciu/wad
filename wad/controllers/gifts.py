import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to
import routes
from sqlalchemy import orm

from wad.lib.base import BaseController, render
from wad.lib.decorators import check_invitation, check_gift_count
from wad import model
from wad.model import meta

log = logging.getLogger(__name__)

class GiftsController(BaseController):

    @check_invitation
    @check_gift_count
    def list(self):
        c.gifts = meta.Session.query(model.Gift).filter(
            model.Gift.invitation_id == None
        ).order_by(model.Gift.name).all()
        return render('/gifts/list.html')

    @check_invitation
    @check_gift_count
    def view(self, slug):
        try:
            c.gift = meta.Session.query(model.Gift).filter(
                model.Gift.slug == slug
            ).one()
        except orm.exc.NoResultFound:
            abort(404)
        return render('/gifts/view.html')

    @check_invitation
    @check_gift_count
    def confirm(self, slug):
        try:
            gift = meta.Session.query(model.Gift).filter(
                model.Gift.slug == slug
            ).one()
        except orm.exc.NoResultFound:
            abort(404)
        gift.invitation_id = self.invitation_id
        meta.Session.commit()
        c.gift = gift
        
        return render('/gifts/confirm.html')

    def too_much(self):
        return render('/gifts/too_much.html')
