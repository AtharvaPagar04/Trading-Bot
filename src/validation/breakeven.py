def calculate_minimum_grid_spacing(
    maker_fee_pct: float,
    taker_fee_pct: float,
    spread_pct: float,
    slippage_pct: float,
) -> float:
    minimum_spacing = (
        (maker_fee_pct + taker_fee_pct)
        + spread_pct
        + slippage_pct
    )

    return round(minimum_spacing, 4)