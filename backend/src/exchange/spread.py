from src.exchange.models import (
    OrderSide,
)

from src.exchange.spread_models import (
    SpreadAdjustedPrice,
)


def apply_spread(
    market_price: float,

    spread_percent: float,

    side: OrderSide,
) -> SpreadAdjustedPrice:

    adjusted_price = (
        market_price
    )

    half_spread = (
        spread_percent / 2
    )

    if side == OrderSide.BUY:

        adjusted_price = (
            market_price
            * (
                1
                +
                half_spread
            )
        )

    elif side == OrderSide.SELL:

        adjusted_price = (
            market_price
            * (
                1
                -
                half_spread
            )
        )

    return SpreadAdjustedPrice(
        market_price=
        market_price,

        adjusted_price=
        adjusted_price,

        spread_percent=
        spread_percent,
    )