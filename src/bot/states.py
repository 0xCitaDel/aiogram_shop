from aiogram.fsm.state import StatesGroup, State

class MainSG(StatesGroup):
    start = State()

class AdminSG(StatesGroup):
    start = State() 

class AdminAddProductSG(StatesGroup):
    title = State() 
    description = State() 
    price = State() 
    image = State()
    

class OrderSG(StatesGroup):
    start = State()
    payment = State()
    all_orders = State()
    success = State()

class ProductSG(StatesGroup):
    start = State()

class CatalogSG(StatesGroup):
    start = State()

class CartSG(StatesGroup):
    start = State()
