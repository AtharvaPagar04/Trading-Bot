from dataclasses import dataclass

from src.runtime.logging.runtime_logger import (
    runtime_log,
    LogLevel,
    LogCategory,
)
from src.db.runtime_repository import (
    RuntimeRepository,
)
@dataclass
class RuntimeRecoveryResult:

    restored: bool

    recovered_trades: int

    recovery_message: str

def recover_runtime_state(
    runtime_state,
):
    runtime_log(
        level=LogLevel.INFO,
        category=LogCategory.RUNTIME,
        message="Runtime recovery started",
    )
    repository = (
        RuntimeRepository()
    )
    persisted_state = (
        repository
        .load_runtime_state()
    )
   
    if persisted_state is None:

        runtime_log(
            level=LogLevel.WARNING,
            category=LogCategory.RUNTIME,
            message="No persisted runtime state found",
        )
        return RuntimeRecoveryResult(
            restored=False,
            recovered_trades=0,
            recovery_message="No persisted state available",
        )
    runtime_state.operating_state = (
        persisted_state
        .operating_state
    )

    runtime_state.safe_mode = (
        persisted_state
        .safe_mode
    )

    runtime_state.total_trades = (
        persisted_state
        .total_trades
    )
    runtime_log(
        level=LogLevel.INFO,
        category=LogCategory.RUNTIME,
        message="Persisted runtime state loaded",
    )

    return RuntimeRecoveryResult(
        restored=True,
        recovered_trades=persisted_state.total_trades,
        recovery_message="Persisted runtime state loaded",
    )