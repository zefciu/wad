"""The application's model objects"""
import sqlalchemy as sa
from sqlalchemy import orm
orm.relationship = orm.relation
from wad.model import meta

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    meta.Session.configure(bind=engine)
    meta.engine = engine
    meta.connection = engine.connect()

guests_table = sa.Table(
    'guests', meta.metadata,
    sa.Column(
        'id', sa.types.Integer, sa.schema.Sequence(
            'guests_id_seq', optional= True
        ), primary_key = True
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
        'id', sa.types.Integer, sa.schema.Sequence(
            'invitations_id_seq', optional = True
        ), primary_key = True
    ),
    sa.Column('parties', sa.types.Integer()),
    sa.Column('code', sa.types.String(8)),
)

class Invitation(object):
    pass

orm.mapper(Invitation, invitations_table)

gifts_table = sa.Table(
    'gifts', meta.metadata,
    sa.Column(
        'id', sa.types.Integer, sa.schema.Sequence(
            'gifts_id_seq', optional = True
        ), primary_key = True
    ),
    sa.Column('name', sa.types.String(64)),
    sa.Column('photo', sa.types.String(64)),
    sa.Column('explanation', sa.types.Text),
    sa.Column('invitation_id', sa.types.Integer, sa.ForeignKey('invitations.id')),
)

class Gift(object):
    pass


sections_table = sa.Table(
    'sections', meta.metadata,
    sa.Column(
        'id', sa.types.Integer, sa.schema.Sequence(
            'sections_id_seq', optional = True
        ), primary_key = True
    ),
    sa.Column('title', sa.types.String(128)),
    sa.Column('order', sa.types.Integer),
)

class Section(object):
    pass

qnas_table = sa.Table(
    'qnas', meta.metadata,
    sa.Column(
        'id', sa.types.Integer, sa.schema.Sequence(
            'qnas_id_seq', optional = True
        ), primary_key = True
    ),
    sa.Column('question', sa.types.Text()),
    sa.Column('answer', sa.types.Text()),
    sa.Column('section_id', sa.types.Integer, sa.ForeignKey('sections.id')),
    sa.Column('order', sa.types.Integer),
)

class QNA(object):
    pass

orm.mapper(QNA, qnas_table)

orm.mapper(Section, sections_table, properties = {
    'qnas': orm.relationship(QNA, backref = 'section', order_by=qnas_table.c.order)
})

pages_table = sa.Table(
    'pages', meta.metadata,
    sa.Column(
        'id', sa.types.Integer, sa.schema.Sequence(
            'pages_id_seq', optional = True
        ), primary_key = True
    ),
    sa.Column('slug', sa.types.String(128)),
    sa.Column('content', sa.types.Text),
)

class Page(object):
    pass

orm.mapper(Page, pages_table)
