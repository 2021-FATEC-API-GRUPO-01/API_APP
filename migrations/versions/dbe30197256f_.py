"""empty message

Revision ID: dbe30197256f
Revises: 02c226aad929
Create Date: 2021-05-15 00:09:03.455258

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'dbe30197256f'
down_revision = '02c226aad929'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
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
    op.drop_table('transactions')
    op.drop_table('customers_products')
    op.drop_table('spc_raw_data')
    op.drop_table('raw_data')
    op.drop_table('customers')
    op.drop_table('schema_migrations')
    op.drop_table('products')
    op.drop_table('kaggle_raw_data')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
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
    sa.PrimaryKeyConstraint('id', name='kaggle_raw_data_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('products',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('category', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='products_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('schema_migrations',
    sa.Column('version', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('inserted_at', postgresql.TIMESTAMP(precision=0), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('version', name='schema_migrations_pkey')
    )
    op.create_table('customers',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), autoincrement=False, nullable=False),
    sa.Column('country', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('state', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('district', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('avg_income', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('raw_data_id', postgresql.UUID(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='customers_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('raw_data',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), autoincrement=False, nullable=False),
    sa.Column('birthday', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('avg_income', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('latitude', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('longitude', sa.VARCHAR(length=255), autoincrement=False, nullable=True)
    )
    op.create_table('spc_raw_data',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), autoincrement=False, nullable=False),
    sa.Column('birthday', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('avg_income', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('latitude', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('longitude', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='raw_data_pkey')
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
    op.create_table('transactions',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), autoincrement=False, nullable=False),
    sa.Column('customer_id', postgresql.UUID(), autoincrement=False, nullable=True),
    sa.Column('kaggle_raw_data_id', postgresql.UUID(), autoincrement=False, nullable=True),
    sa.Column('date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('value', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('total_limit', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('available_limit', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('category', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('country', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], name='transactions_customer_id_fkey'),
    sa.ForeignKeyConstraint(['kaggle_raw_data_id'], ['kaggle_raw_data.id'], name='transactions_kaggle_raw_data_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='transactions_pkey')
    )
    op.drop_table('users')
    # ### end Alembic commands ###
