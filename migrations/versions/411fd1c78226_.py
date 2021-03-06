"""empty message

Revision ID: 411fd1c78226
Revises: a40c2e3028d9
Create Date: 2021-04-27 03:34:47.962837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '411fd1c78226'
down_revision = 'a40c2e3028d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('shops_malls_shop_id_fkey', 'shops_malls', type_='foreignkey')
    op.drop_constraint('shops_malls_mall_id_fkey', 'shops_malls', type_='foreignkey')
    op.create_foreign_key(None, 'shops_malls', 'shop', ['shop_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'shops_malls', 'mall', ['mall_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'shops_malls', type_='foreignkey')
    op.drop_constraint(None, 'shops_malls', type_='foreignkey')
    op.create_foreign_key('shops_malls_mall_id_fkey', 'shops_malls', 'mall', ['mall_id'], ['id'])
    op.create_foreign_key('shops_malls_shop_id_fkey', 'shops_malls', 'shop', ['shop_id'], ['id'])
    # ### end Alembic commands ###
