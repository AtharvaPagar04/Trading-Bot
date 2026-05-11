from src.exchange.binance_balance_parser import (
    parse_balances,
)


def test_empty_balance_payload():

    balances = (
        parse_balances(
            {}
        )
    )

    assert (
        balances
        ==
        {}
    )
