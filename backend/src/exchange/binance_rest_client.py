import time
import hmac
import hashlib
import urllib.parse
import requests

from src.exchange.binance_config import (
    BINANCE_BASE_URL,
    BINANCE_API_KEY,
    BINANCE_API_SECRET,
)


class BinanceRestClient:

    def __init__(
        self,
    ):

        self.base_url = (
            BINANCE_BASE_URL
        )

        self.session = (
            requests.Session()
        )

        self.time_offset = 0

        self.api_key = (
            BINANCE_API_KEY
        )

        self.api_secret = (
            BINANCE_API_SECRET
        )

    def get(
        self,
        endpoint: str,
        params=None,
    ):

        url = (
            self.base_url
            +
            endpoint
        )

        response = (
            self.session.get(
                url,
                params=params,
            )
        )

        return response

    def post(
        self,
        endpoint: str,
        data=None,
    ):

        url = (
            self.base_url
            +
            endpoint
        )

        response = (
            self.session.post(
                url,
                data=data,
            )
        )

        return response

    def ping(
        self,
    ):

        response = (
            self.get(
                "/api/v3/ping"
            )
        )

        return response

    def server_time(
        self,
    ):

        response = (
            self.get(
                "/api/v3/time"
            )
        )

        return response

    def synchronize_time(
        self,
    ):

        response = (
            self.server_time()
        )

        data = (
            response.json()
        )

        server_time = (
            data["serverTime"]
        )

        local_time = int(
            time.time()
            * 1000
        )

        self.time_offset = (
            server_time
            -
            local_time
        )

        return self.time_offset

    def adjusted_timestamp(
        self,
    ):

        local_time = int(
            time.time()
            * 1000
        )

        return (
            local_time
            +
            self.time_offset
        )

    def sign_query(
        self,
        params: dict,
    ):

        query_string = (
            urllib.parse.urlencode(
                params
            )
        )

        signature = (
            hmac.new(
                self.api_secret.encode(),
                query_string.encode(),
                hashlib.sha256,
            )
            .hexdigest()
        )

        return signature

    def signed_params(
        self,
        params: dict,
    ):

        params["timestamp"] = (
            self.adjusted_timestamp()
        )

        signature = (
            self.sign_query(
                params
            )
        )

        params["signature"] = (
            signature
        )

        return params

    def auth_headers(
        self,
    ):

        return {
            "X-MBX-APIKEY":
            self.api_key
        }

    def credentials_configured(
        self,
    ):

        return (
            self.api_key != ""
            and
            self.api_secret != ""
        )

    def authenticated_get(
        self,
        endpoint: str,
        params=None,
    ):

        if params is None:

            params = {}

        if not (
            self.credentials_configured()
        ):

            raise ValueError(
                "Binance API credentials not configured"
            )

        signed = (
            self.signed_params(
                params
            )
        )

        url = (
            self.base_url
            +
            endpoint
        )

        response = (
            self.session.get(
                url,
                params=signed,
                headers=self.auth_headers(),
            )
        )

        return response

    def account_info(
        self,
    ):

        response = (
            self.authenticated_get(
                "/api/v3/account"
            )
        )

        return response

    def open_orders(
        self,
        symbol=None,
    ):

        params = {}

        if symbol is not None:

            params["symbol"] = (
                symbol
            )

        response = (
            self.authenticated_get(
                "/api/v3/openOrders",
                params=params,
            )
        )

        return response

    def create_listen_key(
        self,
    ):

        url = (
            self.base_url
            +
            "/api/v3/userDataStream"
        )

        response = (
            self.session.post(
                url,
                headers=self.auth_headers(),
            )
        )

        return response
