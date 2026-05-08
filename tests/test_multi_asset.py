from src.portfolio.multi_asset import (
    generate_portfolio_allocations,
)

scores = {
    "BTC/USDT": 0.9,
    "ETH/USDT": 0.6,
    "SOL/USDT": 0.5,
}

report = (
    generate_portfolio_allocations(
        confidence_scores=
        scores
    )
)

print(report)