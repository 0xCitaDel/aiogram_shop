from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Url
from aiogram_dialog.widgets.text import Const, Format, Jinja

from bot import states as st
from bot.handlers.common_handlers import close_dialog

from . import getters
from . import handlers


order_dialog = Dialog(
    Window(
        Jinja(
            'Товары:\n\n'
            '{% for o in orders %}'
            '{{ o.title}}\n' 
            '{{ o.price }} x {{ o.quantity }} шт. = {{ o.quantity * o.price }} ₽\n\n'
            '{% endfor %}'
            'Итоговая сумма: {{ total_amount }} ₽\n\n'
        ),
        Button(
            Const('Перейти к оплате'),
            id='order_pay',
            on_click=handlers.pay_handler
        ),
        Button(
            Const('Меню'),
            id='order_pay_exit',
            on_click=handlers.go_menu
        ),
        state=st.OrderSG.start,
        getter=getters.order_common_getter
    ),
    Window(
        Jinja(
            'Все заказы:\n\n'
            '{% for o in orders %}'
            '#{{ o.id }} {{ o.total_amount }} ₽: Статус оплаты: {{ o.payment_status_id }}\n\n'
            '{% endfor %}'
        ),
        state=st.OrderSG.all_orders,
        getter=getters.all_orders
    ),
    Window(
        Format('После оплаты, нажмите на "Проверить оплату"'),
        Url(
            text=Format('Оплатить {total_amount} ₽'),
            url=Format('{payment_url}'),
            id='b_payment_url'
        ),
        Button(
            Const('Проверить оплату'),
            id='payment',
            on_click=handlers.check_handler
        ),
        state=st.OrderSG.payment,
        getter=getters.order_payment_getter
    ),
    Window(
        Format('Ваш заказ успешно оплачен, наш оператор свяжется с вами'),
        Button(
            Const('Главное меню'),
            id='success',
            on_click=handlers.go_menu
        ),
        state=st.OrderSG.success,
    )
)
