"""add status to order

Revision ID: b115ed26f101
Revises: eeaedc181238
Create Date: 2023-03-04 21:30:31.722201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b115ed26f101'
down_revision = 'eeaedc181238'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('status', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order', 'status')
    # ### end Alembic commands ###
