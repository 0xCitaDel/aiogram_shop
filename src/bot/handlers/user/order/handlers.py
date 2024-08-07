from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot.states import OrderSG

async def pay_handler(
        callback: CallbackQuery,
        widget: Button,
        manager: DialogManager,
    ):
    db = manager.middleware_data['db']
    data = manager.dialog_data

    await manager.switch_to(OrderSG.payment)

