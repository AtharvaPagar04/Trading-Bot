class StrategyRegistry:

    def __init__(self):

        self.strategies = {}

    def register(
        self,
        name: str,
        strategy,
    ):

        self.strategies[
            name
        ] = strategy

    def get_strategy(
        self,
        name: str,
    ):

        return (
            self.strategies.get(
                name
            )
        )

    def get_all(self):

        return self.strategies