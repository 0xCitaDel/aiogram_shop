from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot.states import CatalogSG


async def select_catalog(
        callback: CallbackQuery,
        widget: Button,
        manager: DialogManager
    ):
    await manager.start(CatalogSG.start)
