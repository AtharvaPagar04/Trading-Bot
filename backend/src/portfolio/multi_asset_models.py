from dataclasses import dataclass


@dataclass
class AssetAllocation:

    symbol: str

    allocation_percent: float

    confidence_score: float


@dataclass
class PortfolioAllocationReport:

    allocations: list[AssetAllocation]

    total_allocated: float