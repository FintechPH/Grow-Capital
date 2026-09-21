
import os
import requests


class AugmontProvider:

    def __init__(self, config):
        self.config = config

        self.base_url = os.getenv(
            "AUGMONT_BASE_URL",
            "https://your-augmont-api-url.com"
        )

        self.api_key = os.getenv("AUGMONT_API_KEY")

    def get_gold_price(self):

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        response = requests.get(
            f"{self.base_url}/gold/price",
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    def buy_gold(self, amount):

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "amount": amount,
            "currency": self.config["country"]["currency"]
        }

        response = requests.post(
            f"{self.base_url}/gold/buy",
            json=data,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    def sell_gold(self, grams):

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "grams": grams,
            "currency": self.config["country"]["currency"]
        }

        response = requests.post(
            f"{self.base_url}/gold/sell",
            json=data,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        return response.json()
