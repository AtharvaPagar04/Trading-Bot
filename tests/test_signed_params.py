from src.exchange.binance_rest_client import (
    BinanceRestClient,
)


def test_signed_params():

    client = (
        BinanceRestClient()
    )

    client.synchronize_time()

    params = (
        client.signed_params(
            {
                "symbol": "BTCUSDT",
            }
        )
    )

    assert (
        "timestamp"
        in params
    )

    assert (
        "signature"
        in params
    )
