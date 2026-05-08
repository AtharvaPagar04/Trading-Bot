from src.risk.kill_switch import (
    KillSwitch,
)

kill_switch = (
    KillSwitch(
        max_drawdown=0.10,

        max_daily_loss=0.05,
    )
)

safe_status = (
    kill_switch.evaluate_risk(
        current_drawdown=0.03,

        daily_loss=0.02,
    )
)

print("SAFE STATUS")

print(safe_status)

print()

danger_status = (
    kill_switch.evaluate_risk(
        current_drawdown=0.15,

        daily_loss=0.02,
    )
)

print("DANGER STATUS")

print(danger_status)