from src.exchange.binance_rest_client import (
    BinanceRestClient,
)


def test_binance_time_sync():

    client = (
        BinanceRestClient()
    )

    offset = (
        client.synchronize_time()
    )

    assert isinstance(
        offset,
        int,
    )
