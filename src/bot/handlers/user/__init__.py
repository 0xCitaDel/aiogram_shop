from aiogram import Router

from .cart import cart_dialog
from .catalog import catalog_dialog
from .order import order_dialog
from .product import product_dialog


user_router = Router()


user_router.include_router(catalog_dialog)
user_router.include_router(product_dialog)
user_router.include_router(order_dialog)
user_router.include_router(cart_dialog)
