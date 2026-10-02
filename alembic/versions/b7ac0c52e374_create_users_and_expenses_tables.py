"""create users and expenses tables

Revision ID: b7ac0c52e374
Revises: 
Create Date: 2026-09-30 13:10:01.858824

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b7ac0c52e374'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(length=100), nullable=False),
        sa.Column('hashed_password', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_index(
        op.f('ix_users_email'),
        'users',
        ['email'],
        unique=True
    )

    op.create_index(
        op.f('ix_users_id'),
        'users',
        ['id'],
        unique=False
    )

    op.create_table(
        'expenses',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('amount', sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column('category', sa.String(length=50), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_index(
        op.f('ix_expenses_id'),
        'expenses',
        ['id'],
        unique=False
    )



def downgrade() -> None:
    """Downgrade schema."""

    op.drop_index(
        op.f('ix_expenses_id'),
        table_name='expenses'
    )
    op.drop_table('expenses')

    op.drop_index(
        op.f('ix_users_id'),
        table_name='users'
    )
    op.drop_index(
        op.f('ix_users_email'),
        table_name='users'
    )
    op.drop_table('users')

    # ### end Alembic commands ###
