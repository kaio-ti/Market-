"""testando sapraga

Revision ID: 7661b3783bdf
Revises: 
Create Date: 2021-12-13 16:20:01.897784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7661b3783bdf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('category', sa.String(length=30), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('stores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('state', sa.String(length=20), nullable=False),
    sa.Column('phone_number', sa.String(length=20), nullable=True),
    sa.Column('cnpj', sa.String(length=14), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cnpj')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('state', sa.String(length=2), nullable=False),
    sa.Column('country', sa.String(length=6), nullable=True),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('products_img',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('img', sa.LargeBinary(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('mimetype', sa.Text(), nullable=False),
    sa.Column('products_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['products_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products_store',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('store_id', sa.Integer(), nullable=False),
    sa.Column('price_by_store', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['store_id'], ['stores.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('users_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sugestions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=20), nullable=False),
    sa.Column('message', sa.String(length=250), nullable=False),
    sa.Column('users_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users_img',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('img', sa.LargeBinary(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('mimetype', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_img')
    op.drop_table('sugestions')
    op.drop_table('products_users')
    op.drop_table('products_store')
    op.drop_table('products_img')
    op.drop_table('users')
    op.drop_table('stores')
    op.drop_table('products')
    # ### end Alembic commands ###
