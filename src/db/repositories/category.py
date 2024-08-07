from typing import Optional

from sqlalchemy import select, ScalarResult
from sqlalchemy.ext.asyncio import AsyncSession

from db.repositories.abstract import AbstractRepository
from db.models.category import Category


class CategoryRepo(AbstractRepository[Category]):
    """Lesosn repository for CRUD and other SQL queries."""

    def __init__(self, session: AsyncSession):
        """Initialize user repository as for all users or only for one user."""
        super().__init__(model=Category, session=session)

    async def get_by_parent_category(self, parent_id: Optional[int]):
        """Get category by parent_id."""
        return await self.get_by_where(
            Category.parent_id == parent_id
        )
