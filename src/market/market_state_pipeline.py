import pandas as pd

from src.core.state import (
    MarketState,
)

from src.indicators.adx import (
    calculate_adx,
)

from src.indicators.atr import (
    calculate_atr,
)

from src.market.market_data import (
    MarketDataSnapshot,
)

from src.risk.regime import (
    evaluate_market_regime,
)

from src.risk.volatility import (
    classify_volatility,
)


def generate_market_state(
    snapshot: MarketDataSnapshot,
) -> MarketState:

    df = pd.DataFrame(
        [
            {
                "open": candle.open,
                "high": candle.high,
                "low": candle.low,
                "close": candle.close,
                "volume": candle.volume,
            }
            for candle
            in snapshot.candles
        ]
    )

    atr_series = calculate_atr(
        df
    )

    adx_series = calculate_adx(
        df
    )

    atr_percent = float(
        atr_series.iloc[-1]
    )

    adx_value = adx_series.iloc[-1]

    if pd.isna(adx_value):
        adx_value = 0.0

    adx_value = float(adx_value)

    volatility_state = (
        classify_volatility(
            atr_percent
        )
    )

    regime = (
        evaluate_market_regime(
            adx_value
        )
    )

    return MarketState(
        timeframe=
        snapshot.timeframe,

        adx=adx_value,

        atr_percent=
        atr_percent,

        regime_state=
        regime.regime_state,

        volatility_state=
        volatility_state,

        allow_entries=
        regime.allow_entries,
    )