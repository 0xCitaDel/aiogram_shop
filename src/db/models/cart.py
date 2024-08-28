import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Cart(Base):
    __tablename__ = 'cart'

    user_id: Mapped[int] = mapped_column(
        sa.ForeignKey('users.user_id'), unique=False, nullable=False
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
