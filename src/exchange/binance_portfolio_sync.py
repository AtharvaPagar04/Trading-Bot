from src.exchange.binance_balance_parser import (
    parse_balances,
)


def synchronize_portfolio(
    rest_client,
):

    response = (
        rest_client.account_info()
    )

    payload = (
        response.json()
    )

    balances = (
        parse_balances(
            payload
        )
    )

    return balances
