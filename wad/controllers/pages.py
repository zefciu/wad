import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from wad.lib.base import BaseController, render
from wad import model
from wad.model import meta
from sqlalchemy import orm

log = logging.getLogger(__name__)

class PagesController(BaseController):

    def view(slug):
        try:
            page = meta.Session.query(model.Page).filter(
                model.page.Slug == slug 
            ).one()
        except orm.exc.NoResultFound:

