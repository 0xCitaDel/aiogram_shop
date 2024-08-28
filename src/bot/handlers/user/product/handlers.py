from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot import states as st
from services.category import check_and_add_to_cart

async def add_cart(
        callback: CallbackQuery,
        widget: Button,
        manager: DialogManager
    ):
    db = manager.middleware_data['db']
    product_id = manager.dialog_data['product_id']
    product_price = manager.dialog_data['product_price']
    user_id = callback.from_user.id
    quantity = manager.current_context().widget_data['counter']
    await check_and_add_to_cart(db, user_id, product_id, quantity, product_price)
    await manager.switch_to(st.ProductSG.start)

async def go_cart(
        callback: CallbackQuery,
        widget: Button,
        manager: DialogManager
    ):
    await manager.start(st.CartSG.start)

