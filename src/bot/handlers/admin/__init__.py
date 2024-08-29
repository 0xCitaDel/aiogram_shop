from aiogram import Router
from .dialogs  import admin_dialog, admin_add_product_dialog



admin_router = Router()

admin_router.include_router(admin_dialog)
admin_router.include_router(admin_add_product_dialog)
