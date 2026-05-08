from dataclasses import dataclass
from enum import Enum


class TradeSignal(
    str,
    Enum,
):
    BUY = "BUY"

    SELL = "SELL"

    HOLD = "HOLD"


@dataclass
class SignalDecision:
    signal: TradeSignal

    confidence: float

    reason: str