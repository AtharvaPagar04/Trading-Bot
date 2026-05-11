from src.exchange.binance_event_parser import (
    parse_user_event,
)


def test_parse_user_event():

    payload = {
        "e": "executionReport",
        "E": 123456,
        "s": "BTCUSDT",
        "X": "FILLED",
        "x": "TRADE",
    }

    event = (
        parse_user_event(
            payload
        )
    )

    assert (
        event["event_type"]
        ==
        "executionReport"
    )

    assert (
        event["symbol"]
        ==
        "BTCUSDT"
    )

    assert (
        event["order_status"]
        ==
        "FILLED"
    )
