import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from wad.lib.base import BaseController, render
from wad import model
from wad.model import meta

log = logging.getLogger(__name__)

class QnasController(BaseController):

    def index(self):
        c.sections = meta.Session.query(model.Section).join(model.QNA).order_by(
            model.Section.order
        ).all()
        return render('qnas/index.html')
