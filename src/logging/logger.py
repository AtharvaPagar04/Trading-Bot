import json
import logging
from datetime import datetime


class StructuredLogger:

    def __init__(
        self,
        name: str = "grid_trading_bot",
    ):

        self.logger = logging.getLogger(name)

        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:

            handler = logging.StreamHandler()

            formatter = logging.Formatter(
                "%(message)s"
            )

            handler.setFormatter(formatter)

            self.logger.addHandler(handler)

    def log_event(
        self,
        event_type: str,
        message: str,
        payload: dict | None = None,
    ):

        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": event_type,
            "message": message,
            "payload": payload or {},
        }

        self.logger.info(
            json.dumps(log_entry)
        )