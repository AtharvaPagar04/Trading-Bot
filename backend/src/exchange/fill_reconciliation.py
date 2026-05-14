from src.execution.order_deduplicator import (
    OrderDeduplicator,
)


order_deduplicator = (
    OrderDeduplicator()
)


def reconcile_fill_event(
    event: dict,
):

    order_id = (
        event.get("order_id")
    )

    if (
        order_id
        is not None
    ):

        if (
            order_deduplicator
            .is_duplicate(order_id)
        ):

            return None

    return {
        "symbol":
        event.get(
            "symbol"
        ),

        "status":
        event.get(
            "order_status"
        ),

        "execution_type":
        event.get(
            "execution_type"
        ),
    }