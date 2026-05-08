from datetime import datetime
from datetime import timedelta

from src.core.recovery_coordinator import (
    evaluate_coordinated_recovery,
)

from src.core.runtime_clearance import (
    clear_runtime_safe_mode,
)

from src.core.safe_mode import (
    apply_safe_mode,
)

from src.persistence.runtime_loader import (
    load_runtime_snapshot,
)

runtime = load_runtime_snapshot()

runtime = apply_safe_mode(
    runtime
)

cooldown_end = (
    datetime.utcnow()
    + timedelta(minutes=15)
)

result = (
    evaluate_coordinated_recovery(
        runtime=runtime,

        cooldown_end=
        cooldown_end,

        current_time=
        datetime.utcnow(),

        adx_value=18,

        atr_percent=1.5,

        stable_closes=2,
    )
)

print("COOLDOWN ACTIVE")
print(result)

runtime = clear_runtime_safe_mode(
    runtime
)

expired_cooldown = (
    datetime.utcnow()
    - timedelta(minutes=1)
)

result = (
    evaluate_coordinated_recovery(
        runtime=runtime,

        cooldown_end=
        expired_cooldown,

        current_time=
        datetime.utcnow(),

        adx_value=18,

        atr_percent=1.5,

        stable_closes=2,
    )
)

print("\nCOOLDOWN EXPIRED")
print(result)