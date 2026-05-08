from src.core.state import MarketState
from src.strategy.regime import (
    classify_regime,
    allow_new_entries,
)
from src.strategy.volatility import (
    classify_volatility,
)


def build_market_state(
    timeframe: str,
    adx_value: float,
    atr_percent: float,
) -> MarketState:
    regime_state = classify_regime(
        adx_value
    )

    volatility_state = classify_volatility(
        atr_percent
    )

    entries_allowed = allow_new_entries(
        regime_state
    )

    return MarketState(
        timeframe=timeframe,
        adx=adx_value,
        atr_percent=atr_percent,
        regime_state=regime_state,
        volatility_state=volatility_state,
        allow_entries=entries_allowed,
    )