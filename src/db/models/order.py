import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class OrderDetail(Base):
    __tablename__ = 'order_details'

    user_id: Mapped[int] = mapped_column(
        sa.ForeignKey('users.user_id'), unique=False, nullable=False
    )
    total_amount: Mapped[float] = mapped_column(
        sa.DECIMAL(10, 2), unique=False, nullable=False
    )
    # payment_id: Mapped[int] = mapped_column(
    #     sa.ForeignKey('payment_details.id'), unique=False, nullable=False
    # )

class OrderItem(Base):
    __tablename__ = 'order_items'

    order_id: Mapped[int] = mapped_column(
        sa.ForeignKey('order_details.id'), unique=False, nullable=False
    )
    product_id: Mapped[int] = mapped_column(
        sa.ForeignKey('products.id'), unique=False, nullable=False
    )
    quanity: Mapped[int] = mapped_column(
        sa.Integer, unique=False, nullable=False
    )
    price: Mapped[float] = mapped_column(
        sa.DECIMAL(10, 2), unique=False, nullable=False
    )
