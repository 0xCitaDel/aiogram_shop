from typing import Optional

from sqlalchemy import insert, select, ScalarResult
from sqlalchemy.ext.asyncio import AsyncSession

from db.repositories.abstract import AbstractRepository
from db.models.product import Product, Characteristic, Property, PropertyValue


class ProductRepo(AbstractRepository[Product]):
    """Lesosn repository for CRUD and other SQL queries."""

    def __init__(self, session: AsyncSession):
        """Initialize user repository as for all users or only for one user."""
        super().__init__(model=Product, session=session)

    async def get_product_by_category(self, category_id: Optional[int]):
        """Get category by parent_id."""
        return await self.get_by_where(
            Product.category_id == category_id
        )

    async def add_product_by_category(
        self, category_id: Optional[int],
        title, description, price, photo_id,
    ):
        """Get category by parent_id."""
        statement = insert(self.model).values(
            title=title,
            description=description,
            price=price,
            photo_id=photo_id,
            category_id=category_id
        )
        await self.session.execute(statement)
        await self.session.commit()


class CharacteristicRepo(AbstractRepository[Characteristic]):
    """Lesosn repository for CRUD and other SQL queries."""

    def __init__(self, session: AsyncSession):
        """Initialize user repository as for all users or only for one user."""
        super().__init__(model=Characteristic, session=session)

    async def get_product_characteristics(self, product_id: int):
        statement = select(
            Characteristic.id, Product.title,
            Property.property_name, PropertyValue.property_value)\
            .select_from(Characteristic)\
            .join(Product, Product.id == Characteristic.product_id)\
            .join(Property, Property.id == Characteristic.property_id)\
            .join(PropertyValue, PropertyValue.id == Characteristic.property_value_id)\
            .filter(Characteristic.product_id == product_id)
        res = await self.session.execute(statement)
        return res.all()
