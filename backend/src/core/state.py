from dataclasses import dataclass

from src.strategy.regime import RegimeState
from src.strategy.volatility import (
    VolatilityState,
)


@dataclass
class MarketState:
    timeframe: str

    adx: float
    atr_percent: float

    regime_state: RegimeState
    volatility_state: VolatilityState

    allow_entries: bool