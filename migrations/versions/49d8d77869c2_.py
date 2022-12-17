"""empty message

Revision ID: 49d8d77869c2
Revises: 
Create Date: 2022-12-17 16:12:29.556663

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '49d8d77869c2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('artists', schema=None) as batch_op:
        batch_op.drop_column('av_start')
        batch_op.drop_column('av_end')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('artists', schema=None) as batch_op:
        batch_op.add_column(sa.Column('av_end', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('av_start', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
