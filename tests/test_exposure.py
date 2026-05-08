from src.risk.exposure import (
    allocate_capital,
    drawdown_size_multiplier,
)

capital = allocate_capital(2000)

print(capital)

drawdowns = [
    0.5,
    1.5,
    2.5,
    3.5,
]

for drawdown in drawdowns:
    multiplier = (
        drawdown_size_multiplier(
            drawdown
        )
    )

    print(
        f"Drawdown: {drawdown}% | "
        f"Size Multiplier: "
        f"{multiplier}"
    )