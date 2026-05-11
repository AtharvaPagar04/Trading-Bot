from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class OrderSide(
    str,
    Enum,
):
    BUY = "BUY"

    SELL = "SELL"


class OrderStatus(
    str,
    Enum,
):
    PENDING = "PENDING"

    FILLED = "FILLED"

    CANCELLED = (
        "CANCELLED"
    )


@dataclass
class Order:
    order_id: str

    symbol: str

    side: OrderSide

    quantity: float

    price: float

    status: OrderStatus

    timestamp: datetime


@dataclass
class Position:
    symbol: str

    quantity: float

    average_price: float

@dataclass
class CompletedTrade:
    symbol: str

    quantity: float

    entry_price: float

    exit_price: float

    realized_pnl: float
    fees_paid: float
    opened_at: datetime

    closed_at: datetime

@dataclass
class Balance:
    total_capital: float

    available_capital: float