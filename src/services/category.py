from typing import Optional
from db.database import Database

async def get_categories(db: Database, parent_category: Optional[int]):
    categories = await db.category.get_by_parent_category(parent_category)
    categories_info = [(category.title, category.id, category.parent_id) for category in categories]
    return categories_info

async def parent_exist(db: Database, parent_category: Optional[int]):
    categories = await db.category.get_by_parent_category(parent_category)
    return categories.first()

async def get_products(db: Database, product_category: Optional[int]):
    products = await db.product.get_product_by_category(product_category)
    products_info = [(p.id, p.title, p.price, p.photo_id) for p in products]
    return products_info

async def get_products_from_cart(db: Database, user_id: int):
    products = await db.cart.get_products(user_id)
    products_info = [(p.id, p.title, p.price, p.quanity, p.photo_id) for p in products]
    return products_info

async def check_and_add_to_cart(db: Database, user_id: int, product_id: int, quanity: int, price: int):
    await db.cart.add_product_in_cart(user_id, product_id, quanity, price)
    return product_id

