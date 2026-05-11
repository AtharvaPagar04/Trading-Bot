from dataclasses import dataclass


@dataclass
class AsymmetricSpacing:
    base_spacing: float
    sell_spacing: float
    buy_spacing: float


def calculate_asymmetric_spacing(
    base_spacing: float,
) -> AsymmetricSpacing:
    sell_spacing = (
        base_spacing * 1.0
    )

    buy_spacing = (
        base_spacing * 1.5
    )

    return AsymmetricSpacing(
        base_spacing=
        round(base_spacing, 4),

        sell_spacing=
        round(sell_spacing, 4),

        buy_spacing=
        round(buy_spacing, 4),
    )