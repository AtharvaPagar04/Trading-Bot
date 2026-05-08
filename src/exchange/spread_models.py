from dataclasses import dataclass


@dataclass
class SpreadAdjustedPrice:

    market_price: float

    adjusted_price: float

    spread_percent: float