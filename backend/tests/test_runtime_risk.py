import asyncio

from src.runtime.handlers.risk_handler import (
    evaluate_runtime_risk,
)


async def main():

    status = (
        await evaluate_runtime_risk()
    )

    print()

    print(
        "FINAL STATUS"
    )

    print(status)


asyncio.run(main())