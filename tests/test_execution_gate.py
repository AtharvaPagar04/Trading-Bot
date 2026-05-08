from src.core.execution_gate import (
    evaluate_execution_permission,
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

runtime = build_runtime_state(
    capital=2000,
    timeframe="15m",
    adx_value=18,
    atr_percent=1.5,
)

permission = (
    evaluate_execution_permission(
        runtime
    )
)

print("\nINITIAL")
print(permission)

runtime = process_runtime_trade(
    runtime=runtime,
    realized_pnl=-300,
)

runtime = dispatch_runtime_events(
    runtime
)

permission = (
    evaluate_execution_permission(
        runtime
    )
)

print("\nAFTER DAMAGE")
print(permission)