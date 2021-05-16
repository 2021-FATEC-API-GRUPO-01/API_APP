"""empty message

Revision ID: 65d41e59bc74
Revises: 85d221ae7ee6
Create Date: 2021-05-15 02:08:40.481140

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '65d41e59bc74'
down_revision = '85d221ae7ee6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schemamigrations',
    sa.Column('version', sa.BigInteger(), nullable=False),
    sa.Column('inserted_at', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('version')
    )
    op.create_table('spcrawdata',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('birthday', sa.String(length=255), nullable=True),
    sa.Column('avg_income', sa.String(length=255), nullable=True),
    sa.Column('latitude', sa.String(length=255), nullable=True),
    sa.Column('longitude', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_state', sa.String(length=30), nullable=True),
    sa.Column('customer_city', sa.String(length=30), nullable=True),
    sa.Column('customer_age', sa.Float(), nullable=True),
    sa.Column('customer_avg_income', sa.Integer(), nullable=True),
    sa.Column('customer_products_active', sa.Boolean(), nullable=True),
    sa.Column('transactions_total_limit', sa.Float(), nullable=True),
    sa.Column('transactions_category', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('customersproducts',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('customer', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('product', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('inserted_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['customer'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['product'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('kagglerawdata',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('customer', postgresql.UUID(as_uuid=True), nullable=True),
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
    op.drop_table('spc_raw_data')
    op.drop_table('kaggle_raw_data')
    op.drop_table('customers_products')
    op.drop_table('schema_migrations')
    op.drop_constraint('customers_raw_data_id_fkey', 'customers', type_='foreignkey')
    op.create_foreign_key(None, 'customers', 'spcrawdata', ['spc_raw_data_id'], ['id'])
    op.alter_column('products', 'name',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('products', 'category',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.add_column('transactions', sa.Column('customer', postgresql.UUID(as_uuid=True), nullable=True))
    op.add_column('transactions', sa.Column('kaggle_raw_data', postgresql.UUID(as_uuid=True), nullable=True))
    op.drop_constraint('transactions_kaggle_raw_data_id_fkey', 'transactions', type_='foreignkey')
    op.drop_constraint('transactions_customer_id_fkey', 'transactions', type_='foreignkey')
    op.create_foreign_key(None, 'transactions', 'kagglerawdata', ['kaggle_raw_data'], ['id'])
    op.create_foreign_key(None, 'transactions', 'customers', ['customer'], ['id'])
    op.drop_column('transactions', 'kaggle_raw_data_id')
    op.drop_column('transactions', 'customer_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transactions', sa.Column('customer_id', postgresql.UUID(), autoincrement=False, nullable=True))
    op.add_column('transactions', sa.Column('kaggle_raw_data_id', postgresql.UUID(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'transactions', type_='foreignkey')
    op.drop_constraint(None, 'transactions', type_='foreignkey')
    op.create_foreign_key('transactions_customer_id_fkey', 'transactions', 'customers', ['customer_id'], ['id'])
    op.create_foreign_key('transactions_kaggle_raw_data_id_fkey', 'transactions', 'kaggle_raw_data', ['kaggle_raw_data_id'], ['id'])
    op.drop_column('transactions', 'kaggle_raw_data')
    op.drop_column('transactions', 'customer')
    op.alter_column('products', 'category',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('products', 'name',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.drop_constraint(None, 'customers', type_='foreignkey')
    op.create_foreign_key('customers_raw_data_id_fkey', 'customers', 'spc_raw_data', ['spc_raw_data_id'], ['id'])
    op.create_table('schema_migrations',
    sa.Column('version', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('inserted_at', postgresql.TIMESTAMP(precision=0), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('version', name='schema_migrations_pkey')
    )
    op.create_table('customers_products',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), autoincrement=False, nullable=False),
    sa.Column('active', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False),
    sa.Column('customer_id', postgresql.UUID(), autoincrement=False, nullable=True),
    sa.Column('product_id', postgresql.UUID(), autoincrement=False, nullable=True),
    sa.Column('inserted_at', postgresql.TIMESTAMP(precision=0), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(precision=0), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], name='customers_products_customer_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name='customers_products_product_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='customers_products_pkey')
    )
    op.create_table('kaggle_raw_data',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), autoincrement=False, nullable=False),
    sa.Column('customer_id', postgresql.UUID(), autoincrement=False, nullable=True),
    sa.Column('reference_id', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('branch', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('state', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('age', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('gender', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('total_limit', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('available_limit', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('date', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('value', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('group', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('purchase_city', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('purchase_country', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], name='kaggle_raw_data_customer_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='kaggle_raw_data_pkey')
    )
    op.create_table('spc_raw_data',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), autoincrement=False, nullable=False),
    sa.Column('birthday', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('avg_income', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('latitude', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('longitude', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='raw_data_pkey')
    )
    op.drop_table('kagglerawdata')
    op.drop_table('customersproducts')
    op.drop_table('users')
    op.drop_table('spcrawdata')
    op.drop_table('schemamigrations')
    # ### end Alembic commands ###
