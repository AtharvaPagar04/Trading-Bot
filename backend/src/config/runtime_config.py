from dataclasses import (
    dataclass,
)


@dataclass
class RuntimeConfig:

    starting_capital: float = (
        1000.0
    )

    default_timeframe: str = (
        "5m"
    )

    default_adx: float = (
        20.0
    )

    default_atr_percent: float = (
        1.0
    )

    cooldown_seconds: int = (
        30
    )

    max_reconnect_attempts: int = (
        5
    )

    reconciliation_tolerance: float = (
        0.01
    )