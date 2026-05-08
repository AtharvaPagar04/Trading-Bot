from src.core.runtime_governance_loop import (
    execute_governance_cycle,
)

from src.core.safe_mode import (
    apply_safe_mode,
)

from src.persistence.runtime_loader import (
    load_runtime_snapshot,
)

runtime = load_runtime_snapshot()

runtime = apply_safe_mode(
    runtime
)

print("INITIAL")
print(runtime.operating_state)

result = execute_governance_cycle(
    runtime=runtime,

    adx_value=18,

    atr_percent=1.5,

    stable_closes=2,
)

runtime = result.runtime

print("\nUPDATED")
print(runtime.operating_state)

print("\nMETRICS")
print(result.metrics)

print("\nEVENTS")
for event in runtime.active_events:
    print(event)