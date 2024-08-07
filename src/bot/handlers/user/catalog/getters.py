from aiogram_dialog import DialogManager

from db.database import Database
from services.category import get_categories

async def categories_getter(dialog_manager: DialogManager, db: Database, **kwargs):
    category_id = dialog_manager.dialog_data.get('category_id')
    category_info = await get_categories(db, parent_category=category_id)
    return {'category_items': category_info}
