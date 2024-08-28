from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import (
    Button,
    Counter,
    CurrentPage,
    NextPage,
    PrevPage,
    Row,
    StubScroll
)
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Format

from bot import states as st
from bot.handlers.user.handlers import select_catalog

from . import getters
from . import handlers
from .. import constants as cnst
from bot.handlers.user.order.handlers import make_order

cart_window = Window(
    DynamicMedia('photo'),
    Format("[{current_page} | {pages}]"),
    Format('{product[1]}'),
    Format('Price: {product[2]}'),
    Format('Quantity: {product[3]}'),
    StubScroll(id=cnst.ID_STUB_SCROLL_CART, pages="pages"),
    Row(
        PrevPage(scroll=cnst.ID_STUB_SCROLL_CART),
        NextPage(scroll=cnst.ID_STUB_SCROLL_CART),
    ),
    Button(
        Format('Оформить'),
        id='b_order',
        on_click=make_order
    ),
    Button(
        Format('Назад'),
        id='b_go_back',
        on_click=select_catalog
    ),
    getter=getters.paging_cart_getter,
    preview_data=getters.paging_cart_getter,
    state=st.CartSG.start
)

cart_dialog = Dialog(cart_window)
