from dataclasses import dataclass


@dataclass
class PaperPosition:

    symbol: str

    quantity: float = 0.0

    average_entry_price: float = 0.0