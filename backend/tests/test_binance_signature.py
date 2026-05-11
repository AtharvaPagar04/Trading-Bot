from src.exchange.binance_rest_client import (
    BinanceRestClient,
)


def test_signature_generation():

    client = (
        BinanceRestClient()
    )

    signature = (
        client.sign_query(
            {
                "symbol": "BTCUSDT",
                "timestamp": 123456789,
            }
        )
    )

    assert isinstance(
        signature,
        str,
    )

    assert (
        len(signature)
        ==
        64
    )
