
class OrderService:

    def create_order(self, user_id, amount, currency):

        if not user_id:
            raise ValueError("User ID is required.")

        if amount <= 0:
            raise ValueError("Order amount must be greater than zero.")

        if not currency:
            raise ValueError("Currency is required.")

        return {
            "user_id": user_id,
            "amount": amount,
            "currency": currency,
            "status": "created"
        }

    def get_order(self, order_id):

        if not order_id:
            raise ValueError("Order ID is required.")

        # Database integration will be added later
        return {
            "order_id": order_id,
            "status": "created"
        }

    def cancel_order(self, order_id):

        if not order_id:
            raise ValueError("Order ID is required.")

        return {
            "order_id": order_id,
            "status": "cancelled"
        }
