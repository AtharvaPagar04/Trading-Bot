from src.core.runtime_builder import (
    build_runtime_state,
)

from src.core.runtime_update import (
    process_runtime_trade,
)

from src.events.event_dispatcher import (
    dispatch_runtime_events,
)

from src.persistence.event_store import (
    persist_runtime_events,
)

runtime = build_runtime_state(
    capital=2000,
    timeframe="15m",
    adx_value=18,
    atr_percent=1.5,
)

trade_results = [
    -50,
    -100,
    -120,
]

for pnl in trade_results:
    runtime = process_runtime_trade(
        runtime=runtime,
        realized_pnl=pnl,
    )

runtime = dispatch_runtime_events(
    runtime
)

persist_runtime_events(
    runtime.event_history
)

print("Runtime events persisted")