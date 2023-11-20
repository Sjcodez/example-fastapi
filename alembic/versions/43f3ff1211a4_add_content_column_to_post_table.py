"""add content column to post table

Revision ID: 43f3ff1211a4
Revises: e4b4f0d17676
Create Date: 2023-11-20 11:15:24.156836

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '43f3ff1211a4'
down_revision: Union[str, None] = 'e4b4f0d17676'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content') 
    pass
