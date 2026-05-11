from src.core.runtime_builder import (
    build_runtime_state,
)

from src.core.runtime_update import (
    process_runtime_trade,
)

runtime = build_runtime_state(
    capital=2000,
    timeframe="15m",
    adx_value=18,
    atr_percent=1.5,
)

trade_results = [
    40,
    -50,
    -100,
    -120,
]

for pnl in trade_results:
    runtime = process_runtime_trade(
        runtime=runtime,
        realized_pnl=pnl,
    )

    print("\nSESSION")
    print(runtime.session)

    print("\nRISK")
    print(runtime.risk_state)

    print("\nEVENTS")
    for event in runtime.active_events:
        print(event)