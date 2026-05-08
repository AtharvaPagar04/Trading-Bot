from src.portfolio.correlation_models import (
    CorrelationReport,
)

from src.portfolio.diversification_models import (
    DiversificationReport,
)


def evaluate_diversification(
    report: CorrelationReport,
) -> DiversificationReport:

    avg_corr = (
        report
        .average_correlation
    )

    diversification_score = (
        1
        -
        avg_corr
    )

    concentration_risk = (
        avg_corr
    )

    portfolio_fragility = (
        avg_corr
        ** 2
    )

    return DiversificationReport(
        diversification_score=
        diversification_score,

        concentration_risk=
        concentration_risk,

        average_correlation=
        avg_corr,

        portfolio_fragility=
        portfolio_fragility,
    )