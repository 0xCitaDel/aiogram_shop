from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import (
    Button,
    CurrentPage,
    NextPage,
    PrevPage,
    Row,
    StubScroll
)
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Format

from aiogram_dialog_custom.counter import CustomCounter
from bot import states as st

from . import getters
from . import handlers
from .. import constants as cnst

 
product_window = Window(
    DynamicMedia('photo'),
    Format('[{current_page} | {pages}]'),
    Format('{product[1]}'),
    Format('Price: {product[2]}'),
    CustomCounter(
        id=cnst.ID_COUNTER,
        default=5,
        min_value=cnst.PRODUCT_COUNTER_MIN_VALUE,
        max_value=cnst.PRODUCT_COUNTER_MAX_VALUE,
        text=Format("{value} piece"),
        cycle=True
    ),
    StubScroll(id=cnst.ID_STUB_SCROLL_PRODUCT, pages="pages"),
    Button(
        Format('Add cart'),
        id='b_add_cart',
        on_click=handlers.add_cart
    ),
    Row(
        PrevPage(scroll=cnst.ID_STUB_SCROLL_PRODUCT, text=Format('⬅️')),
        CurrentPage(scroll=cnst.ID_STUB_SCROLL_PRODUCT, text=Format('{current_page1} / {pages}')),
        NextPage(scroll=cnst.ID_STUB_SCROLL_PRODUCT, text=Format('➡️')),
    ),
    Button(
        Format('Go to cart'),
        id='b_go_cart',
        on_click=handlers.go_cart
    ),
    state=st.ProductSG.start,
    getter=getters.paging_product_getter,
    preview_data=getters.paging_product_getter
)

 
cart_window = Window(
    DynamicMedia('photo'),
    Format("[{current_page} | {pages}]"),
    Format('{product[1]}'),
    Format('Price: {product[2]}'),
    Format('Quanity: {product[3]}'),
    StubScroll(id=cnst.ID_STUB_SCROLL_CART, pages="pages"),
    Row(
        PrevPage(scroll=cnst.ID_STUB_SCROLL_CART),
        NextPage(scroll=cnst.ID_STUB_SCROLL_CART),
    ),
    Button(
        Format('Оформить'),
        id='order',
        on_click=handlers.make_order
    ),
    getter=getters.paging_cart_getter,
    preview_data=getters.paging_cart_getter,
    state=st.ProductSG.cart
)


product_dialog = Dialog(product_window, cart_window)
