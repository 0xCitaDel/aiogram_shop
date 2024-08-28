from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine

from db.repositories.payment import PaymentRepo

from .repositories import (
    UserRepo,
    ProductRepo,
    CategoryRepo,
    CartRepo,
    CharacteristicRepo,
    OrderItemRepo,
    OrderRepo
)


def create_async_engine(url: URL | str, echo: bool) -> AsyncEngine:
    """Create async engine with given URL.

    :param url: URL to connect
    :return: AsyncEngine
    """
    return _create_async_engine(url=url, echo=echo, pool_pre_ping=True)


class Database:
    """Database class.

    is the highest abstraction level of database and
    can be used in the handlers or any others bot-side functions.
    """

    user: UserRepo
    cart: CartRepo
    category: CategoryRepo
    product: ProductRepo
    characteristic: CharacteristicRepo
    order_item: OrderItemRepo
    order_detail: OrderRepo
    payment: PaymentRepo
    """ User repository """

    session: AsyncSession

    def __init__(
        self,
        session: AsyncSession,
        user: UserRepo= None,
        cart: CartRepo = None,
        category: CategoryRepo = None,
        product: ProductRepo = None,
        characteristic: CharacteristicRepo= None,
        order_item: OrderItemRepo = None,
        order_detail: OrderRepo = None,
        payment: PaymentRepo = None
    ):
        """Initialize Database class.

        :param session: AsyncSession to use
        :param user: (Optional) User repository
        :param chat: (Optional) Chat repository
        """
        self.session = session
        self.user = user or UserRepo(session=session)
        self.cart = cart or CartRepo(session=session)
        self.category = category or CategoryRepo(session=session)
        self.product = product or ProductRepo(session=session)
        self.characteristic = characteristic or CharacteristicRepo(session=session)
        self.order_item = order_item or OrderItemRepo(session=session)
        self.order_detail = order_detail or OrderRepo(session=session)
        self.payment = payment or PaymentRepo(session=session)
