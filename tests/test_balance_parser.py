from src.exchange.binance_balance_parser import (
    parse_balances,
)


def test_parse_balances():

    payload = {
        "balances": [
            {
                "asset": "BTC",
                "free": "0.5",
                "locked": "0.1",
            },
            {
                "asset": "USDT",
                "free": "1000",
                "locked": "0",
            },
        ]
    }

    balances = (
        parse_balances(
            payload
        )
    )

    assert (
        balances["BTC"]["total"]
        ==
        0.6
    )

    assert (
        balances["USDT"]["free"]
        ==
        1000.0
    )
