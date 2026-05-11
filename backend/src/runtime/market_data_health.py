from dataclasses import dataclass
from datetime import datetime
from datetime import timedelta


MARKET_DATA_TIMEOUT_SECONDS = 15


@dataclass
class MarketDataHealth:

    last_update: datetime

    def update(self):

        self.last_update = (
            datetime.utcnow()
        )

    def is_stale(self) -> bool:

        threshold = (
            self.last_update
            +
            timedelta(
                seconds=
                MARKET_DATA_TIMEOUT_SECONDS
            )
        )

        return (
            datetime.utcnow()
            >
            threshold
        )