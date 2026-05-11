from src.exchange.binance_rest_client import (
    BinanceRestClient,
)


def test_auth_headers():

    client = (
        BinanceRestClient()
    )

    headers = (
        client.auth_headers()
    )

    assert (
        "X-MBX-APIKEY"
        in headers
    )
