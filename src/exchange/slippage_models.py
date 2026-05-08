from dataclasses import dataclass


@dataclass
class SlippageResult:

    expected_price: float

    slipped_price: float

    slippage_percent: float