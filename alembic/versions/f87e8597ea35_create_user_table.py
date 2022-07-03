"""create user table

Revision ID: f87e8597ea35
Revises: 
Create Date: 2022-06-30 08:49:41.808373

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f87e8597ea35'
down_revision = None
branch_labels = None
depends_on = None
  

def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('email', sa.String(30), nullable=False, unique=True),
        sa.Column('created_at', sa.TIMESTAMP, server_default=sa.func.now())
    )


def downgrade():
    op.drop_table('user')
