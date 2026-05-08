from src.analytics.montecarlo import (
    run_montecarlo_simulation,
)

returns = [
    10,
    -5,
    8,
    12,
    -3,
]

result = (
    run_montecarlo_simulation(
        returns=
        returns,

        simulations=100,

        noise_level=0.2,
    )
)

print(result)