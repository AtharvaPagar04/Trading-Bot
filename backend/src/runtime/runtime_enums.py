from enum import Enum


class RuntimeMode(str, Enum):
    DRY_RUN = "dry_run"
    PAPER = "paper"
    LIVE = "live"


class RuntimeStatus(str, Enum):
    STARTING = "starting"
    RUNNING = "running"
    PAUSED = "paused"
    SAFE_MODE = "safe_mode"
    COOLDOWN = "cooldown"
    EMERGENCY_STOP = "emergency_stop"
    SHUTDOWN = "shutdown"
    


class EmergencyReason(str, Enum):
    HEARTBEAT_FAILURE = "heartbeat_failure"
    MAX_DRAWDOWN = "max_drawdown"
    ATR_SPIKE = "atr_spike"
    POSITION_MISMATCH = "position_mismatch"
    MANUAL_STOP = "manual_stop"
    TRANSPORT_FAILURE = (
        "TRANSPORT_FAILURE"
    )
   