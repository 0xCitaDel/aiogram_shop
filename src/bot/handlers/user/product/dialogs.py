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

 
product_window = Window(
    DynamicMedia('photo'),
    Format('[{current_page} | {pages}]'),
    Format('{product[1]}'),
    Format('Price: {product[2]}'),
    StubScroll(id=cnst.ID_STUB_SCROLL_PRODUCT, pages="pages"),
    Counter(
        id=cnst.ID_COUNTER,
        default=1,
        min_value=cnst.PRODUCT_COUNTER_MIN_VALUE,
        max_value=cnst.PRODUCT_COUNTER_MAX_VALUE,
        text=Format("{value} шт."),
        cycle=True
    ),
    Row(
        Button(
            Format('В корзину [{card_items} шт.]'),
            id='b_add_cart',
            on_click=handlers.add_cart
        ),
        Button(
            Format('Перейти к корзине'),
            id='b_go_cart',
            on_click=handlers.go_cart,
            when='card_items'
        ),
    ),
    Row(
        PrevPage(scroll=cnst.ID_STUB_SCROLL_PRODUCT, text=Format('⬅️')),
        CurrentPage(scroll=cnst.ID_STUB_SCROLL_PRODUCT, text=Format('{current_page1} / {pages}')),
        NextPage(scroll=cnst.ID_STUB_SCROLL_PRODUCT, text=Format('➡️')),
    ),
    Button(
        Format('Назад'),
        id='b_go_back',
        on_click=select_catalog
    ),

    state=st.ProductSG.start,
    getter=getters.paging_product_getter,
    preview_data=getters.paging_product_getter
)

product_dialog = Dialog(product_window)
