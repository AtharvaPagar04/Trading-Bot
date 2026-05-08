from src.persistence.runtime_loader import (
    load_runtime_snapshot,
)

runtime = load_runtime_snapshot()

print(runtime)