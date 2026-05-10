import pytest

from src.exchange.binance_config import (
    BINANCE_API_KEY,
    BINANCE_API_SECRET,
)

from src.exchange.binance_rest_client import (
    BinanceRestClient,
)


def test_balance_structure():

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

    data = response.json()

    balances = (
        data["balances"]
    )

    assert isinstance(
        balances,
        list,
    )
