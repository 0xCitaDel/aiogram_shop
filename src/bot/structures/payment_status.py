from enum import IntEnum

class PayStatus(IntEnum):

    PENDING = 0
    COMPLETED = 1
    FAILED = 2
    REFUNDED = 3

    @property
    def display_name(self):
        status_names = {
            PayStatus.PENDING: "Ожидает оплаты",
            PayStatus.COMPLETED: "Завершен",
            PayStatus.FAILED: "Неудачный",
            PayStatus.REFUNDED: "Возвращен",
        }
        return status_names.get(self, "Неизвестный статус")
