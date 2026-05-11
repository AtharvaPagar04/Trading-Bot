from src.persistence.runtime_loader import (
    load_runtime_snapshot,
)

from src.core.runtime_integrity import (
    validate_runtime_integrity,
)

runtime = load_runtime_snapshot()

report = validate_runtime_integrity(
    runtime
)

print(report)