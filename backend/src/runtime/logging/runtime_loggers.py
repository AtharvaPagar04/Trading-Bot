from src.logging.runtime_logger import (
    build_logger,
)

runtime_logger = build_logger(
    "RUNTIME"
)

governance_logger = build_logger(
    "GOVERNANCE"
)

session_logger = build_logger(
    "SESSION"
)

recovery_logger = build_logger(
    "RECOVERY"
)
