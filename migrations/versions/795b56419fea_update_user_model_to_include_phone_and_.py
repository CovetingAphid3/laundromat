"""Update User model to include phone and creation date

Revision ID: 795b56419fea
Revises: eddb4dc4dfaf
Create Date: 2023-07-09 15:55:26.247343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '795b56419fea'
down_revision = 'eddb4dc4dfaf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_orders')
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address', sa.String(), nullable=True))
        batch_op.alter_column('phone',
               existing_type=sa.VARCHAR(length=12),
               type_=sa.String(length=13),
               existing_nullable=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('phone', sa.String(length=13), nullable=True))
        batch_op.add_column(sa.Column('date_created', sa.DateTime(), nullable=True))

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
        batch_op.drop_column('address')

    op.create_table('_alembic_tmp_orders',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('phone', sa.VARCHAR(length=13), nullable=False),
    sa.Column('service', sa.VARCHAR(length=12), nullable=False),
    sa.Column('date', sa.DATE(), nullable=False),
    sa.Column('pick_up_time', sa.TIME(), nullable=False),
    sa.Column('special_instructions', sa.VARCHAR(length=250), nullable=True),
    sa.Column('image', sa.VARCHAR(length=50), nullable=False),
    sa.Column('status', sa.VARCHAR(), nullable=True),
    sa.Column('date_created', sa.DATETIME(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('price', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
