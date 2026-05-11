from collections import defaultdict

from src.market.market_data import (
    MarketDataSnapshot,
)

from src.strategy.models import (
    SignalDecision,
    TradeSignal,
)

from src.strategy.weighted_models import (
    WeightedStrategy,
)


class EnsembleStrategy:

    def __init__(
        self,

        strategies:
        list[WeightedStrategy],
    ):

        self.strategies = (
            strategies
        )

    def generate_signal(
        self,

        snapshot: MarketDataSnapshot,
    ) -> SignalDecision:

        weighted_scores = (
            defaultdict(float)
        )

        total_weight = 0.0

        for weighted_strategy in (
            self.strategies
        ):

            decision = (
                weighted_strategy
                .strategy
                .generate_signal(
                    snapshot
                )
            )

            weighted_score = (
                weighted_strategy
                .weight
                *
                decision.confidence
            )

            weighted_scores[
                decision.signal
            ] += weighted_score

            total_weight += (
                weighted_score
            )

        dominant_signal = max(
            weighted_scores,

            key=
            weighted_scores.get,
        )

        dominant_score = (
            weighted_scores[
                dominant_signal
            ]
        )

        confidence = 0.0

        if total_weight > 0:

            confidence = (
                dominant_score
                / total_weight
            )

        return SignalDecision(
            signal=
            dominant_signal,

            confidence=
            confidence,

            reason=
            "Weighted ensemble consensus",
        )