from src.strategy.live_regime_detector import (
    LiveRegimeDetector,
)

from src.strategy.regime_adaptive_orchestrator import (
    RegimeAdaptiveOrchestrator,
)


class CognitiveRuntime:

    def __init__(
        self,
        registry,
        performance_tracker,
        regime_router,
    ):

        self.detector = (
            LiveRegimeDetector()
        )

        self.orchestrator = (
            RegimeAdaptiveOrchestrator(
                registry,
                performance_tracker,
                regime_router,
            )
        )

    def process_market_snapshot(
        self,
        snapshot,
    ):

        regime = (
            self.detector
            .detect_regime(
                snapshot.candles
            )
        )

        print()

        print(
            "DETECTED REGIME"
        )

        print(regime)

        decision = (
            self.orchestrator
            .evaluate(
                snapshot,
                regime,
            )
        )

        print()

        print(
            "COGNITIVE DECISION"
        )

        print(decision)

        return {
            "regime":
            regime,

            "decision":
            decision,
        }