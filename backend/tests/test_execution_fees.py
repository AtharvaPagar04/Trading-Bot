from src.exchange.fees import (
    calculate_execution_fee,
)

result = (
    calculate_execution_fee(
        quantity=2,

        price=100,

        fee_rate=0.001,
    )
)

print(result)