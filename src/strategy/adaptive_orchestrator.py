from collections import defaultdict


class AdaptiveOrchestrator:

    def __init__(
        self,
        registry,
        performance_tracker,
    ):

        self.registry = registry

        self.performance_tracker = (
            performance_tracker
        )

    def evaluate(
        self,
        snapshot,
    ):

        weighted_scores = (
            defaultdict(float)
        )

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

            stats = (
                self.performance_tracker
                .get_stats(name)
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
                f"STRATEGY: {name}"
            )

            print(
                "CONFIDENCE:",
                decision.confidence,
            )

            print(
                "WIN RATE:",
                reliability,
            )

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
            "ADAPTIVE SCORES"
        )

        print(
            dict(
                weighted_scores
            )
        )

        return final_signal