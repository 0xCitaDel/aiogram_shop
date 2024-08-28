from aiogram.types import User
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import ManagedCounter

from db.database import Database

from .. import constants as cnst
from services.order import OrderService
from services.payment import PaymentService

async def all_orders(dialog_manager: DialogManager, db: Database, **kwargs):
    return {'orders': dialog_manager.start_data['orders']}

async def order_common_getter(dialog_manager: DialogManager, db: Database, **kwargs):
    user_id = dialog_manager.event.from_user.id
    orders = dialog_manager.start_data['orders']
    return {'orders': orders[0], 'total_amount': orders[1]}


async def order_payment_getter(dialog_manager: DialogManager, bot, db: Database, **kwargs):
    return {'payment_url': dialog_manager.dialog_data['invoice'][0],
            'total_amount': dialog_manager.start_data['orders'][1]
            }
