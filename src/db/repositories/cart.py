from typing import Optional

from sqlalchemy import and_, delete, select, ScalarResult
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.functions import sum

from db.repositories.abstract import AbstractRepository
from db.models.cart import Cart
from db.models.product import Product


class CartRepo(AbstractRepository[Cart]):
    """Lesosn repository for CRUD and other SQL queries."""

    def __init__(self, session: AsyncSession):
        """Initialize user repository as for all users or only for one user."""
        super().__init__(model=Cart, session=session)
    
    async def add_product_in_cart(self, user_id: int, product_id: int, quanity: int, price: int):
        return await self.new(user_id=user_id, product_id=product_id, quanity=quanity, price=price)

    async def get_total_amount(self, user_id: int):
        """Get total amount in user's cart"""
        query = select(sum(self.model.quanity * self.model.price))\
            .filter(self.model.user_id==user_id)
        return await self.session.scalar(query)

    async def get_by_user(self, user_id: int):
        query = select(self.model).filter(self.model.user_id==user_id)
        return await self.session.scalars(query)

    async def delete_by_user(self, user_id: int):
        stmt = delete(self.model).filter(self.model.user_id==user_id)
        await self.session.execute(stmt)

    async def get_products(self, user_id: int):
        query = select(Cart.id, Cart.product_id,
                       Cart.quanity, Product.title,
                       Product.price, Product.photo_id)\
        .select_from(Cart)\
        .join(Product, Product.id == Cart.product_id)\
        .filter(Cart.user_id==user_id)
        res = await self.session.execute(query)
        return res.all()


    async def get_user_product(self, user_id: int, product_id: int):
        query = select(self.model)\
            .where(Cart.user_id == user_id)\
            .where(Cart.product_id == product_id)
        res = (await self.session.execute(query)).scalar()
        return res
    
        
