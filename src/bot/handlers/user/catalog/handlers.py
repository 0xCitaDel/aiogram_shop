from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Select

from bot.states import CatalogSG, ProductSG
from services.category import get_products, parent_exist


async def category_handler(
        callback: CallbackQuery,
        widget: Select,
        manager: DialogManager,
        item_id
    ):
    db = manager.middleware_data['db']
    data = manager.dialog_data

    manager.dialog_data['category_id'] = category_id = int(item_id)

    if await parent_exist(db, int( item_id)):
        await manager.switch_to(CatalogSG.start)
    else:
        await manager.start(
            ProductSG.start,
            data={'all_products': await get_products(db, category_id)}
        )
