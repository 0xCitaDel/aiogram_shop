from typing import Optional
from aiogram.types import ContentType
from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment, MediaId
from aiogram_dialog.widgets.kbd import ManagedCounter

from db.database import Database
from services.category import get_products, get_products_from_cart

from .. import constants as cnst


async def paging_product_getter(dialog_manager: DialogManager, db: Database, **_kwargs):
    user_id = dialog_manager.event.from_user.id
    current_page = await dialog_manager.find(cnst.ID_STUB_SCROLL_PRODUCT).get_page()
    counter: Optional[ManagedCounter] = dialog_manager.find(cnst.ID_COUNTER)

    all_products = dialog_manager.start_data['all_products']

    product_id = dialog_manager.dialog_data['product_id'] = all_products[current_page][0]
    dialog_manager.dialog_data['product_price'] = all_products[current_page][2]
    image_id = all_products[current_page][3]
    image = MediaAttachment(ContentType.PHOTO, file_id=MediaId(image_id))

    cart_products_info = await get_products_from_cart(db, user_id)
    print('******************************************************************')
    print(cart_products_info)
    print('******************************************************************')


    return {
        "product": all_products[current_page],
        "photo": image,
        "pages": len(all_products),
        "current_page": current_page + 1,
        "card_items": len(cart_products_info)
    }


