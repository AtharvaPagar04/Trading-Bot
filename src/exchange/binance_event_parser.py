def parse_user_event(
    payload: dict,
):

    return {
        "event_type":
        payload.get(
            "e"
        ),

        "event_time":
        payload.get(
            "E"
        ),

        "symbol":
        payload.get(
            "s"
        ),

        "order_status":
        payload.get(
            "X"
        ),

        "execution_type":
        payload.get(
            "x"
        ),
    }
