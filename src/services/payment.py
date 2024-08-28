import json
import hashlib
import base64
from typing import Any

from aiohttp import ClientSession
import asyncio
import yookassa
from yookassa import Payment, Configuration
import uuid

from db.database import Database
from config import settings


Configuration.account_id = settings.pay.ACCOUNT_ID
Configuration.secret_key = settings.pay.API_KEY


class PaymentService:
    def __init__(self, db: Database):
        self.db: Database = db

    async def create_invoice(self, user_id, amount):
        idempotence_key = str(uuid.uuid4())
        payment = Payment.create({
            "amount": {
              "value": amount,
              "currency": "RUB"
            },
            "payment_method_data": {
              "type": "bank_card"
            },
            "confirmation": {
              "type": "redirect",
              "return_url": "https:/t.me/awaitly_bot"
            },
            "description": "Заказ №72"
        }, idempotence_key)

        payment_data = json.loads(payment.json())
        payment_id = payment_data['id']
        payment_url = (payment_data['confirmation'])['confirmation_url']

        return payment_url, payment_id


    async def check_payment(self, payment_id):
        payment = json.loads((Payment.find_one(payment_id)).json())

        from pprint import pprint
        if payment['paid']==True:
            print("SUCCSESS RETURN")
            pprint(payment)
            return True
        else:
            print("BAD RETURN")
            pprint(payment)
            return False

# class CryptomusService:
#
#     def __init__(self, db: Database):
#         self.db: Database = db
#         self.API_KEY = settings.pay.API_KEY
#         self.MERCHANT_UUID = settings.pay.MERCHANT_UUID
#
#     def _generate_headers(self, data: str) -> dict[str, Any]:
#         sign = hashlib.md5(
#             base64.b64encode(data.encode('ascii')) + self.MERCHANT_UUID.encode('ascii')
#         ).hexdigest()
#
#         return {
#             'merchant': self.MERCHANT_UUID,
#             'sign': sign,
#             'content-type': 'application/json'
#         }
#
#     async def create_invoice(self, user_id, amount: str):
#         async with ClientSession() as session:
#             json_dumps = json.dumps({
#                 'amount': amount,
#                 'currency': 'USDT',
#                 'order_id': f'HERE-MUST-BE-{user_id}-ORDER-ID',
#                 'network': 'tron',
#                 'lifetime': 1800
#             })
#            
#             response = await session.post(
#                 'https://api.cryptomus.com/v1/payment',
#                 data=json_dumps,
#                 headers=self._generate_headers(json_dumps)
#             )
#             return await response.json()
#
#
#
