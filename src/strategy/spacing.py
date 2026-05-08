def calculate_dynamic_grid_spacing(
    atr_percent: float,
    minimum_spacing_percent: float,
) -> float:
    final_spacing = max(
        atr_percent,
        minimum_spacing_percent,
    )

    return round(final_spacing, 4)