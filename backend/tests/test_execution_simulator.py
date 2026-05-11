from src.exchange.execution_simulator import (
    ExecutionSimulator,
)

simulator = (
    ExecutionSimulator()
)

execution = (
    simulator.simulate_execution(
        market_price=100000,

        quantity=0.1,
    )
)

print()

print(
    "SIMULATED EXECUTION"
)

print(execution)