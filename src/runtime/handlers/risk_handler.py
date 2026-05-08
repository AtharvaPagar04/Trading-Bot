from src.risk.kill_switch import (
    KillSwitch,
)

kill_switch = (
    KillSwitch(
        max_drawdown=0.10,

        max_daily_loss=0.05,
    )
)


async def evaluate_runtime_risk():

    current_drawdown = 0.03

    daily_loss = 0.02

    status = (
        kill_switch.evaluate_risk(
            current_drawdown=
            current_drawdown,

            daily_loss=
            daily_loss,
        )
    )

    print(
        "RISK STATUS"
    )

    print(status)

    return status