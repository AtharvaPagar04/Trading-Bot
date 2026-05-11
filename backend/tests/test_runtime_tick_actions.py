from src.core.runtime_tick_actions import (
    execute_tick_actions,
)

from src.persistence.runtime_loader import (
    load_runtime_snapshot,
)

runtime = load_runtime_snapshot()

result = execute_tick_actions(
    runtime
)

print("HEARTBEAT")
print(result.heartbeat)

print("\nMETRICS")
print(result.metrics)