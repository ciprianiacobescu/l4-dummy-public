"""In-memory stock ledger."""


class StockLedger:
    def __init__(self) -> None:
        self._counts: dict[str, int] = {}

    def receive(self, sku: str, qty: int) -> None:
        if qty < 1:
            raise ValueError(f"quantity must be at least 1: {qty}")
        self._counts[sku] = self._counts.get(sku, 0) + qty

    def ship(self, sku: str, qty: int) -> None:
        if qty < 1:
            raise ValueError(f"quantity must be at least 1: {qty}")
        current = self._counts.get(sku, 0)
        if qty > current:
            raise ValueError(f"cannot ship {qty} of {sku}: {current} on hand")
        self._counts[sku] = current - qty

    def on_hand(self, sku: str) -> int:
        return self._counts.get(sku, 0)
