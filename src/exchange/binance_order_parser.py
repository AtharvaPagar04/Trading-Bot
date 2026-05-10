def parse_open_orders(
    payload: list,
):

    orders = []

    for order in payload:

        parsed = {
            "symbol":
            order.get(
                "symbol"
            ),

            "order_id":
            order.get(
                "orderId"
            ),

            "side":
            order.get(
                "side"
            ),

            "status":
            order.get(
                "status"
            ),

            "price":
            float(
                order.get(
                    "price",
                    0,
                )
            ),

            "original_quantity":
            float(
                order.get(
                    "origQty",
                    0,
                )
            ),

            "executed_quantity":
            float(
                order.get(
                    "executedQty",
                    0,
                )
            ),
        }

        orders.append(
            parsed
        )

    return orders
