"""empty message

Revision ID: 339ceeb94fe6
Revises: a1d0f2f67358
Create Date: 2022-04-04 13:33:23.552401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '339ceeb94fe6'
down_revision = 'a1d0f2f67358'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'asset', 'mdgPrototype-users', ['owner_id'], ['id'])
    op.alter_column('mdgPrototype-users', 'profile_picture',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.create_unique_constraint(None, 'mdgPrototype-users', ['walletId'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'mdgPrototype-users', type_='unique')
    op.alter_column('mdgPrototype-users', 'profile_picture',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    op.drop_constraint(None, 'asset', type_='foreignkey')
    # ### end Alembic commands ###
