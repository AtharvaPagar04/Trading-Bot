import pytest

from src.exchange.binance_config import (
    BINANCE_API_KEY,
    BINANCE_API_SECRET,
)

from src.exchange.binance_rest_client import (
    BinanceRestClient,
)


def test_account_info():

    if (
        BINANCE_API_KEY == ""
        or
        BINANCE_API_SECRET == ""
    ):

        pytest.skip(
            "Binance API credentials not configured"
        )

    client = (
        BinanceRestClient()
    )

    client.synchronize_time()

    response = (
        client.account_info()
    )

    assert (
        response.status_code
        ==
        200
    )

    data = response.json()

    assert (
        "balances"
        in data
    )
