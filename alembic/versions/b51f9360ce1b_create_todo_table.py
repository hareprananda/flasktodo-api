"""create todo table

Revision ID: b51f9360ce1b
Revises: f87e8597ea35
Create Date: 2022-07-02 10:55:41.031231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b51f9360ce1b'
down_revision = '1b4f81f07051'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'todo',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('status', sa.Integer, sa.ForeignKey('status.id'), nullable=False),
        sa.Column('user', sa.Integer, sa.ForeignKey('user.id'), nullable=False)
    )


def downgrade():
    op.drop_table('todo')
