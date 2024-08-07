import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Category(Base):
    __tablename__ = 'categories'

    title: Mapped[str] = mapped_column(
        sa.String(32), unique=True, nullable=False
    )
    parent_id: Mapped[int] = mapped_column(
        sa.ForeignKey('categories.id'), unique=False, nullable=True, default=None
    )





