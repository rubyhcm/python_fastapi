"""add some columns to notes table

Revision ID: bf0c756149d2
Revises: 0e637405350f
Create Date: 2025-03-12 10:13:45.534446

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bf0c756149d2'
down_revision: Union[str, None] = '0e637405350f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('notes', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('notes', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('notes', 'published')
    op.drop_column('notes', 'created_at')
    pass
