from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

from bot import states as st

from . import handlers


main_window = Window(
        Const('Добро пожаловать в магазин продовольственных продуктов'),
        Button(
            Const('Витрина'), id='b_catalog',
            on_click = handlers.select_catalog
        ),
        state=st.MainSG.start
    )


main_dialog = Dialog(main_window)
