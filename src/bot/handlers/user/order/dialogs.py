from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const, Format, Jinja

from bot import states as st

from . import getters
from . import handlers


order_dialog = Dialog(
    Window(
        Jinja(
            'Products:\n\n'
            '{% for o in orders %}'
            '{{ o.title}}\n' 
            '{{ o.quanity }} piece x {{ o.price }} = {{ o.quanity * o.price }}\n\n'
            '{% endfor %}'
            'Total amount: {{ total_amount }}$\n\n'
        ),
        Button(
            Const('Pay order'),
            id='order_pay',
            on_click=handlers.pay_handler
        ),
        state=st.OrderSG.start,
        getter=getters.order_common_getter
    ),
    Window(
        Format('Payment here'),
        Button(
            Const('Go pay suite'),
            id='payment'
        ),
        state=st.OrderSG.payment,
        getter=getters.order_payment_getter
    )
)
