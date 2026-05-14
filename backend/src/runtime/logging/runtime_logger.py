from enum import Enum
from datetime import datetime


class LogLevel(str, Enum):

    DEBUG = "DEBUG"

    INFO = "INFO"

    WARNING = "WARNING"

    ERROR = "ERROR"

    CRITICAL = "CRITICAL"


class LogCategory(str, Enum):

    RUNTIME = "RUNTIME"
    ISOLATION = "ISOLATION"

    WEBSOCKET = "WEBSOCKET"

    STRATEGY = "STRATEGY"

    EXECUTION = "EXECUTION"

    PERSISTENCE = "PERSISTENCE"

    API = "API"

    ANALYTICS = "ANALYTICS"

    GOVERNANCE = "GOVERNANCE"


def runtime_log(
    level: LogLevel,
    category: LogCategory,
    message: str,
):

    timestamp = (
        datetime.utcnow()
        .isoformat()
    )

    print(
        f"[{timestamp}] "
        f"[{level}] "
        f"[{category}] "
        f"{message}"
    )