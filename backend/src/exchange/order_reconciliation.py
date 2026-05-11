from src.exchange.binance_order_parser import (
    parse_open_orders,
)


def reconcile_open_orders(
    rest_client,
    symbol=None,
):

    response = (
        rest_client.open_orders(
            symbol=symbol,
        )
    )

    payload = (
        response.json()
    )

    orders = (
        parse_open_orders(
            payload
        )
    )

    return orders
