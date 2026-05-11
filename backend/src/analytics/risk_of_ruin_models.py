from dataclasses import dataclass


@dataclass
class RiskOfRuinReport:

    simulations: int

    ruin_count: int

    survival_rate: float

    ruin_probability: float