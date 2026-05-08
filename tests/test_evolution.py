from src.core.evolution import (
    evolve_system,
)

from src.core.meta_governance_models import (
    MetaGovernanceReport,
)

governance = (
    MetaGovernanceReport(
        system_confidence=0.0032,

        governance_score=0.32,

        recalibration_required=True,

        recommendation=
        "Reduce risk and recalibrate",
    )
)

report = (
    evolve_system(
        governance
    )
)

print(report)