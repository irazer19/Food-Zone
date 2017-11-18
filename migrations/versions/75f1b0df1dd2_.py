"""empty message

Revision ID: 75f1b0df1dd2
Revises: 86cf285d94f9
Create Date: 2017-11-18 07:35:36.517835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75f1b0df1dd2'
down_revision = '86cf285d94f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('menu_items', sa.Column('description', sa.String(length=250), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('menu_items', 'description')
    # ### end Alembic commands ###