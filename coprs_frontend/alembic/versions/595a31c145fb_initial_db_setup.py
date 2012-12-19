"""Initial DB setup

Revision ID: 595a31c145fb
Revises: None
Create Date: 2012-11-26 09:39:51.229910

"""

# revision identifiers, used by Alembic.
revision = '595a31c145fb'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('openid_name', sa.String(length=100), nullable=False),
    sa.Column('mail', sa.String(length=150), nullable=False),
    sa.Column('proven', sa.Boolean(), nullable=True),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('copr',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('chroots', sa.Text(), nullable=False),
    sa.Column('repos', sa.Text(), nullable=True),
    sa.Column('created_on', sa.Integer(), nullable=True),
    sa.Column('build_count', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('build',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pkgs', sa.Text(), nullable=True),
    sa.Column('canceled', sa.Boolean(), nullable=True),
    sa.Column('chroots', sa.Text(), nullable=False),
    sa.Column('repos', sa.Text(), nullable=True),
    sa.Column('submitted_on', sa.Integer(), nullable=False),
    sa.Column('started_on', sa.Integer(), nullable=True),
    sa.Column('ended_on', sa.Integer(), nullable=True),
    sa.Column('results', sa.Text(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('memory_reqs', sa.Integer(), nullable=True),
    sa.Column('timeout', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('copr_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['copr_id'], ['copr.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('copr_permission',
    sa.Column('copr_builder', sa.SmallInteger(), nullable=True),
    sa.Column('copr_admin', sa.SmallInteger(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('copr_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['copr_id'], ['copr.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'copr_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('copr_permission')
    op.drop_table('build')
    op.drop_table('copr')
    op.drop_table('user')
    ### end Alembic commands ###
