from src.exchange.execution_decision import (
    evaluate_execution_decision,
)

from src.exchange.portfolio_risk import (
    PortfolioRiskLevel,
    PortfolioRiskState,
)

from src.exchange.position_sizing import (
    calculate_position_size,
)

risk = PortfolioRiskState(
    risk_level=
    PortfolioRiskLevel
    .CAUTION,

    utilization_percent=20,

    exposure_percent=15,

    pnl_percent=-4,

    allow_new_entries=True,
)

position_size = (
    calculate_position_size(
        available_capital=2000,

        asset_price=100,

        runtime_state=
        "RECOVERY",

        portfolio_risk=
        risk,

        volatility_percent=3.5,
    )
)

decision = (
    evaluate_execution_decision(
        runtime_state=
        "RECOVERY",

        entries_allowed=
        True,

        market_entries_allowed=
        True,

        portfolio_entries_allowed=
        risk.allow_new_entries,

        position_size=
        position_size,
    )
)

print(decision)