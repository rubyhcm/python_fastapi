"""add content column to notes table

Revision ID: 1564183216a6
Revises: 3f2cb1cd21cd
Create Date: 2025-03-12 09:41:05.341898

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1564183216a6'
down_revision: Union[str, None] = '3f2cb1cd21cd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('notes', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('notes', 'content')
    pass
