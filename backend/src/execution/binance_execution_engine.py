from src.execution.execution_interface import (
    ExecutionInterface,
)

from src.paper_execution.paper_order import (
    PaperOrder,
)

from src.exchange.binance_rest_client import (
    BinanceRestClient,
)


class BinanceExecutionEngine(
    ExecutionInterface
):

    def __init__(
        self,
        runtime,
    ):

        self.runtime = runtime

        self.rest_client = (
            BinanceRestClient()
        )

    def execute_order(
        self,
        order: PaperOrder,
    ) -> bool:

        raise NotImplementedError(
            "Binance live execution not implemented yet"
        )

    def cancel_order(
        self,
        order: PaperOrder,
    ) -> bool:

        raise NotImplementedError(
            "Binance order cancellation not implemented yet"
        )

    def process_pending_orders(
        self,
    ) -> None:

        pass
