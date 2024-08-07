import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from bot.structures.payment_status import PayStatus


class PaymentDetail(Base):
    __tablename__ = 'payment_details'

    order_id: Mapped[int] = mapped_column(
        sa.Integer, unique=True, nullable=False
    )
    amount: Mapped[int] = mapped_column(
        sa.Integer, unique=False, nullable=False
    )
    status: Mapped[PayStatus] = mapped_column(
        sa.Enum(PayStatus), default=PayStatus.PENDING
    )
