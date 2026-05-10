from src.exchange.binance_rest_client import (
    BinanceRestClient,
)


def test_account_info_method_exists():

    client = (
        BinanceRestClient()
    )

    assert callable(
        client.account_info
    )
