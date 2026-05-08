from src.runtime.instrumentation import (
    RuntimeInstrumentation,
)

RuntimeInstrumentation.track_event(
    event_type=
    "MARKET_TICK",

    payload={
        "symbol":
        "BTCUSDT",

        "price":
        100000,
    },
)

RuntimeInstrumentation.track_event(
    event_type=
    "SIGNAL_GENERATED",

    payload={
        "signal":
        "BUY",

        "confidence":
        0.9,
    },
)

print()

print(
    "INSTRUMENTATION COMPLETE"
)