from enum import IntEnum

class OrderStatus(IntEnum):

    NEW = 1
    PROCESSING = 2
    SHIPPED = 3
    DELIVERED = 4
    CANCELED = 5
    RETURNED = 6 

    @property
    def display_name(self):
        status_names = {
            OrderStatus.NEW: "Новый",
            OrderStatus.PROCESSING: "В обработке",
            OrderStatus.SHIPPED: "Отправлен",
            OrderStatus.DELIVERED: "Доставлен",
            OrderStatus.CANCELED: "Отменен",
            OrderStatus.RETURNED: "Возвращен"
        }
        return status_names.get(self, "Неизвестный статус")

