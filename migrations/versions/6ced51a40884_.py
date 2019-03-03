"""empty message

Revision ID: 6ced51a40884
Revises: 
Create Date: 2019-03-01 19:31:45.516045

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ced51a40884'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('timeblock', sa.Integer(), nullable=False),
    sa.Column('dateStart', sa.DateTime(), nullable=False),
    sa.Column('dateEnd', sa.DateTime(), nullable=False),
    sa.Column('token', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('timeranges',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('timeStart', sa.DateTime(), nullable=False),
    sa.Column('timeEnd', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('timeranges')
    op.drop_table('users')
    op.drop_table('events')
    # ### end Alembic commands ###