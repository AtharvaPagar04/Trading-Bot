from collections import defaultdict


class StrategyPerformanceTracker:

    def __init__(self):

        self.performance = (
            defaultdict(
                lambda: {
                    "wins": 0,
                    "losses": 0,
                    "pnl": 0.0,
                }
            )
        )

    def record_trade(
        self,
        strategy_name: str,
        pnl: float,
    ):

        if pnl > 0:

            self.performance[
                strategy_name
            ]["wins"] += 1

        else:

            self.performance[
                strategy_name
            ]["losses"] += 1

        self.performance[
            strategy_name
        ]["pnl"] += pnl

    def get_stats(
        self,
        strategy_name: str,
    ):

        stats = (
            self.performance[
                strategy_name
            ]
        )

        total = (
            stats["wins"]
            +
            stats["losses"]
        )

        win_rate = 0

        if total > 0:

            win_rate = (
                stats["wins"]
                / total
            )

        return {
            "wins":
            stats["wins"],

            "losses":
            stats["losses"],

            "pnl":
            stats["pnl"],

            "win_rate":
            win_rate,
        }

    def full_report(self):

        report = {}

        for strategy in (
            self.performance
        ):

            report[
                strategy
            ] = self.get_stats(
                strategy
            )

        return report