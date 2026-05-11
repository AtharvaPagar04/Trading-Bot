from src.core.runtime_builder import (
    build_runtime_state,
)

runtime = build_runtime_state(
    capital=2000,
    timeframe="15m",
    adx_value=18,
    atr_percent=1.5,
)

print(runtime)