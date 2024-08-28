from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Select
from aiogram_dialog.widgets.text import Const, Format

from bot import states as st
from bot.handlers.common_handlers import close_dialog

from . import getters
from . import handlers


catalog_window = Window(
    Const('Выберите категорию'),
    Select(
        Format('{item[0]}'), id='category',
        item_id_getter=lambda x: x[1], items='category_items',
        on_click=handlers.category_handler
    ),
    Button(
        Const('☰ Mеню'),
        id="b_menu",
        on_click=close_dialog
    ),
    getter = getters.categories_getter,
    preview_data = getters.categories_getter,
    state=st.CatalogSG.start
)


catalog_dialog = Dialog(catalog_window)
