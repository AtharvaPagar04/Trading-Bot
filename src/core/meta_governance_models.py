from dataclasses import dataclass


@dataclass
class MetaGovernanceReport:

    system_confidence: float

    governance_score: float

    recalibration_required: bool

    recommendation: str