import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from bot.structures.payment_status import PayStatus


class Payment(Base):
    __tablename__ = 'payments'

    order_id: Mapped[int] = mapped_column(
        sa.ForeignKey('orders.id'), unique=True, nullable=False
    )
    payment_uuid: Mapped[str] = mapped_column(
        sa.String, unique=True, nullable=False
    )
    amount: Mapped[int] = mapped_column(
        sa.Integer, unique=False, nullable=False
    )
    status: Mapped[PayStatus] = mapped_column(
        sa.Enum(PayStatus), default=PayStatus.PENDING
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=sa.text("TIMEZONE('utc', now())")
    )
