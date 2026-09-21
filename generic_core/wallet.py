
class Wallet:

    def __init__(self):
        self.gold_balance = 0.0

    def add_gold(self, grams):

        self.gold_balance += grams

        return self.gold_balance

    def remove_gold(self, grams):

        if grams > self.gold_balance:
            raise ValueError("Insufficient gold balance")

        self.gold_balance -= grams

        return self.gold_balance

    def get_balance(self):

        return self.gold_balance
