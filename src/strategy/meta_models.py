from dataclasses import dataclass


@dataclass
class EnsemblePerformance:

    ensemble_name: str

    realized_pnl: float

    wins: int

    losses: int

    usage_count: int