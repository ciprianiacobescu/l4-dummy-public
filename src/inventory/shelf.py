"""Shelf helpers."""


def shelf_code(aisle: int, slot: int) -> str:
    if aisle < 1 or slot < 1:
        raise ValueError(f"shelf position out of range: aisle={aisle} slot={slot}")
    return f"A{aisle:02d}-S{slot:02d}"
