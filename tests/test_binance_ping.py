from src.exchange.binance_rest_client import (
    BinanceRestClient,
)


def test_binance_ping():

    client = (
        BinanceRestClient()
    )

    response = (
        client.ping()
    )

    assert (
        response.status_code
        ==
        200
    )
