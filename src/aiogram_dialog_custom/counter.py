from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.api.protocols import DialogProtocol
from aiogram_dialog.widgets.kbd import Counter


class CustomCounter(Counter):

    async def custom_inc_value(self, value: float):
        if value == 1000: value += 1
        if value == 500: value += 500
        elif value == 250: value += 250
        elif value == 100: value += 150
        elif value == 50: value += 50
        elif value == 25: value += 25
        elif value == 10: value += 15
        else: value += 5
        return value
    
    async def custom_dec_value(self, value: float):
        if value == 5: value -= 1
        if value == 10: value -= 5
        if value == 25: value -= 15
        if value == 50: value -= 25
        if value == 100: value -= 50
        if value == 250: value -= 150
        if value == 500: value -= 250
        if value == 1000: value -= 500
        return value

    async def _process_item_callback(
            self,
            callback: CallbackQuery,
            data: str,
            dialog: DialogProtocol,
            manager: DialogManager,
    ) -> bool:
        await self.on_click.process_event(
            callback, self.managed(manager), manager,
        )

        value = self.get_value(manager)
        if data == "+":
            value = await self.custom_inc_value(value)
            if value > self.max and self.cycle:
                value = self.min
            await self.set_value(manager, value)
        elif data == "-":
            value = await self.custom_dec_value(value)
            if value < self.min and self.cycle:
                value = self.max
            await self.set_value(manager, value)
        elif data == "":
            await self.on_text_click.process_event(
                callback, self.managed(manager), manager,
            )
        return True
