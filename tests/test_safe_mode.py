from src.core.execution_gate import (
    evaluate_execution_permission,
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

permission = (
    evaluate_execution_permission(
        runtime
    )
)

print("SAFE MODE")
print(runtime.safe_mode)

print("\nPERMISSION")
print(permission)