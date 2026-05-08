from dataclasses import dataclass


@dataclass
class RuntimeConfig:

    symbol: str = "BTCUSDT"

    websocket_symbol: str = (
        "btcusdt"
    )

    candle_interval_seconds: int = 10

    max_drawdown: float = 0.10

    max_daily_loss: float = 0.05

    default_position_size: float = (
        0.001
    )

    runtime_duration_seconds: int = (
        30
    )


CONFIG = RuntimeConfig()