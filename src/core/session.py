from dataclasses import dataclass
from datetime import datetime


@dataclass
class TradingSession:
    session_id: str

    start_time: datetime

    starting_capital: float
    current_capital: float

    session_pnl_percent: float

    peak_pnl_percent: float

    entries_enabled: bool