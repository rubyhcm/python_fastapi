"""add phone_number to users table

Revision ID: 82e055d62b95
Revises: c3c395990db1
Create Date: 2025-03-12 10:45:11.163501

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '82e055d62b95'
down_revision: Union[str, None] = 'c3c395990db1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    pass


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
    pass
