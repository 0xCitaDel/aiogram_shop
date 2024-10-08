from typing import Optional

from aiogram import Dispatcher
from aiogram.fsm.storage.base import BaseEventIsolation, BaseStorage
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.strategy import FSMStrategy

from aiogram_dialog import setup_dialogs
from yookassa.domain.common.user_agent import yookassa
from bot.middlewares.database import DatabaseMiddleware
from bot.middlewares.check_access import CheckAccessMiddleware

from bot.handlers import routers

from config import settings

def get_dispatcher(
    storage: BaseStorage = MemoryStorage(),
    fsm_strategy: Optional[FSMStrategy] = FSMStrategy.CHAT,
    event_isolation: Optional[BaseEventIsolation] = None,
):
    """This function set up dispatcher with routers, filters and middlewares"""
    yookassa.Configuration.account_id =settings.pay.ACCOUNT_ID
    yookassa.Configuration.secret_key = settings.pay.API_KEY

    dp = Dispatcher(
        storage=storage
    )

    dp.update.outer_middleware(DatabaseMiddleware())
    dp.update.outer_middleware(CheckAccessMiddleware())

    setup_dialogs(dp)

    for router in routers:
        dp.include_router(router)

    return dp
