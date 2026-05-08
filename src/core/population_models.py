from dataclasses import dataclass


@dataclass
class IntelligenceAgent:

    name: str

    confidence: float

    fitness_score: float

    survived: bool


@dataclass
class PopulationReport:

    agents: list[IntelligenceAgent]

    surviving_agents: int

    average_fitness: float