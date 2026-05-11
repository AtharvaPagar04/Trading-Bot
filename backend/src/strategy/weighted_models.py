from dataclasses import dataclass

from src.strategy.interface import (
    Strategy,
)


@dataclass
class WeightedStrategy:
    strategy: Strategy

    weight: float

    realized_pnl: float = 0.0

    wins: int = 0

    losses: int = 0