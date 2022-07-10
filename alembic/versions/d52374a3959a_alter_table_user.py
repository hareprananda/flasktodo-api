"""alter_table_user

Revision ID: d52374a3959a
Revises: b51f9360ce1b
Create Date: 2022-07-03 15:40:21.349343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd52374a3959a'
down_revision = 'b51f9360ce1b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'user', 
        sa.Column('password', sa.String(200), nullable=False),
    )


def downgrade() -> None:
    op.drop_column('user', 'password')
