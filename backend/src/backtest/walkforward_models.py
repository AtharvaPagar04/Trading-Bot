from dataclasses import dataclass


@dataclass
class WalkForwardWindow:

    train_start: int

    train_end: int

    test_start: int

    test_end: int