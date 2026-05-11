from collections import Counter

from src.strategy.models import (
    TradeSignal,
)


class StrategyOrchestrator:

    def __init__(
        self,
        registry,
    ):

        self.registry = registry

    def evaluate(
        self,
        snapshot,
    ):

        signals = []

        for (
            name,
            strategy
        ) in (
            self.registry
            .get_all()
            .items()
        ):

            signal = (
                strategy.generate_signal(
                    snapshot
                )
            )

            print()

            print(
                f"STRATEGY: {name}"
            )

            print(signal)

            signals.append(
                signal.signal
            )

        if len(signals) == 0:

            return None

        vote = (
            Counter(signals)
            .most_common(1)[0][0]
        )

        return vote