from dataclasses import dataclass
from enum import Enum


class SignalType(
    str,
    Enum,
):

    BUY = "BUY"

    SELL = "SELL"

    HOLD = "HOLD"


@dataclass
class StrategySignal:

    symbol: str

    signal_type: SignalType

    confidence: float