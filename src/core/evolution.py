from src.core.evolution_models import (
    EvolutionReport,
)

from src.core.meta_governance_models import (
    MetaGovernanceReport,
)


def evolve_system(
    governance:
    MetaGovernanceReport,
) -> EvolutionReport:

    previous = (
        governance
        .system_confidence
    )

    mutation_strength = 0.0

    evolution_applied = False

    evolved = previous

    reason = (
        "No evolution required"
    )

    if (
        governance
        .recalibration_required
    ):

        mutation_strength = 0.25

        evolved = (
            previous
            *
            (
                1
                +
                mutation_strength
            )
        )

        evolution_applied = True

        reason = (
            "Applied adaptive evolution"
        )

    return (
        EvolutionReport(
            previous_confidence=
            previous,

            evolved_confidence=
            evolved,

            mutation_strength=
            mutation_strength,

            evolution_applied=
            evolution_applied,

            evolution_reason=
            reason,
        )
    )