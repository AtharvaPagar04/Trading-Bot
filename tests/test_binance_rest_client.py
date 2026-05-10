from src.exchange.binance_rest_client import (
    BinanceRestClient,
)


def test_rest_client_initializes():

    client = (
        BinanceRestClient()
    )

    assert (
        client.base_url
        ==
        "https://testnet.binance.vision"
    )

    assert (
        client.session
        is not None
    )
