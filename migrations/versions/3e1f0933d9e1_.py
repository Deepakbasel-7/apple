"""empty message

Revision ID: 3e1f0933d9e1
Revises: a3eafa61d67f
Create Date: 2024-11-14 19:39:28.956509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e1f0933d9e1'
down_revision = 'a3eafa61d67f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wishlist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('quantity', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('customer_link', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('product_link', sa.Integer(), nullable=False))

        # Creating new foreign keys with explicit names
        batch_op.create_foreign_key('fk_wishlist_product_link', 'product', ['product_link'], ['id'])
        batch_op.create_foreign_key('fk_wishlist_customer_link', 'customer', ['customer_link'], ['id'])

        batch_op.drop_column('product_id')
        batch_op.drop_column('customer_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wishlist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('customer_id', sa.INTEGER(), nullable=False))
        batch_op.add_column(sa.Column('product_id', sa.INTEGER(), nullable=False))

        # Dropping the new foreign keys by name
        batch_op.drop_constraint('fk_wishlist_product_link', type_='foreignkey')
        batch_op.drop_constraint('fk_wishlist_customer_link', type_='foreignkey')

        # Re-adding the old foreign keys with their original names if needed
        batch_op.create_foreign_key('fk_wishlist_customer_id', 'customer', ['customer_id'], ['id'])
        batch_op.create_foreign_key('fk_wishlist_product_id', 'product', ['product_id'], ['id'])

        batch_op.drop_column('product_link')
        batch_op.drop_column('customer_link')
        batch_op.drop_column('quantity')
    # ### end Alembic commands ###