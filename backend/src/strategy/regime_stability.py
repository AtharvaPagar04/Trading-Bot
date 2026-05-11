from collections import Counter

from src.strategy.regime_stability_models import (
    RegimeStability,
)


def analyze_regime_stability(
    regimes: list[str],
) -> RegimeStability:

    counts = Counter(regimes)

    dominant_regime = (
        counts.most_common(1)[0][0]
    )

    dominant_count = (
        counts[dominant_regime]
    )

    transitions = 0

    for i in range(
        1,
        len(regimes),
    ):

        if (
            regimes[i]
            !=
            regimes[i - 1]
        ):

            transitions += 1

    stability_score = (
        dominant_count
        / len(regimes)
    )

    return RegimeStability(
        dominant_regime=
        dominant_regime,

        stability_score=
        stability_score,

        transitions=
        transitions,

        total_samples=
        len(regimes),
    )