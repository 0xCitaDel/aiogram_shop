import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Product(Base):
    __tablename__ = 'products'

    title: Mapped[str] = mapped_column(
        sa.String(32), unique=True, nullable=False
    )
    price: Mapped[float] = mapped_column(
        sa.DECIMAL(10, 2), unique=False, nullable=False
    )
    # manufacturer_id: Mapped[int] = mapped_column(
    #     sa.ForeignKey('manufacturers.id'), unique=False, nullable=False
    # )
    category_id: Mapped[int] = mapped_column(
        sa.ForeignKey('categories.id'), unique=False, nullable=False
    )
    photo_id: Mapped[str] = mapped_column(
        sa.Text, unique=True, nullable=True
    )

class Property(Base):
    __tablename__ = 'product_properties'

    property_name: Mapped[str] = mapped_column(
        sa.String(32), unique=True, nullable=False
    )

class PropertyValue(Base):
    __tablename__ = 'product_property_values'

    property_id: Mapped[int] = mapped_column(
        sa.ForeignKey('product_properties.id'), unique=False, nullable=False
    )
    property_value: Mapped[str] = mapped_column(
        sa.String(32), unique=False, nullable=False
    )

class Characteristic (Base):
    __tablename__ = 'product_characteristics'

    product_id: Mapped[int] = mapped_column(
        sa.ForeignKey('products.id'), unique=False, nullable=False
    )
    property_id: Mapped[int] = mapped_column(
        sa.ForeignKey('product_properties.id'), unique=False, nullable=False
    )
    property_value_id: Mapped[int] = mapped_column(
        sa.ForeignKey('product_property_values.id'), unique=False, nullable=False
    )





