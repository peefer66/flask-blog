"""empty message

Revision ID: 6d83a103982c
Revises: None
Create Date: 2017-01-27 13:59:51.049674

"""

# revision identifiers, used by Alembic.
revision = '6d83a103982c'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('image', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'image')
    # ### end Alembic commands ###
