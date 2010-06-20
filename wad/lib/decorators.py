from decorator import decorator
from pylons import session, request
from pylons.controllers.util import abort, redirect_to
from wad import model
from wad.model import meta
import routes

@decorator
def check_invitation(func, self, *args, **kwargs):
    try:
        self.invitation_id = session['invitation_id']
    except KeyError:
        session['redir'] = routes.url_for(request.url)
        session.save()
        redirect_to(controller = 'invitations', action = 'confirmation_form')
    return func(self, *args, **kwargs)

@decorator
def check_gift_count(func, self, *args, **kwargs):
    if meta.Session.query(model.Gift).filter(
        model.Gift.invitation_id == self.invitation_id
    ).count() >= meta.Session.query(model.Guest).filter(
        model.Guest.invitation_id == self.invitation_id
    ).count():
        redirect_to(controller = 'gifts', action = 'too_much')
        return
    else: 
        return func(self, *args, **kwargs)
