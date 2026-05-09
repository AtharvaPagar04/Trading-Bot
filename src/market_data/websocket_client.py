from src.market_data.market_data_router import (
    MarketDataRouter,
)
from datetime import datetime
from src.market_data.market_tick import (
    MarketTick,
)
from src.runtime.runtime_enums import (
    EmergencyReason,
)
class WebSocketClient:

    def __init__(
        self,
        router: MarketDataRouter,
        
    ):

        self.router = router

        self.connected = False
        self.reconnect_attempts = 0
        self.max_reconnect_attempts = 5

    def connect(self):

        self.connected = True

    def disconnect(self):

        self.connected = False
    def receive_tick(
        self,
        symbol: str,
        price: float,
        exchange: str,
    ):

        tick = MarketTick(
            symbol=symbol,
            price=price,
            timestamp=datetime.utcnow(),
            exchange=exchange,
        )

        self.router.route_tick(
            tick
        )
    def reconnect(self):

        if (
            self.reconnect_attempts
            >=
            self.max_reconnect_attempts
        ):

            self.router.runtime.emergency_stop(
                EmergencyReason.HEARTBEAT_FAILURE
            )

            return False

        self.reconnect_attempts += 1

        self.connect()

        return True