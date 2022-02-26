"""empty message

Revision ID: 99743fb41dc2
Revises: 21ef4005d6bc
Create Date: 2022-02-25 00:16:16.391941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99743fb41dc2'
down_revision = '21ef4005d6bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
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
    # ### end Alembic commands ###
