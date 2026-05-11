from enum import Enum


class OrderStatus(
    str,
    Enum,
):

    PENDING = "PENDING"

    FILLED = "FILLED"

    PARTIALLY_FILLED = (
        "PARTIALLY_FILLED"
    )

    CANCELLED = "CANCELLED"

    REJECTED = "REJECTED"