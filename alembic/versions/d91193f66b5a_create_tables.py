"""create tables

Revision ID: d91193f66b5a
Revises: c47ecbf163d4
Create Date: 2024-07-05 13:02:59.575405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd91193f66b5a'
down_revision = 'c47ecbf163d4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts')
    pass


def downgrade():
    pass
