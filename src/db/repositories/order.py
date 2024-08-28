from sqlalchemy import Integer, cast, delete, insert, select, text, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.functions import sum

from bot.structures.payment_status import PayStatus
from db.models.user import User
from db.repositories.abstract import AbstractRepository
from db.models.order import OrderItem, Order
from db.models.cart import Cart
from db.models.product import Product


class OrderItemRepo(AbstractRepository[OrderItem]):
    """Lesosn repository for CRUD and other SQL queries."""

    def __init__(self, session: AsyncSession):
        """Initialize user repository as for all users or only for one user."""
        super().__init__(model=OrderItem, session=session)

    async def get_by_order_id(self, order_id: int):
        query = select(self.model.order_id, self.model.quantity,
                       self.model.price, Product.title)\
            .join(Product, Product.id == self.model.product_id)\
            .filter(self.model.order_id==order_id)
        return await self.session.execute(query)


class OrderRepo(AbstractRepository[Order]):
    """Lesosn repository for CRUD and other SQL queries."""

    def __init__(self, session: AsyncSession):
        """Initialize user repository as for all users or only for one user."""
        super().__init__(model=Order, session=session)

    async def get_user_orders(self, user_id: int):
        query = select(Order).filter(User.user_id == user_id)
        return (await self.session.scalars(query)).all()

    async def update_payment_status(self, id: int, pay_status: PayStatus):
        statement = (
            update(self.model)
            .where(self.model.id==id)
            .values(payment_status_id=pay_status)
        ) 
        await self.session.execute(statement)
