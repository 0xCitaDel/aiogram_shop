import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from bot.structures.role import Role

from .base import Base


class User(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(
        sa.BigInteger, unique=True, nullable=False
    )
    user_name: Mapped[str] = mapped_column(
        sa.Text, unique=False, nullable=True
    )
    first_name: Mapped[str] = mapped_column(
        sa.Text, unique=False, nullable=True
    )
    second_name: Mapped[str] = mapped_column(
        sa.Text, unique=False, nullable=True
    )
    phone_number: Mapped[str] = mapped_column(
        sa.String(20), unique=False, nullable=True
    )
    address: Mapped[str] = mapped_column(
        sa.String(256), unique=False, nullable=True
    )
    is_premium: Mapped[bool] = mapped_column(
        sa.Boolean, unique=False, nullable=False
    )
    is_banned: Mapped[bool] = mapped_column(
        sa.Boolean, unique=False, nullable=False, default=False
    )
    role: Mapped[Role] = mapped_column(
        sa.Enum(Role), default=Role.USER
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=sa.text("TIMEZONE('utc', now())")
    )
