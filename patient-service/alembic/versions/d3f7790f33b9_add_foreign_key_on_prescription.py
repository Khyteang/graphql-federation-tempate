"""add foreign key on prescription

Revision ID: d3f7790f33b9
Revises: a58d39783aa6
Create Date: 2023-03-04 20:29:30.861082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3f7790f33b9'
down_revision = 'a58d39783aa6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('prescription', sa.Column('patient_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'prescription', 'patient', ['patient_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'prescription', type_='foreignkey')
    op.drop_column('prescription', 'patient_id')
    # ### end Alembic commands ###