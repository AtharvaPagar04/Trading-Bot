from src.risk.grid_protection import (
    evaluate_grid_protection,
)

grid_floor = 100

prices = [
    99,
    98,
    96,
    94,
]

for price in prices:
    state = (
        evaluate_grid_protection(
            current_price=price,
            grid_floor=grid_floor,
        )
    )

    print(
        f"Price: {price} | "
        f"Protection State: "
        f"{state}"
    )