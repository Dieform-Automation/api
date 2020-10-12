"""empty message

Revision ID: 636a31af0295
Revises: 
Create Date: 2020-10-12 15:26:08.531632

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '636a31af0295'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('api_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('password_hash', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('public_id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('blacklist_tokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=255), nullable=False),
    sa.Column('street', sa.String(length=255), nullable=False),
    sa.Column('city', sa.String(length=255), nullable=False),
    sa.Column('country', sa.String(length=255), nullable=False),
    sa.Column('province', sa.String(length=255), nullable=False),
    sa.Column('postal_code', sa.String(length=255), nullable=False),
    sa.Column('point_of_contact', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('purchase_order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('receiving_order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('customer_packing_slip', sa.String(length=255), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('part',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('purchase_order_id', sa.Integer(), nullable=True),
    sa.Column('number', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.ForeignKeyConstraint(['purchase_order_id'], ['purchase_order.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('received_part',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('part_id', sa.Integer(), nullable=True),
    sa.Column('receiving_order_id', sa.Integer(), nullable=True),
    sa.Column('part_quantity', sa.Integer(), nullable=False),
    sa.Column('bins', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['part_id'], ['part.id'], ),
    sa.ForeignKeyConstraint(['receiving_order_id'], ['receiving_order.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('received_part')
    op.drop_table('part')
    op.drop_table('receiving_order')
    op.drop_table('purchase_order')
    op.drop_table('customer')
    op.drop_table('blacklist_tokens')
    op.drop_table('api_user')
    # ### end Alembic commands ###