class OrderDeduplicator:

    def __init__(
        self,
    ):

        self.order_ids = set()

    def is_duplicate(
        self,
        order_id: str,
    ):

        if (
            order_id
            in self.order_ids
        ):

            return True

        self.order_ids.add(
            order_id
        )

        return False
