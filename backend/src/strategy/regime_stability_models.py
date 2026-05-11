from dataclasses import dataclass


@dataclass
class RegimeStability:

    dominant_regime: str

    stability_score: float

    transitions: int

    total_samples: int