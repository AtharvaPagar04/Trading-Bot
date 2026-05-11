from src.db.runtime_repository import (
    RuntimeRepository,
)

repository = (
    RuntimeRepository()
)

repository.save_runtime_state(
    operating_state="NORMAL",

    safe_mode=False,

    total_trades=5,
)

runtime_state = (
    repository.load_runtime_state()
)

print(
    runtime_state.operating_state,
    runtime_state.safe_mode,
    runtime_state.total_trades,
)