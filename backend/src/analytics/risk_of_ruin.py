import random

from src.analytics.risk_of_ruin_models import (
    RiskOfRuinReport,
)


def analyze_risk_of_ruin(
    returns: list[float],

    simulations: int,

    starting_capital: float,

    ruin_threshold: float,
) -> RiskOfRuinReport:

    ruin_count = 0

    for _ in range(simulations):

        capital = (
            starting_capital
        )

        randomized_returns = (
            returns.copy()
        )

        random.shuffle(
            randomized_returns
        )

        for r in randomized_returns:

            capital += r

            if (
                capital
                <= ruin_threshold
            ):

                ruin_count += 1

                break

    survival_rate = (
        (
            simulations
            - ruin_count
        )
        / simulations
    )

    ruin_probability = (
        ruin_count
        / simulations
    )

    return RiskOfRuinReport(
        simulations=
        simulations,

        ruin_count=
        ruin_count,

        survival_rate=
        survival_rate,

        ruin_probability=
        ruin_probability,
    )