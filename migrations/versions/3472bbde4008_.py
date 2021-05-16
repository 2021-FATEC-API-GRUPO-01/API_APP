"""empty message

Revision ID: 3472bbde4008
Revises: 2f6ccd0b1423
Create Date: 2021-05-15 01:04:27.660109

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3472bbde4008'
down_revision = '2f6ccd0b1423'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('category', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('schemamigrations',
    sa.Column('version', sa.BigInteger(), nullable=False),
    sa.Column('inserted_at', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('version')
    )
    op.create_table('spcrawdata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('birthday', sa.String(length=255), nullable=True),
    sa.Column('avg_income', sa.String(length=255), nullable=True),
    sa.Column('latitude', sa.String(length=255), nullable=True),
    sa.Column('longitude', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('country', sa.String(length=255), nullable=True),
    sa.Column('state', sa.String(length=255), nullable=True),
    sa.Column('city', sa.String(length=255), nullable=True),
    sa.Column('district', sa.String(length=255), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('avg_income', sa.Numeric(), nullable=True),
    sa.Column('spc_raw_data', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['spc_raw_data'], ['spcrawdata.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('customersproducts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('customer', sa.Integer(), nullable=True),
    sa.Column('product', sa.Integer(), nullable=True),
    sa.Column('inserted_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['customer'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['product'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('kagglerawdata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer', sa.Integer(), nullable=True),
    sa.Column('reference_id', sa.String(length=255), nullable=True),
    sa.Column('branch', sa.String(length=255), nullable=True),
    sa.Column('city', sa.String(length=255), nullable=True),
    sa.Column('state', sa.String(length=255), nullable=True),
    sa.Column('age', sa.String(length=255), nullable=True),
    sa.Column('gender', sa.String(length=255), nullable=True),
    sa.Column('total_limit', sa.String(length=255), nullable=True),
    sa.Column('available_limit', sa.String(length=255), nullable=True),
    sa.Column('date', sa.String(length=255), nullable=True),
    sa.Column('value', sa.String(length=255), nullable=True),
    sa.Column('group', sa.String(length=255), nullable=True),
    sa.Column('purchase_city', sa.String(length=255), nullable=True),
    sa.Column('purchase_country', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['customer'], ['customers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer', sa.Integer(), nullable=True),
    sa.Column('kaggle_raw_data', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('value', sa.Numeric(), nullable=True),
    sa.Column('total_limit', sa.Numeric(), nullable=True),
    sa.Column('available_limit', sa.Numeric(), nullable=True),
    sa.Column('category', sa.String(length=255), nullable=True),
    sa.Column('city', sa.String(length=255), nullable=True),
    sa.Column('country', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['customer'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['kaggle_raw_data'], ['kagglerawdata.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    op.drop_table('kagglerawdata')
    op.drop_table('customersproducts')
    op.drop_table('customers')
    op.drop_table('spcrawdata')
    op.drop_table('schemamigrations')
    op.drop_table('products')
    # ### end Alembic commands ###