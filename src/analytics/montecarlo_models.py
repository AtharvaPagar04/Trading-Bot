from dataclasses import dataclass


@dataclass
class MonteCarloResult:

    simulation_returns: list[float]

    average_return: float

    worst_return: float

    best_return: float