from src.exchange.binance_rest_client import (
    BinanceRestClient,
)


def test_authenticated_get_exists():

    client = (
        BinanceRestClient()
    )

    assert callable(
        client.authenticated_get
    )
