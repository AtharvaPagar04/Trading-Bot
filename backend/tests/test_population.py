from src.core.population import (
    evaluate_population,
)

from src.core.population_models import (
    IntelligenceAgent,
)

agents = [

    IntelligenceAgent(
        name="Agent-A",

        confidence=0.8,

        fitness_score=0.9,

        survived=True,
    ),

    IntelligenceAgent(
        name="Agent-B",

        confidence=0.5,

        fitness_score=0.4,

        survived=False,
    ),

    IntelligenceAgent(
        name="Agent-C",

        confidence=0.7,

        fitness_score=0.8,

        survived=True,
    ),
]

report = (
    evaluate_population(
        agents
    )
)

print(report)