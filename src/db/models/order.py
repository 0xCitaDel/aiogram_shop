import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from bot.structures.order_status import OrderStatus
from bot.structures.payment_status import PayStatus

from .base import Base


class Order(Base):
    __tablename__ = 'orders'

    user_id: Mapped[int] = mapped_column(
        sa.ForeignKey('users.user_id'), unique=False, nullable=False
    )
    payment_uuid: Mapped[str] = mapped_column(
        sa.String, unique=True, nullable=True
    )
    total_amount: Mapped[float] = mapped_column(
        sa.DECIMAL(10, 2), unique=False, nullable=False
    )
    order_status_id: Mapped[OrderStatus] = mapped_column(
        sa.Enum(OrderStatus), default=OrderStatus.NEW
    )
    payment_status_id: Mapped[PayStatus] = mapped_column(
        sa.Enum(PayStatus), default=PayStatus.PENDING
    )
    shipping_address: Mapped[str] = mapped_column(
        sa.String(256), unique=False, nullable=False
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=sa.text("TIMEZONE('utc', now())")
    )

class OrderItem(Base):
    __tablename__ = 'order_items'

    order_id: Mapped[int] = mapped_column(
        sa.ForeignKey('orders.id'), unique=False, nullable=False
    )
    product_id: Mapped[int] = mapped_column(
        sa.ForeignKey('products.id'), unique=False, nullable=False
    )
    quantity: Mapped[int] = mapped_column(
        sa.Integer, unique=False, nullable=False
    )
    price: Mapped[float] = mapped_column(
        sa.DECIMAL(10, 2), unique=False, nullable=False
    )
    total_price: Mapped[float] = mapped_column(
        sa.DECIMAL(10, 2), unique=False, nullable=False
    )
