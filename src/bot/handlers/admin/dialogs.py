from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

from bot import states as st

from . import handlers


admin_main_window = Window(
        Const('Добро пожаловать Admin Panel'),
        Button(
            Const('Добавить товар'), id='b_catalog_add_product',
            on_click=handlers.select_admin_add_product
        ),
        state=st.AdminSG.start
    )


admin_dialog = Dialog(admin_main_window)

admin_add_product_dialog = Dialog(
    Window(
        Const('Введите название товара'),
        MessageInput(
            func=handlers.message_title,
            content_types=ContentType.ANY,
        ),
        state=st.AdminAddProductSG.title
    ),
    Window(
        Const('Введите описание товара'),
        MessageInput(
            func=handlers.message_description,
            content_types=ContentType.ANY,
        ),
        state=st.AdminAddProductSG.description
    ),
    Window(
        Const('Введите цену товара'),
        MessageInput(
            func=handlers.message_price,
            content_types=ContentType.ANY,
        ),
        state=st.AdminAddProductSG.price
    ),
    Window(
        Const('Пришлите фото товара'),
        MessageInput(
            func=handlers.message_image,
            content_types=ContentType.ANY,
        ),
        state=st.AdminAddProductSG.image
    )
)
