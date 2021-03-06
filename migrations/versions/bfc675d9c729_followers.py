"""followers

Revision ID: bfc675d9c729
Revises: 127033f3f54f
Create Date: 2020-07-14 16:13:58.055285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfc675d9c729'
down_revision = '127033f3f54f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('followers', sa.Column('following_id', sa.Integer(), nullable=True))
    op.drop_constraint(None, 'followers', type_='foreignkey')
    op.create_foreign_key(None, 'followers', 'user', ['following_id'], ['id'])
    op.drop_column('followers', 'followed_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('followers', sa.Column('followed_id', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'followers', type_='foreignkey')
    op.create_foreign_key(None, 'followers', 'user', ['followed_id'], ['id'])
    op.drop_column('followers', 'following_id')
    # ### end Alembic commands ###
