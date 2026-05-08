from statistics import mean

from src.portfolio.correlation_models import (
    AssetCorrelation,
)

from src.portfolio.correlation_models import (
    CorrelationReport,
)


def analyze_correlations(
    correlations:
    dict[tuple[str, str], float],
) -> CorrelationReport:

    reports = []

    values = []

    for (
        assets,
        corr
    ) in correlations.items():

        asset_a, asset_b = assets

        reports.append(
            AssetCorrelation(
                asset_a=
                asset_a,

                asset_b=
                asset_b,

                correlation=
                corr,
            )
        )

        values.append(corr)

    average_corr = 0.0

    if len(values) > 0:

        average_corr = (
            mean(values)
        )

    return CorrelationReport(
        correlations=
        reports,

        average_correlation=
        average_corr,
    )