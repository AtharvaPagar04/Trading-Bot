import random

from src.exchange.execution_simulator_models import (
    SimulatedExecution,
)


class ExecutionSimulator:

    def __init__(self):

        self.max_slippage_percent = (
            0.002
        )

        self.max_latency_ms = 250

        self.partial_fill_probability = (
            0.3
        )

    def simulate_execution(
        self,
        market_price: float,
        quantity: float,
    ):

        latency = random.randint(
            10,
            self.max_latency_ms,
        )

        slippage_percent = (
            random.uniform(
                0,
                self.max_slippage_percent,
            )
        )

        executed_price = (
            market_price
            *
            (
                1
                +
                slippage_percent
            )
        )

        partial_fill = (
            random.random()
            <
            self.partial_fill_probability
        )

        filled_quantity = quantity

        if partial_fill:

            filled_quantity = (
                quantity
                *
                random.uniform(
                    0.3,
                    0.9,
                )
            )

        successful = True

        rejection_reason = None

        if filled_quantity <= 0:

            successful = False

            rejection_reason = (
                "NO_LIQUIDITY"
            )

        return SimulatedExecution(
            requested_price=
            market_price,

            executed_price=
            executed_price,

            quantity_requested=
            quantity,

            quantity_filled=
            filled_quantity,

            slippage=
            executed_price
            -
            market_price,

            latency_ms=
            latency,

            execution_successful=
            successful,

            rejection_reason=
            rejection_reason,
        )