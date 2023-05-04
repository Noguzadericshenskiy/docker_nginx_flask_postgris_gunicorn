"""init

Revision ID: 5bc4e11de8ef
Revises: 
Create Date: 2023-05-04 20:48:05.186822

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5bc4e11de8ef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('has_sale', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('address', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('coffee_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['coffee_id'], ['coffee.id'], name='users_coffee_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='users_pkey')
    )
    op.create_table('coffee',
    sa.Column('title', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('origin', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('intensifier', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('notes', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='coffee_pkey')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('coffee')
    op.drop_table('users')

    # ### end Alembic commands ###
