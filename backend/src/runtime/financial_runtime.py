from src.exchange.execution_simulator import (
    ExecutionSimulator,
)

from src.portfolio.accounting_engine import (
    PortfolioAccountingEngine,
)


class FinancialRuntime:

    def __init__(self):

        self.execution_simulator = (
            ExecutionSimulator()
        )

        self.accounting_engine = (
            PortfolioAccountingEngine(
                initial_cash=10000
            )
        )

    def execute_trade(
        self,
        symbol: str,
        market_price: float,
        quantity: float,
    ):

        execution = (
            self.execution_simulator
            .simulate_execution(
                market_price=
                market_price,

                quantity=
                quantity,
            )
        )

        print()

        print(
            "EXECUTION RESULT"
        )

        print(execution)

        if not (
            execution
            .execution_successful
        ):

            print()

            print(
                "EXECUTION FAILED"
            )

            return None

        self.accounting_engine.open_position(
            symbol=symbol,

            quantity=
            execution.quantity_filled,

            entry_price=
            execution.executed_price,
        )

        return execution

    def update_market(
        self,
        symbol: str,
        market_price: float,
    ):

        self.accounting_engine.update_market_price(
            symbol=symbol,

            market_price=
            market_price,
        )

    def portfolio_status(self):

        snapshot = (
            self.accounting_engine
            .portfolio_snapshot()
        )

        print()

        print(
            "PORTFOLIO STATUS"
        )

        print(snapshot)

        return snapshot