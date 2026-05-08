from src.risk.kill_switch_models import (
    KillSwitchStatus,
)


class KillSwitch:

    def __init__(
        self,
        max_drawdown: float = 0.10,
        max_daily_loss: float = 0.05,
    ):

        self.max_drawdown = (
            max_drawdown
        )

        self.max_daily_loss = (
            max_daily_loss
        )

    def evaluate_risk(
        self,
        current_drawdown: float,
        daily_loss: float,
    ) -> KillSwitchStatus:

        if (
            current_drawdown
            >=
            self.max_drawdown
        ):

            return KillSwitchStatus(
                trading_allowed=False,

                trigger_reason=
                "MAX_DRAWDOWN_EXCEEDED",

                current_drawdown=
                current_drawdown,

                daily_loss=
                daily_loss,
            )

        if (
            daily_loss
            >=
            self.max_daily_loss
        ):

            return KillSwitchStatus(
                trading_allowed=False,

                trigger_reason=
                "MAX_DAILY_LOSS_EXCEEDED",

                current_drawdown=
                current_drawdown,

                daily_loss=
                daily_loss,
            )

        return KillSwitchStatus(
            trading_allowed=True,

            trigger_reason=
            "NONE",

            current_drawdown=
            current_drawdown,

            daily_loss=
            daily_loss,
        )