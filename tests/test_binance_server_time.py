from src.exchange.binance_rest_client import (
    BinanceRestClient,
)


def test_binance_server_time():

    client = (
        BinanceRestClient()
    )

    response = (
        client.server_time()
    )

    assert (
        response.status_code
        ==
        200
    )

    data = response.json()

    assert (
        "serverTime"
        in data
    )
