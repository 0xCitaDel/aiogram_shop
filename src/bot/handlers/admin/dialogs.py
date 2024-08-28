from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

from bot import states as st

# from . import handlers


user_main_window = Window(
        Const('Добро пожаловать в магазин Admin продовольственных продуктов'),
        Button(
            Const('Витрина'), id='b_catalog'
        ),
        Button(
            Const('Admin panel'), id='b_catalog'
        ),
        state=st.MainSG.start
    )
