"""updated bird model to reflect false unique attr

Revision ID: 90b361d75d24
Revises: 205b4840b9bf
Create Date: 2021-10-15 13:50:49.553787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90b361d75d24'
down_revision = '205b4840b9bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('birds_bird_type_key', 'birds', type_='unique')
    op.drop_constraint('birds_color_key', 'birds', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('birds_color_key', 'birds', ['color'])
    op.create_unique_constraint('birds_bird_type_key', 'birds', ['bird_type'])
    # ### end Alembic commands ###
