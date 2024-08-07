from aiogram.fsm.state import StatesGroup, State

class OrderSG(StatesGroup):
    start = State()
    payment = State()

class ProductSG(StatesGroup):
    start = State()
    cart = State()

class CatalogSG(StatesGroup):
    start = State()

class MainSG(StatesGroup):
    start = State()
