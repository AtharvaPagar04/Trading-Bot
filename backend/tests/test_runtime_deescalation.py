from src.core.runtime_deescalation import (
    auto_deescalate_runtime,
)

from src.core.runtime_state_machine import (
    RuntimeOperatingState,
)

from src.persistence.runtime_loader import (
    load_runtime_snapshot,
)

runtime = load_runtime_snapshot()

runtime.safe_mode = False

runtime.operating_state = (
    RuntimeOperatingState
    .SAFE_MODE
    .value
)

print("INITIAL")
print(runtime.operating_state)

runtime = auto_deescalate_runtime(
    runtime=runtime,

    adx_value=18,

    atr_percent=1.5,

    stable_closes=2,
)

print("\nSTEP 1")
print(runtime.operating_state)

runtime = auto_deescalate_runtime(
    runtime=runtime,

    adx_value=18,

    atr_percent=1.5,

    stable_closes=2,
)

print("\nSTEP 2")
print(runtime.operating_state)

runtime = auto_deescalate_runtime(
    runtime=runtime,

    adx_value=18,

    atr_percent=1.5,

    stable_closes=2,
)

print("\nSTEP 3")
print(runtime.operating_state)

print("\nEVENTS")
for event in runtime.active_events:
    print(event)