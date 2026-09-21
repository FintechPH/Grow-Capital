
class PaymentService:

    def create_payment(self, user_id, amount, currency):

        if not user_id:
            raise ValueError("User ID is required.")

        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")

        if not currency:
            raise ValueError("Currency is required.")

        return {
            "user_id": user_id,
            "amount": amount,
            "currency": currency,
            "status": "pending"
        }

    def verify_payment(self, payment_id):

        if not payment_id:
            raise ValueError("Payment ID is required.")

        # Payment gateway verification will be added later
        return {
            "payment_id": payment_id,
            "status": "verified"
        }
