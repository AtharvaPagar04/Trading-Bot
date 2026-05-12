from abc import ABC
from abc import abstractmethod


class BaseStrategy(
    ABC
):

    @abstractmethod
    def should_enter(
        self,
        market_state,
    ):

        pass

    @abstractmethod
    def should_exit(
        self,
        market_state,
        position,
    ):

        pass

    @abstractmethod
    def on_tick(
        self,
        market_state,
    ):

        pass

    @abstractmethod
    def get_name(
        self,
    ):

        pass