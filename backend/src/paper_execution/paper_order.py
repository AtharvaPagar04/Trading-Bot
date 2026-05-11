from dataclasses import dataclass
from datetime import datetime
from src.paper_execution.order_status import (
    OrderStatus,
)
from typing import Optional
@dataclass
class PaperOrder:

    symbol: str

    side: str

    quantity: float

    price: float

    timestamp: datetime
    
    status: OrderStatus = (
        OrderStatus.PENDING
    )
    filled_quantity: float = 0.0
    eligible_execution_time: (
        Optional[datetime]
    ) = None
    expiration_time: (
        Optional[datetime]
    ) = None