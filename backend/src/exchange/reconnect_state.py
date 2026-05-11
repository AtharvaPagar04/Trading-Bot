from dataclasses import (
    dataclass,
)


@dataclass
class ReconnectState:

    reconnect_attempts: int = 0

    reconnect_limit: int = 5

    connected: bool = False
