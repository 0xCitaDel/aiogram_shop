import json
import hashlib
import base64
from typing import Any

from aiohttp import ClientSession

from db.database import Database
from config import settings


class PaymentService:
    def __init__(self, db: Database):
        self.db: Database = db
        self.merchant = CryptomusService(db)

    async def create_invoice(self, user_id, amount):
        return await self.merchant.create_invoice(user_id, amount)


class CryptomusService:

    def __init__(self, db: Database):
        self.db: Database = db
        self.API_KEY = settings.pay.API_KEY
        self.MERCHANT_UUID = settings.pay.MERCHANT_UUID

    def _generate_headers(self, data: str) -> dict[str, Any]:
        sign = hashlib.md5(
            base64.b64encode(data.encode('ascii')) + self.MERCHANT_UUID.encode('ascii')
        ).hexdigest()

        return {
            'merchant': self.MERCHANT_UUID,
            'sign': sign,
            'content-type': 'application/json'
        }

    async def create_invoice(self, user_id, amount: str):
        async with ClientSession() as session:
            json_dumps = json.dumps({
                'amount': amount,
                'currency': 'USDT',
                'order_id': f'HERE-MUST-BE-{user_id}-ORDER-ID',
                'network': 'tron',
                'lifetime': 1800
            })
            
            response = await session.post(
                'https://api.cryptomus.com/v1/payment',
                data=json_dumps,
                headers=self._generate_headers(json_dumps)
            )
            return await response.json()



