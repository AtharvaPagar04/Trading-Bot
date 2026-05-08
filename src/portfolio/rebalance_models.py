from dataclasses import dataclass


@dataclass
class RebalanceAction:

    symbol: str

    old_allocation: float

    new_allocation: float


@dataclass
class PortfolioRebalanceReport:

    actions: list[RebalanceAction]

    fragility_score: float