from dataclasses import dataclass
from datetime import datetime


@dataclass
class PaperOrder:

    symbol: str

    side: str

    quantity: float

    price: float

    timestamp: datetime