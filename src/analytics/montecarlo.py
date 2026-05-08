import random
from statistics import mean

from src.analytics.montecarlo_models import (
    MonteCarloResult,
)


def run_montecarlo_simulation(
    returns: list[float],

    simulations: int,

    noise_level: float,
) -> MonteCarloResult:

    simulation_results = []

    for _ in range(simulations):

        perturbed_returns = []

        for r in returns:

            noise = random.uniform(
                -noise_level,
                noise_level,
            )

            perturbed = (
                r
                *
                (
                    1
                    +
                    noise
                )
            )

            perturbed_returns.append(
                perturbed
            )

        total_return = sum(
            perturbed_returns
        )

        simulation_results.append(
            total_return
        )

    return MonteCarloResult(
        simulation_returns=
        simulation_results,

        average_return=
        mean(simulation_results),

        worst_return=
        min(simulation_results),

        best_return=
        max(simulation_results),
    )