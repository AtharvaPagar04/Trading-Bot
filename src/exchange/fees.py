from src.exchange.fee_models import (
    ExecutionFee,
)


def calculate_execution_fee(
    quantity: float,

    price: float,

    fee_rate: float,
) -> ExecutionFee:

    trade_value = (
        quantity
        * price
    )

    fee_paid = (
        trade_value
        * fee_rate
    )

    return ExecutionFee(
        fee_rate=
        fee_rate,

        fee_paid=
        fee_paid,
    )