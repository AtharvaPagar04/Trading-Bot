from src.exchange.binance_balance_parser import (
    parse_balances,
)


def test_zero_balances_removed():

    payload = {
        "balances": [
            {
                "asset": "BTC",
                "free": "0",
                "locked": "0",
            },
            {
                "asset": "USDT",
                "free": "100",
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
        "BTC"
        not in balances
    )

    assert (
        "USDT"
        in balances
    )
