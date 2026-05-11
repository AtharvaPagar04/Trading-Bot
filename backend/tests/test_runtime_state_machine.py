from src.core.runtime_clearance import (
    clear_runtime_safe_mode,
)

from src.core.runtime_state_machine import (
    evaluate_runtime_state,
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

state = evaluate_runtime_state(
    runtime
)

print("SAFE MODE")
print(state)

runtime = clear_runtime_safe_mode(
    runtime
)

state = evaluate_runtime_state(
    runtime
)

print("\nAFTER CLEARANCE")
print(state)