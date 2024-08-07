from typing import Optional
from aiogram.types import ContentType
from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment, MediaId
from aiogram_dialog.widgets.kbd import ManagedCounter

from db.database import Database
from services.category import get_products, get_products_from_cart

from .. import constants as cnst


async def paging_product_getter(dialog_manager: DialogManager, db: Database, **_kwargs):
    current_page = await dialog_manager.find(cnst.ID_STUB_SCROLL_PRODUCT).get_page()
    counter: Optional[ManagedCounter] = dialog_manager.find(cnst.ID_COUNTER)
    products_info = await get_products(db, dialog_manager.start_data['category_id'])


    product_id = dialog_manager.dialog_data['product_id'] = products_info[current_page][0]
    dialog_manager.dialog_data['product_price'] = products_info[current_page][2]
    image_id = products_info[current_page][3]
    image = MediaAttachment(ContentType.PHOTO, file_id=MediaId(image_id))

    return {
        "product": products_info[current_page],
        "photo": image,
        "pages": len(products_info),
        "current_page": current_page + 1,
    }


async def paging_cart_getter(dialog_manager: DialogManager, db: Database, **_kwargs):
    current_page = await dialog_manager.find(cnst.ID_STUB_SCROLL_CART).get_page()
    user_id = dialog_manager.event.from_user.id
    cart_products_info = await get_products_from_cart(db, user_id)
    image_id = cart_products_info[current_page][4]
    image = MediaAttachment(ContentType.PHOTO, file_id=MediaId(image_id))

    dialog_manager.dialog_data['product_id'] = cart_products_info[current_page][0]

    return {
        "product": cart_products_info[current_page],
        "photo": image,
        "pages": len(cart_products_info),
        "current_page": current_page + 1,
    }
