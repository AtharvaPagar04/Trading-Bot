from src.exchange.binance_rest_client import (
    BinanceRestClient,
)


def test_listen_key_method_exists():

    client = (
        BinanceRestClient()
    )

    assert callable(
        client.create_listen_key
    )
