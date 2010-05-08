"""The application's model objects"""
import sqlalchemy as sa
from sqlalchemy import orm

from wad.model import meta

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    meta.Session.configure(bind=engine)
    meta.engine = engine


guests_table = sa.Table(
    'guests', meta.metadata,
    sa.Column(
        'id', sa.types.Integer, sa.Sequence('guests_id_seq'), 
        primary_key = True
    ),
    sa.Column('name', sa.types.String(32)),
    sa.Column('surname', sa.types.String(32)),
    sa.Column('name_acc', sa.types.String(32)),
    sa.Column('surname_acc', sa.types.String(32)),
    sa.Column('confirmed', sa.types.Boolean(32)),
    sa.Column('companion_id', sa.types.Integer(), sa.ForeignKey('guests.id')),
    sa.Column('invitation_id', sa.types.Integer(), sa.ForeignKey('invitations.id'))
)

class Guest(object):
    pass

orm.mapper(Guest, guests_table)

invitations_table = sa.Table(
    'invitations', meta.metadata,
    sa.Column(
        'id', sa.types.Integer, sa.Sequence('invitations_id_seq'), 
        primary_key = True
    ),
    sa.Column('parties', sa.types.Integer()),
    sa.Column('code', sa.types.String(8)),
)

class Invitation(object):
    pass

orm.mapper(Invitation, invitations_table)
