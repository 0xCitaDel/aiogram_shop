from collections.abc import Sequence
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot import states as st
from bot.structures.payment_status import PayStatus
from db.models.order import Order
from db.database import Database
from services.order import OrderService
from services.payment import PaymentService

async def all_orders(
        callback: CallbackQuery,
        widget: Button,
        manager: DialogManager
    ):
    db: Database = manager.middleware_data['db']
    user_id = manager.event.from_user.id 
    all_orders: Sequence[Order] = await db.order_detail.get_user_orders(user_id)
    orders = (
        {
            'id': order.id,
            'total_amount': order.total_amount,
            'order_status_id': order.order_status_id.display_name,
            'payment_status_id': order.payment_status_id.display_name,
            'shipping_address': order.shipping_address,
            'created_at': order.created_at
        }
        for order in all_orders
    )
    await manager.start(
        st.OrderSG.all_orders,
        data = {'orders': orders}
    )

async def make_order(
        callback: CallbackQuery,
        widget: Button,
        manager: DialogManager
    ):
    db = manager.middleware_data['db']
    user_id = manager.event.from_user.id 
    orders = await OrderService(db).create_order_and_clear_cart(user_id)
    await manager.start(st.OrderSG.start, data={
        'orders': orders,
        'order_id': orders[0][0]['order_id'],
        'order_id': orders[2]
    })

async def pay_handler(
        callback: CallbackQuery,
        widget: Button,
        manager: DialogManager,
    ):
    db: Database = manager.middleware_data['db']
    data = manager.dialog_data
    total_amount = manager.start_data['orders'][1]
    invoice = await PaymentService(db).create_invoice(1, total_amount)
    data['invoice'] = invoice
    await db.payment.create_payment(
        order_id=manager.start_data['order_id'],
        payment_uuid=invoice[1],
        amount=total_amount
    )
    await db.session.commit()
    await manager.switch_to(st.OrderSG.payment)

async def check_handler(
        callback: CallbackQuery,
        widget: Button,
        manager: DialogManager,
    ):
    db: Database = manager.middleware_data['db']
    data = manager.dialog_data
    invoice_id = data['invoice'][1]
    status = await PaymentService(db).check_payment(invoice_id)
    if not status:
        await manager.switch_to(st.OrderSG.payment)
    else:
        await db.payment.update_payment_status(invoice_id, PayStatus.COMPLETED)
        await db.session.commit()
        await manager.switch_to(st.OrderSG.success)

async def go_menu(
        callback: CallbackQuery,
        widget: Button,
        manager: DialogManager,
    ):
        await manager.start(st.MainSG.start)

