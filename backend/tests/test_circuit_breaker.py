from src.risk.circuit_breaker import (
    CircuitBreaker,
)


def test_circuit_breaker():

    breaker = (
        CircuitBreaker(
            failure_limit=2
        )
    )

    breaker.record_failure()

    breaker.record_failure()

    assert (
        breaker.triggered()
        is True
    )
