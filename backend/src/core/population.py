from statistics import mean

from src.core.population_models import (
    IntelligenceAgent,
)

from src.core.population_models import (
    PopulationReport,
)


def evaluate_population(
    agents:
    list[IntelligenceAgent],
) -> PopulationReport:

    surviving = 0

    fitness_values = []

    for agent in agents:

        fitness_values.append(
            agent.fitness_score
        )

        if agent.survived:

            surviving += 1

    average_fitness = 0.0

    if len(fitness_values) > 0:

        average_fitness = (
            mean(fitness_values)
        )

    return PopulationReport(
        agents=agents,

        surviving_agents=
        surviving,

        average_fitness=
        average_fitness,
    )