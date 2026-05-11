import json

import websocket


class BinanceUserStream:

    def __init__(
        self,
        listen_key: str,
    ):

        self.listen_key = (
            listen_key
        )

        self.base_url = (
            "wss://stream.binance.com:9443/ws/"
        )

        self.ws = None

    def stream_url(
        self,
    ):

        return (
            self.base_url
            +
            self.listen_key
        )

    def connect(
        self,
    ):

        self.ws = websocket.WebSocketApp(
            self.stream_url(),
        )

        return self.ws
