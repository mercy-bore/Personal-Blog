"""Comments id Migration

Revision ID: 13c800c71b8c
Revises: 8b25b23d386f
Create Date: 2022-03-12 10:11:58.741849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13c800c71b8c'
down_revision = '8b25b23d386f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('blog_id', sa.Integer(), nullable=False))
    op.drop_constraint('comments_blogs_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'blogs', ['blog_id'], ['id'])
    op.drop_column('comments', 'blogs_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('blogs_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_blogs_id_fkey', 'comments', 'blogs', ['blogs_id'], ['id'])
    op.drop_column('comments', 'blog_id')
    # ### end Alembic commands ###