"""empty message

Revision ID: 46b3390adcfa
Revises: 9c115618878f
Create Date: 2021-05-12 19:57:53.408574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46b3390adcfa'
down_revision = '9c115618878f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('transactions_category', sa.String(length=30), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'transactions_category')
    # ### end Alembic commands ###