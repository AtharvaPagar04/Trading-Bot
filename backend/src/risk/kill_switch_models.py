from dataclasses import dataclass


@dataclass
class KillSwitchStatus:

    trading_allowed: bool

    trigger_reason: str

    current_drawdown: float

    daily_loss: float