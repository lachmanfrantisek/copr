"""add index to build_chroot.ended_on column

Revision ID: 3a9905ed8ffd
Revises: 3341bf554454
Create Date: 2016-09-27 11:57:50.075139

"""

# revision identifiers, used by Alembic.
revision = '3a9905ed8ffd'
down_revision = '3341bf554454'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_build_chroot_ended_on'), 'build_chroot', ['ended_on'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_build_chroot_ended_on', table_name='build_chroot')
    ### end Alembic commands ###
