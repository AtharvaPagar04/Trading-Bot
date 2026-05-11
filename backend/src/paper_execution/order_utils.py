from src.paper_execution.paper_order import (
    PaperOrder,
)


def remaining_quantity(
    order: PaperOrder,
) -> float:

    return (
        order.quantity
        -
        order.filled_quantity
    )