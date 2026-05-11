from dataclasses import dataclass


@dataclass
class EvolutionReport:

    previous_confidence: float

    evolved_confidence: float

    mutation_strength: float

    evolution_applied: bool

    evolution_reason: str