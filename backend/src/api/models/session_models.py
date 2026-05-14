from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SessionResponse(BaseModel):
    session_active: bool
    active_session_id: Optional[int]
    session_started_at: Optional[datetime]
    session_duration_seconds: int
    session_pnl: float
    total_trades: int
    status: str
