"""add foreign-key to notes table

Revision ID: 0e637405350f
Revises: f73ed9d1fb73
Create Date: 2025-03-12 09:47:51.174508

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0e637405350f'
down_revision: Union[str, None] = 'f73ed9d1fb73'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('notes', sa.Column('user_id', sa.UUID(), nullable=False))
    op.create_foreign_key('note_users_fkey', 'notes', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('note_users_fkey', 'notes', type_='foreignkey')
    op.drop_column('notes', 'user_id')
    pass
