from src.risk.dynamic_position_sizer import (
    DynamicPositionSizer,
)

sizer = (
    DynamicPositionSizer()
)

quantity = (
    sizer.calculate_size(
        equity=10000,

        market_price=100000,

        base_risk_percent=0.02,

        confidence=0.8,

        volatility_multiplier=0.7,

        drawdown_multiplier=0.9,
    )
)

print()

print(
    "FINAL POSITION SIZE"
)

print(quantity)