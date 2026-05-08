from dataclasses import dataclass


@dataclass
class CapitalApproval:

    approved: bool

    approved_quantity: float

    required_cash: float

    available_cash: float

    rejection_reason: str | None