class RegimeRouter:

    def __init__(self):

        self.regime_map = {
            "TREND": [
                "trend_following",
            ],

            "RANGE": [
                "mean_reversion",
            ],

            "VOLATILE": [
                "breakout",
            ],
        }

    def get_active_strategies(
        self,
        regime: str,
    ):

        return (
            self.regime_map.get(
                regime,
                [],
            )
        )