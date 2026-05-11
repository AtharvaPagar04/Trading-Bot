def reconcile_fill_event(
    event: dict,
):

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
