"""Update User model to include phone and creation date

Revision ID: eddb4dc4dfaf
Revises: 4f12781ce64f
Create Date: 2023-07-09 15:48:55.663606

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eddb4dc4dfaf'
down_revision = '4f12781ce64f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.alter_column('phone',
               existing_type=sa.VARCHAR(length=12),
               type_=sa.String(length=13),
               existing_nullable=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('phone', sa.String(length=13), nullable=False))
        batch_op.add_column(sa.Column('date_created', sa.DateTime(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('date_created')
        batch_op.drop_column('phone')

    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.alter_column('phone',
               existing_type=sa.String(length=13),
               type_=sa.VARCHAR(length=12),
               existing_nullable=False)

    # ### end Alembic commands ###
