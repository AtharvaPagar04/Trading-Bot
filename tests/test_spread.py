from src.exchange.models import (
    OrderSide,
)

from src.exchange.spread import (
    apply_spread,
)

result = (
    apply_spread(
        market_price=100,

        spread_percent=0.002,

        side=
        OrderSide.BUY,
    )
)

print(result)