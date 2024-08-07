from sqlalchemy import Integer, cast, delete, insert, select, text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.functions import sum

from db.repositories.abstract import AbstractRepository
from db.models.order import OrderItem, OrderDetail
from db.models.cart import Cart
from db.models.product import Product
from db.models.payment import PaymentDetail


class OrderItemRepo(AbstractRepository[OrderItem]):
    """Lesosn repository for CRUD and other SQL queries."""

    def __init__(self, session: AsyncSession):
        """Initialize user repository as for all users or only for one user."""
        super().__init__(model=OrderItem, session=session)

    async def get_by_order_id(self, order_id: int):
        query = select(self.model.order_id, self.model.quanity,
                       self.model.price, Product.title)\
            .join(Product, Product.id == self.model.product_id)\
            .filter(self.model.order_id==order_id)
        return await self.session.execute(query)


class OrderDetailRepo(AbstractRepository[OrderDetail]):
    """Lesosn repository for CRUD and other SQL queries."""

    def __init__(self, session: AsyncSession):
        """Initialize user repository as for all users or only for one user."""
        super().__init__(model=OrderDetail, session=session)
