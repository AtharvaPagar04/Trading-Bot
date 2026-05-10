from src.exchange.binance_rest_client import (
    BinanceRestClient,
)


def test_credentials_not_configured():

    client = (
        BinanceRestClient()
    )

    assert (
        client.credentials_configured()
        is False
    )
