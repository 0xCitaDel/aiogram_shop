from aiogram.types import CallbackQuery, Message

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button

from bot import states as st
from db.database import Database


async def select_admin_panel(
        callback: CallbackQuery,
        widget: Button,
        manager: DialogManager
    ):
    await manager.start(st.AdminSG.start)

async def select_admin_add_product(
        callback: CallbackQuery,
        widget: Button,
        manager: DialogManager
    ):
    await manager.start(st.AdminAddProductSG.title)


async def message_title(
    message: Message,
    widget: MessageInput,
    dialog_manager: DialogManager
) -> None:
    dialog_manager.dialog_data['title'] = message.text
    await dialog_manager.switch_to(st.AdminAddProductSG.description)

async def message_description(
    message: Message,
    widget: MessageInput,
    dialog_manager: DialogManager
) -> None:
    dialog_manager.dialog_data['description'] = message.text
    await dialog_manager.switch_to(st.AdminAddProductSG.price)


async def message_price(
    message: Message,
    widget: MessageInput,
    dialog_manager: DialogManager
) -> None:
    dialog_manager.dialog_data['price'] = message.text
    await dialog_manager.switch_to(st.AdminAddProductSG.image)

async def message_image(
    message: Message,
    widget: MessageInput,
    dialog_manager: DialogManager
) -> None:
    dialog_manager.dialog_data['image'] = message.photo[-1].file_id
    db: Database = dialog_manager.middleware_data['db']
    await db.product.add_product_by_category(
        category_id=1,
        title=dialog_manager.dialog_data['title'],
        description=dialog_manager.dialog_data['description'],
        price=dialog_manager.dialog_data['price'],
        photo_id=dialog_manager.dialog_data['image']
    )
    await dialog_manager.start(st.AdminSG.start)
