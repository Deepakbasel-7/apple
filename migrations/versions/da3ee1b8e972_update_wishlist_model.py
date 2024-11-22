"""Update Wishlist model

Revision ID: da3ee1b8e972
Revises: 3e1f0933d9e1
Create Date: 2024-11-14 20:40:43.206534

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da3ee1b8e972'
down_revision = '3e1f0933d9e1'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wishlist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('customer_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('product_id', sa.Integer(), nullable=False))
        
        # Drop old constraints with explicit names
        batch_op.drop_constraint('fk_wishlist_customer_link', type_='foreignkey')
        batch_op.drop_constraint('fk_wishlist_product_link', type_='foreignkey')
        
        # Create new foreign key constraints with explicit names
        batch_op.create_foreign_key('fk_wishlist_customer_id', 'customer', ['customer_id'], ['id'])
        batch_op.create_foreign_key('fk_wishlist_product_id', 'product', ['product_id'], ['id'])
        
        batch_op.drop_column('customer_link')
        batch_op.drop_column('product_link')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wishlist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('product_link', sa.INTEGER(), nullable=False))
        batch_op.add_column(sa.Column('customer_link', sa.INTEGER(), nullable=False))
        
        # Drop new constraints with explicit names
        batch_op.drop_constraint('fk_wishlist_customer_id', type_='foreignkey')
        batch_op.drop_constraint('fk_wishlist_product_id', type_='foreignkey')
        
        # Recreate the old foreign key constraints with their original names
        batch_op.create_foreign_key('fk_wishlist_product_link', 'product', ['product_link'], ['id'])
        batch_op.create_foreign_key('fk_wishlist_customer_link', 'customer', ['customer_link'], ['id'])
        
        batch_op.drop_column('product_id')
        batch_op.drop_column('customer_id')
    # ### end Alembic commands ###

