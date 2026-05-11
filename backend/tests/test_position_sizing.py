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

    utilization_percent=25,

    exposure_percent=20,

    pnl_percent=-4,

    allow_new_entries=True,
)

result = (
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

print(result)