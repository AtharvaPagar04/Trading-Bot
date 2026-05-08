from dataclasses import dataclass, field


@dataclass
class StrategyAttribution:

    strategy_name: str

    realized_pnl: float

    wins: int

    losses: int

    recent_pnls: list[float] = (
        field(default_factory=list)
    )