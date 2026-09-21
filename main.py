
import yaml

from generic_core.gold import GoldService
from generic_core.wallet import Wallet

from providers.augmont import AugmontProvider


PROVIDERS = {
    "augmont": AugmontProvider
}


def load_country(country_code):

    file_path = f"countries/{country_code}.yaml"

    with open(file_path, "r") as file:
        return yaml.safe_load(file)


def create_application(country_code):

    # Load country configuration
    config = load_country(country_code)

    # Find provider
    provider_name = config["gold"]["provider"]

    provider_class = PROVIDERS.get(provider_name)

    if provider_class is None:
        raise ValueError(
            f"Provider '{provider_name}' is not supported."
        )

    # Create provider
    provider = provider_class(config)

    # Create generic gold service
    gold_service = GoldService(
        provider,
        config
    )

    # Create wallet
    wallet = Wallet()

    return config, gold_service, wallet


def main():

    # Country can later come from user/account/application
    country_code = "india"

    config, gold, wallet = create_application(
        country_code
    )

    print("--------------------------------")
    print("      GROW CAPITAL")
    print("--------------------------------")

    print(
        "Country:",
        config["country"]["name"]
    )

    print(
        "Currency:",
        config["country"]["currency"]
    )

    print(
        "Gold Provider:",
        config["gold"]["provider"]
    )

    print("--------------------------------")

    # Get gold price
    try:

        price = gold.get_price()

        print("Gold Price:")
        print(price)

    except Exception as e:

        print("Unable to get gold price:")
        print(e)

    print("--------------------------------")

    # Wallet example
    print(
        "Gold Balance:",
        wallet.get_balance(),
        "grams"
    )


if __name__ == "__main__":
    main()
