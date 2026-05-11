from datetime import datetime

from src.market.candle_models import (
    Candle,
)

from src.strategy.live_regime_detector import (
    LiveRegimeDetector,
)

candles = []

prices = [
    100,
    102,
    104,
    106,
    108,
    110,
]

for price in prices:

    candles.append(
        Candle(
            open=price,
            high=price + 1,
            low=price - 1,
            close=price,
            volume=10,
            timestamp=
            datetime.utcnow(),
        )
    )

detector = (
    LiveRegimeDetector()
)

regime = (
    detector.detect_regime(
        candles
    )
)

print()

print(
    "DETECTED REGIME"
)

print(regime)