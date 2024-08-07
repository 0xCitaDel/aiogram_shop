from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode
from bot.handlers.user import (
    main_dialog,
    catalog_dialog,
    product_dialog,
    order_dialog
)
from bot.states import MainSG


router = Router()

router.include_router(main_dialog)
router.include_router(catalog_dialog)
router.include_router(product_dialog)
router.include_router(order_dialog)


@router.message(CommandStart())
async def start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MainSG.start, mode=StartMode.RESET_STACK)

@router.message(F.photo)
async def get_file_id(message: Message, dialog_manager: DialogManager):
    photo_data = message.photo[-1].file_id
    await message.answer(f'{photo_data}')
