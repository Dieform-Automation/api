"""empty message

Revision ID: cf3ab8202674
Revises: a96ff79cc6dd
Create Date: 2020-11-13 15:49:01.659075

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf3ab8202674'
down_revision = 'a96ff79cc6dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shipped_part',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('part_id', sa.Integer(), nullable=True),
    sa.Column('shipment_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('bins', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['part_id'], ['part.id'], ),
    sa.ForeignKeyConstraint(['shipment_id'], ['shipment.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shipped_part')
    # ### end Alembic commands ###
