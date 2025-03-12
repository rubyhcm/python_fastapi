"""add votes table

Revision ID: c3c395990db1
Revises: bf0c756149d2
Create Date: 2025-03-12 10:20:50.660672

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3c395990db1'
down_revision: Union[str, None] = 'bf0c756149d2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('votes',
        sa.Column('user_id', sa.UUID(), nullable=False),
        sa.Column('note_id', sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(['note_id'], ['notes.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('user_id', 'note_id')
    )


def downgrade() -> None:
    op.drop_table('votes')
