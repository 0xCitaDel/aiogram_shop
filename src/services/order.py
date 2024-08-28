from db.database import Database

class OrderService:

    def __init__(self, db: Database):
        self.db: Database = db

    async def _get_order_data(self, order_id):
        order_data = await self.db.order_item.get_by_order_id(order_id)
        return [{'order_id': o[0],
                 'quantity': o[1],
                 'price': o[2],
                 'title': o[3]} for o in order_data.all()]

    async def create_order_and_clear_cart(self, user_id: int):
        total_amount = await self.db.cart.get_total_amount(user_id)
        new_order_id = await self.db.order_detail.add_one({
            'user_id': user_id, 
            'total_amount': total_amount,
            'shipping_address': 'some'
        })

        await self._create_order_items(user_id, new_order_id)
        order_items = await self._get_order_data(new_order_id)

        await self.db.cart.delete_by_user(user_id)
        await self.db.session.commit()

        return order_items, total_amount, new_order_id

    async def _create_order_items(self, user_id, new_order_id):
        order_items = await self._prepare_order_items(user_id, new_order_id)
        await self.db.order_item.add(order_items)
        return order_items

    async def _prepare_order_items(self, user_id: int, order_id):
        res = await self.db.cart.get_by_user(user_id)
        collection = []
        for row in res:
            collection.append({
                'order_id': order_id,
                'product_id': row.product_id,
                'quantity': row.quantity,
                'price': row.price,
                'total_price': row.quantity * row.price
            })
        return collection






