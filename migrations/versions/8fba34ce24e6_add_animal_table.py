"""add animal table

Revision ID: 8fba34ce24e6
Revises: 
Create Date: 2024-02-25 15:59:51.980457

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fba34ce24e6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('animal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('species', sa.String(length=100), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(length=100), nullable=True),
    sa.Column('special_requirement', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('role', sa.String(length=100), nullable=True),
    sa.Column('schedule', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('enclosure',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('feeding',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('animal_id', sa.Integer(), nullable=False),
    sa.Column('enclosure_id', sa.Integer(), nullable=False),
    sa.Column('time', sa.String(length=20), nullable=False),
    sa.Column('food', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['animal_id'], ['animal.id'], ),
    sa.ForeignKeyConstraint(['enclosure_id'], ['enclosure.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('feeding')
    op.drop_table('enclosure')
    op.drop_table('employee')
    op.drop_table('animal')
    # ### end Alembic commands ###