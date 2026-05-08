from src.core.runtime_auto_escalation import (
    auto_escalate_runtime,
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

print("BEFORE")
print(runtime.operating_state)

runtime = auto_escalate_runtime(
    runtime
)

print("\nAFTER")
print(runtime.operating_state)

print("\nEVENTS")
for event in runtime.active_events:
    print(event)