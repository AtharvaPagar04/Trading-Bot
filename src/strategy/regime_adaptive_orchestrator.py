from collections import defaultdict


class RegimeAdaptiveOrchestrator:

    def __init__(
        self,
        registry,
        performance_tracker,
        regime_router,
    ):

        self.registry = registry

        self.performance_tracker = (
            performance_tracker
        )

        self.regime_router = (
            regime_router
        )

    def evaluate(
        self,
        snapshot,
        regime: str,
    ):

        active = (
            self.regime_router
            .get_active_strategies(
                regime
            )
        )

        weighted_scores = (
            defaultdict(float)
        )

        print()

        print(
            f"ACTIVE REGIME: {regime}"
        )

        print(
            f"ACTIVE STRATEGIES: {active}"
        )

        for strategy_name in active:

            strategy = (
                self.registry
                .get_strategy(
                    strategy_name
                )
            )

            if strategy is None:

                continue

            decision = (
                strategy.generate_signal(
                    snapshot
                )
            )

            stats = (
                self.performance_tracker
                .get_stats(
                    strategy_name
                )
            )

            reliability = (
                stats["win_rate"]
            )

            adaptive_weight = (
                decision.confidence
                *
                (
                    1
                    +
                    reliability
                )
            )

            weighted_scores[
                decision.signal
            ] += adaptive_weight

            print()

            print(
                f"STRATEGY: {strategy_name}"
            )

            print(decision)

            print(
                "ADAPTIVE WEIGHT:",
                adaptive_weight,
            )

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
            "REGIME SCORES"
        )

        print(
            dict(
                weighted_scores
            )
        )

        return final_signal