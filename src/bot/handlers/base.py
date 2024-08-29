from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import Dialog, DialogManager, StartMode, Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const
from bot.handlers.user import (
    catalog_dialog,
    product_dialog,
    order_dialog
)
from bot.states import MainSG
from bot import states as st
from bot.handlers.user import user_router
from bot.handlers.admin import admin_router
from bot.handlers.user.handlers import select_catalog
from bot.handlers.user.order.handlers import all_orders
from bot.handlers.admin.handlers import select_admin_panel

router = Router()

main_dialog = Dialog(
    Window(
        Const('Добро пожаловать, что будем делать?'),
        Button(
            Const('Каталог'), id='b_catalog',
            on_click=select_catalog
        ),
        Button(
            Const('Мои заказы'),
            id='b_my_orders',
            on_click=all_orders
        ),
        Button(
            Const('Админ панель'), id='b_admin_panel',
            on_click=select_admin_panel,
        ),
        state=st.MainSG.start
    )
)

router.include_router(main_dialog)
router.include_router(user_router)
router.include_router(admin_router)


@router.message(CommandStart())
async def start_admin(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MainSG.start, mode=StartMode.RESET_STACK)


#n @router.message(F.photo)
# async def get_file_id(message: Message, dialog_manager: DialogManager):
#     photo_data = message.photo[-1].file_id
#     await message.answer(f'{photo_data}')
