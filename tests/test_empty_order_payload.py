from src.exchange.binance_order_parser import (
    parse_open_orders,
)


def test_empty_order_payload():

    orders = (
        parse_open_orders(
            []
        )
    )

    assert (
        orders
        ==
        []
    )
