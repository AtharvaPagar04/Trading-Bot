from src.core.recovery_workflow import (
    evaluate_recovery_workflow,
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

result = evaluate_recovery_workflow(
    runtime=runtime,

    adx_value=18,

    atr_percent=1.5,

    stable_closes=2,
)

print("SAFE MODE ACTIVE")
print(result)

runtime = clear_runtime_safe_mode(
    runtime
)

result = evaluate_recovery_workflow(
    runtime=runtime,

    adx_value=18,

    atr_percent=1.5,

    stable_closes=2,
)

print("\nSAFE MODE CLEARED")
print(result)