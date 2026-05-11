from src.exchange.binance_rest_client import (
    BinanceRestClient,
)


def test_adjusted_timestamp():

    client = (
        BinanceRestClient()
    )

    client.synchronize_time()

    timestamp = (
        client.adjusted_timestamp()
    )

    assert isinstance(
        timestamp,
        int,
    )

    assert (
        timestamp
        >
        0
    )
