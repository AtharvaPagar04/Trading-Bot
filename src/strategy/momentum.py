from statistics import mean

from src.market.market_data import (
    MarketDataSnapshot,
)

from src.strategy.models import (
    SignalDecision,
    TradeSignal,
)


class MomentumStrategy:

    def generate_signal(
        self,

        snapshot: MarketDataSnapshot,
    ) -> SignalDecision:

        closes = [
            candle.close
            for candle
            in snapshot.candles
        ]

        short_ma = mean(
            closes[-5:]
        )

        long_ma = mean(
            closes[-15:]
        )

        if short_ma > long_ma:

            return SignalDecision(
                signal=
                TradeSignal.BUY,

                confidence=0.7,

                reason=
                "Bullish momentum",
            )

        if short_ma < long_ma:

            return SignalDecision(
                signal=
                TradeSignal.SELL,

                confidence=0.7,

                reason=
                "Bearish momentum",
            )

        return SignalDecision(
            signal=
            TradeSignal.HOLD,

            confidence=0.5,

            reason=
            "Neutral momentum",
        )