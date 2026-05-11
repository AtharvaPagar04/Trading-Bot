from src.exchange.dynamic_scaling import (
    apply_confidence_scaling,
)

result = (
    apply_confidence_scaling(
        quantity=10,

        confidence_multiplier=0.4,
    )
)

print(result)