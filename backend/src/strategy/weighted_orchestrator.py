from collections import defaultdict

from src.strategy.models import (
    TradeSignal,
)


class WeightedStrategyOrchestrator:

    def __init__(
        self,
        registry,
    ):

        self.registry = registry

    def evaluate(
        self,
        snapshot,
    ):

        weighted_scores = (
            defaultdict(float)
        )

        strategy_details = []

        for (
            name,
            strategy
        ) in (
            self.registry
            .get_all()
            .items()
        ):

            decision = (
                strategy.generate_signal(
                    snapshot
                )
            )

            weighted_scores[
                decision.signal
            ] += (
                decision.confidence
            )

            strategy_details.append(
                (
                    name,
                    decision,
                )
            )

        for (
            name,
            decision
        ) in strategy_details:

            print()

            print(
                f"STRATEGY: {name}"
            )

            print(decision)

        if (
            len(weighted_scores)
            == 0
        ):

            return None

        final_signal = max(
            weighted_scores,
            key=
            weighted_scores.get,
        )

        print()

        print(
            "WEIGHTED SCORES"
        )

        print(
            dict(
                weighted_scores
            )
        )

        return final_signal