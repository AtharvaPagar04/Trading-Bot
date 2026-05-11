from src.risk.capital_governance import (
    CapitalGovernance,
)

governance = (
    CapitalGovernance()
)

approval = (
    governance.approve_trade(
        cash_balance=10000,

        market_price=100000,

        requested_quantity=0.1,
    )
)

print()

print(
    "CAPITAL APPROVAL"
)

print(approval)