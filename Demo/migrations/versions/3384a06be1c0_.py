"""empty message

Revision ID: 3384a06be1c0
Revises: 84d89bbcbf2f
Create Date: 2021-06-16 09:38:24.068733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3384a06be1c0'
down_revision = '84d89bbcbf2f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('note', sa.Column('images', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('note', 'images')
    # ### end Alembic commands ###
