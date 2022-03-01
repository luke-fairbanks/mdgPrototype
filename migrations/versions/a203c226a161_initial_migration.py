"""Initial migration

Revision ID: a203c226a161
Revises: 
Create Date: 2022-02-21 12:31:41.677026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a203c226a161'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mdgPrototype-users', sa.Column('walletId', sa.String(length=200), nullable=True))
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
    op.drop_column('mdgPrototype-users', 'walletId')
    # ### end Alembic commands ###