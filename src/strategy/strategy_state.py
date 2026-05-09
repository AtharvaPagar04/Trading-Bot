from dataclasses import dataclass

from src.strategy.models import (
    TradeSignal,
)


@dataclass
class StrategyState:

    last_signal: (
        TradeSignal | None
    ) = None