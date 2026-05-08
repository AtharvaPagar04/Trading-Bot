from src.core.execution_gate import (
    evaluate_execution_permission,
)

from src.core.runtime_clearance import (
    clear_runtime_safe_mode,
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

print("BEFORE CLEARANCE")
print(
    evaluate_execution_permission(
        runtime
    )
)

runtime = clear_runtime_safe_mode(
    runtime
)

print("\nAFTER CLEARANCE")
print(
    evaluate_execution_permission(
        runtime
    )
)