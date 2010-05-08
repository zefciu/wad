import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from wad.lib.base import BaseController

log = logging.getLogger(__name__)

class GuestsController(BaseController):
