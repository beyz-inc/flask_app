"""empty message

Revision ID: 5b8e7a527c2d
Revises: 159dbdfe42c1
Create Date: 2024-02-15 16:55:22.053227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b8e7a527c2d'
down_revision = '159dbdfe42c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('last_active', sa.DateTime(), nullable=True))
    op.drop_column('users', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_active', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False))
    op.drop_column('users', 'last_active')
    # ### end Alembic commands ###
