from src.exchange.order_reconciliation import (
    reconcile_open_orders,
)


class MockResponse:

    def json(
        self,
    ):

        return [
            {
                "symbol": "BTCUSDT",
                "orderId": 1,
                "side": "BUY",
                "status": "NEW",
                "price": "100000",
                "origQty": "0.1",
                "executedQty": "0",
            }
        ]


class MockRestClient:

    def open_orders(
        self,
        symbol=None,
    ):

        return MockResponse()


def test_order_reconciliation():

    orders = (
        reconcile_open_orders(
            MockRestClient()
        )
    )

    assert (
        len(orders)
        ==
        1
    )

    assert (
        orders[0]["symbol"]
        ==
        "BTCUSDT"
    )
