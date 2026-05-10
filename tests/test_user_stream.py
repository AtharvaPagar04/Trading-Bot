from src.exchange.binance_user_stream import (
    BinanceUserStream,
)


def test_stream_url():

    stream = (
        BinanceUserStream(
            "abc123"
        )
    )

    assert (
        stream.stream_url()
        ==
        "wss://stream.binance.com:9443/ws/abc123"
    )
