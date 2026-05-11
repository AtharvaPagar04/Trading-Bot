from src.exchange.binance_order_parser import (
    parse_open_orders,
)


def test_parse_open_orders():

    payload = [
        {
            "symbol": "BTCUSDT",
            "orderId": 123,
            "side": "BUY",
            "status": "PARTIALLY_FILLED",
            "price": "100000",
            "origQty": "0.5",
            "executedQty": "0.2",
        }
    ]

    orders = (
        parse_open_orders(
            payload
        )
    )

    order = orders[0]

    assert (
        order["symbol"]
        ==
        "BTCUSDT"
    )

    assert (
        order["price"]
        ==
        100000.0
    )

    assert (
        order["executed_quantity"]
        ==
        0.2
    )
