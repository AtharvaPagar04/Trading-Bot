from src.core.monitoring import (
    generate_runtime_metrics,
)

from src.core.runtime_builder import (
    build_runtime_state,
)

from src.core.runtime_update import (
    process_runtime_trade,
)

from src.events.event_dispatcher import (
    dispatch_runtime_events,
)

from src.persistence.runtime_store import (
    persist_runtime_metrics,
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
]

for pnl in trade_results:
    runtime = process_runtime_trade(
        runtime=runtime,
        realized_pnl=pnl,
    )

    runtime = dispatch_runtime_events(
        runtime
    )

metrics = generate_runtime_metrics(
    runtime
)

persist_runtime_metrics(metrics)

print("Runtime metrics persisted")