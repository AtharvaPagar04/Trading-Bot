from src.core.runtime_builder import (
    build_runtime_state,
)

from src.core.runtime_state_machine import (
    RuntimeOperatingState,
)

from src.core.runtime_transition_engine import (
    execute_runtime_transition,
)

runtime = build_runtime_state(
    capital=2000,
    timeframe="15m",
    adx_value=18,
    atr_percent=1.5,
)

print("INITIAL")
print(runtime.operating_state)

result = execute_runtime_transition(
    runtime=runtime,

    target_state=
    RuntimeOperatingState
    .REDUCE_RISK,
)

print("\nTRANSITION")
print(result)

print("\nUPDATED STATE")
print(runtime.operating_state)

print("\nACTIVE EVENTS")
for event in runtime.active_events:
    print(event)