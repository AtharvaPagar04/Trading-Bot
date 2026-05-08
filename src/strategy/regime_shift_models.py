from dataclasses import dataclass


@dataclass
class RegimeShiftDetection:

    regime_changed: bool

    previous_regime: str

    current_regime: str

    trigger_reason: str