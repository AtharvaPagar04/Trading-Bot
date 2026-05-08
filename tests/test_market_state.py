from src.core.state_builder import (
    build_market_state,
)

state = build_market_state(
    timeframe="15m",
    adx_value=22,
    atr_percent=1.8,
)

print(state)