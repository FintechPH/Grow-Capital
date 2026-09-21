
class GoldService:

    def __init__(self, provider, config):
        self.provider = provider
        self.config = config

    def get_price(self):
        return self.provider.get_gold_price()

    def buy(self, amount):

        if not self.config["gold"]["buy_enabled"]:
            raise Exception("Gold buying is disabled in this country.")

        return self.provider.buy_gold(amount)

    def sell(self, grams):

        if not self.config["gold"]["sell_enabled"]:
            raise Exception("Gold selling is disabled in this country.")

        return self.provider.sell_gold(grams)
