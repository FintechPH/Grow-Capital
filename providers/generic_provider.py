
class GenericGoldProvider:

    def __init__(self, config):
        self.config = config

    def get_gold_price(self):
        return {
            "provider": "Generic",
            "country": self.config["country"]["name"],
            "currency": self.config["country"]["currency"],
            "price": 0,
            "message": "Connect a supported gold provider API."
        }

    def buy_gold(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        return {
            "provider": "Generic",
            "amount": amount,
            "currency": self.config["country"]["currency"],
            "status": "pending"
        }

    def sell_gold(self, grams):
        if grams <= 0:
            raise ValueError("Gold quantity must be greater than zero.")

        return {
            "provider": "Generic",
            "grams": grams,
            "status": "pending"
        }
