from src.persistence.runtime_loader import (
    load_runtime_snapshot,
)

from src.core.recovery_policy import (
    evaluate_recovery_policy,
)

runtime = load_runtime_snapshot()

result = evaluate_recovery_policy(
    runtime
)

print(result)