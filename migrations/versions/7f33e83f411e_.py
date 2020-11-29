"""empty message

Revision ID: 7f33e83f411e
Revises: c786d27a9c5f
Create Date: 2020-11-29 17:33:43.867154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f33e83f411e'
down_revision = 'c786d27a9c5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('received_part', sa.Column('quantity', sa.Integer(), nullable=False))
    op.drop_column('received_part', 'part_quantity')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('received_part', sa.Column('part_quantity', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('received_part', 'quantity')
    # ### end Alembic commands ###
