import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Manufacturer(Base):
    __tablename__ = 'manufacturers'

    title: Mapped[str] = mapped_column(
        sa.String(32), unique=True, nullable=False
    )





