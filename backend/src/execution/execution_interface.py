from abc import (
    ABC,
    abstractmethod,
)

from src.paper_execution.paper_order import (
    PaperOrder,
)


class ExecutionInterface(
    ABC,
):

    @abstractmethod
    def execute_order(
        self,
        order: PaperOrder,
    ) -> bool:
        pass

    @abstractmethod
    def cancel_order(
        self,
        order: PaperOrder,
    ) -> bool:
        pass

    @abstractmethod
    def process_pending_orders(
        self,
    ) -> None:
        pass