from src.core.hierarchy_models import (
    HierarchicalIntelligenceReport,
)

from src.core.meta_governance_models import (
    MetaGovernanceReport,
)


def evaluate_meta_governance(
    hierarchy:
    HierarchicalIntelligenceReport,
) -> MetaGovernanceReport:

    confidence = (
        hierarchy
        .system_confidence
    )

    governance_score = (
        confidence
        * 100
    )

    recalibration_required = (
        confidence < 0.005
    )

    recommendation = (
        "System stable"
    )

    if recalibration_required:

        recommendation = (
            "Reduce risk and recalibrate"
        )

    return (
        MetaGovernanceReport(
            system_confidence=
            confidence,

            governance_score=
            governance_score,

            recalibration_required=
            recalibration_required,

            recommendation=
            recommendation,
        )
    )