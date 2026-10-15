"""In-memory stock ledger."""


class StockLedger:
    def receive(self, sku: str, qty: int) -> None:
        raise NotImplementedError

    def ship(self, sku: str, qty: int) -> None:
        raise NotImplementedError

    def on_hand(self, sku: str) -> int:
        raise NotImplementedError
