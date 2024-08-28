from sqlalchemy import insert, update
from sqlalchemy.ext.asyncio import AsyncSession

from bot.structures.payment_status import PayStatus
from db.models.payment import Payment
from db.repositories.abstract import AbstractRepository


class PaymentRepo(AbstractRepository[Payment]):
    """Lesosn repository for CRUD and other SQL queries."""

    def __init__(self, session: AsyncSession):
        """Initialize user repository as for all users or only for one user."""
        super().__init__(model=Payment, session=session)

    async def create_payment(self, order_id, payment_uuid, amount):
        statement = (
            insert(self.model)
            .values(
                order_id=order_id,
                payment_uuid=payment_uuid,
                amount=amount,
                status=PayStatus.PENDING
            )
        )
        await self.session.execute(statement)

    async def update_payment_status(self, uuid: str, pay_status: PayStatus):
        statement = (
            update(self.model)
            .where(self.model.payment_uuid==uuid)
            .values(
                status=pay_status)
        ) 
        await self.session.execute(statement)
