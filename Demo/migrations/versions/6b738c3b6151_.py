"""empty message

Revision ID: 6b738c3b6151
Revises: dd5a932b7ec7
Create Date: 2021-06-09 18:52:55.728241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b738c3b6151'
down_revision = 'dd5a932b7ec7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('surname', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('date_time', sa.String(length=100), nullable=True),
    sa.Column('description', sa.Text(length=80), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('phone', sa.Text(length=80), nullable=False),
    sa.Column('image', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('profession',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('specialty', sa.String(length=20), nullable=False),
    sa.Column('description', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profession')
    op.drop_table('patient')
    # ### end Alembic commands ###
