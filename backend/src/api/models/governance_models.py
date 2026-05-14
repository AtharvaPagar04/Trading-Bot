from pydantic import BaseModel
from typing import Optional

class RecoveryStatusResponse(BaseModel):
    recovery_allowed: bool
    reason: str
    emergency_reason: Optional[str] = None
    status: str

class GovernanceResponse(BaseModel):
    success: bool
    trading_enabled: Optional[bool] = None
    safe_mode: Optional[bool] = None
    status: Optional[str] = None
    message: Optional[str] = None
