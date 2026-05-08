from src.exchange.models import (
    OrderSide,
)

from src.exchange.slippage_models import (
    SlippageResult,
)


def apply_slippage(
    price: float,

    slippage_percent: float,

    side: OrderSide,
) -> SlippageResult:

    slipped_price = price

    if side == OrderSide.BUY:

        slipped_price = (
            price
            * (
                1
                +
                slippage_percent
            )
        )

    elif side == OrderSide.SELL:

        slipped_price = (
            price
            * (
                1
                -
                slippage_percent
            )
        )

    return SlippageResult(
        expected_price=
        price,

        slipped_price=
        slipped_price,

        slippage_percent=
        slippage_percent,
    )