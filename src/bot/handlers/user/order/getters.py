from aiogram.types import User
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import ManagedCounter

from db.database import Database

from .. import constants as cnst
from services.order import OrderService
from services.payment import PaymentService


async def order_common_getter(dialog_manager: DialogManager, db: Database, **kwargs):
    user_id = dialog_manager.event.from_user.id
    orders = await OrderService(db).create_order_and_clear_cart(user_id)
    dialog_manager.dialog_data['current_order_id'] = orders[0][0]['order_id']
    return {'orders': orders[0], 'total_amount': orders[1]}


async def order_payment_getter(dialog_manager: DialogManager, db: Database, **kwargs):
    some = PaymentService(db).
    return {}
