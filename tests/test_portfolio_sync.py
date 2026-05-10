from src.exchange.binance_portfolio_sync import (
    synchronize_portfolio,
)


class MockResponse:

    def json(
        self,
    ):

        return {
            "balances": [
                {
                    "asset": "USDT",
                    "free": "500",
                    "locked": "0",
                }
            ]
        }


class MockRestClient:

    def account_info(
        self,
    ):

        return MockResponse()


def test_portfolio_sync():

    balances = (
        synchronize_portfolio(
            MockRestClient()
        )
    )

    assert (
        balances["USDT"]["free"]
        ==
        500.0
    )
