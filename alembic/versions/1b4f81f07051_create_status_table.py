"""create status table

Revision ID: 1b4f81f07051
Revises: b51f9360ce1b
Create Date: 2022-07-02 11:04:32.845315

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b4f81f07051'
down_revision = 'f87e8597ea35'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'status',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(200),nullable=False),
    )


def downgrade():
    op.drop_table('status')
