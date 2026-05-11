from statistics import mean

from src.market.market_data import (
    MarketDataSnapshot,
)

from src.strategy.models import (
    SignalDecision,
    TradeSignal,
)


class MeanReversionStrategy:

    def generate_signal(
        self,

        snapshot: MarketDataSnapshot,
    ) -> SignalDecision:

        closes = [
            candle.close
            for candle
            in snapshot.candles
        ]

        current_price = (
            closes[-1]
        )

        moving_average = (
            mean(closes[-10:])
        )

        deviation_percent = (
            (
                current_price
                -
                moving_average
            )
            / moving_average
        ) * 100

        if deviation_percent <= -2:

            return SignalDecision(
                signal=
                TradeSignal.BUY,

                confidence=0.8,

                reason=
                "Price below moving average",
            )

        if deviation_percent >= 2:

            return SignalDecision(
                signal=
                TradeSignal.SELL,

                confidence=0.8,

                reason=
                "Price above moving average",
            )

        return SignalDecision(
            signal=
            TradeSignal.HOLD,

            confidence=0.5,

            reason=
            "Price near equilibrium",
        )