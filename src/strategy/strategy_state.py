from dataclasses import dataclass
from datetime import datetime
from src.strategy.models import (
    TradeSignal,
)

@dataclass
class StrategyState:

    last_signal: (
        TradeSignal | None
    ) = None

    last_execution_time: (
        datetime | None
    ) = None