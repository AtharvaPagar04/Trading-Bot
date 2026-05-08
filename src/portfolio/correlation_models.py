from dataclasses import dataclass


@dataclass
class AssetCorrelation:

    asset_a: str

    asset_b: str

    correlation: float


@dataclass
class CorrelationReport:

    correlations: list[AssetCorrelation]

    average_correlation: float