"""add last few columns to posts table

Revision ID: 7af0bd392eb5
Revises: 80a826dae4a9
Create Date: 2023-11-20 11:39:34.492765

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7af0bd392eb5'
down_revision: Union[str, None] = '80a826dae4a9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'posts', 
        sa.Column('published', sa.Boolean(), nullable=False, server_default='True'),
    )
    op.add_column(
        'posts',
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),
    )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
