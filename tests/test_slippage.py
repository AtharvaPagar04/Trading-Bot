from src.exchange.models import (
    OrderSide,
)

from src.exchange.slippage import (
    apply_slippage,
)

result = (
    apply_slippage(
        price=100,

        slippage_percent=0.002,

        side=
        OrderSide.BUY,
    )
)

print(result)