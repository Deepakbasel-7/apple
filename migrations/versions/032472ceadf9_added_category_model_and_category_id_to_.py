"""Added Category model and category_id to Product with named constraint

Revision ID: 032472ceadf9
Revises: 959e0e181ca0
Create Date: 2024-11-22 15:13:22.765474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '032472ceadf9'
down_revision = '959e0e181ca0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category_id', sa.Integer(), nullable=True))
        batch_op.alter_column('previous_price',
               existing_type=sa.FLOAT(),
               nullable=True)
        batch_op.alter_column('in_stock',
               existing_type=sa.INTEGER(),
               type_=sa.Boolean(),
               nullable=True)
        batch_op.alter_column('product_picture',
               existing_type=sa.VARCHAR(length=1000),
               type_=sa.String(length=200),
               nullable=True)
        batch_op.create_foreign_key('fk_category_product', 'category', ['category_id'], ['id'])
        batch_op.drop_column('category')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category', sa.VARCHAR(length=100), nullable=True))
        batch_op.drop_constraint('fk_category_product', type_='foreignkey')
        batch_op.alter_column('product_picture',
               existing_type=sa.String(length=200),
               type_=sa.VARCHAR(length=1000),
               nullable=False)
        batch_op.alter_column('in_stock',
               existing_type=sa.Boolean(),
               type_=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('previous_price',
               existing_type=sa.FLOAT(),
               nullable=False)
        batch_op.drop_column('category_id')

    # ### end Alembic commands ###
