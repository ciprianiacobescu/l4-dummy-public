"""Shelf helpers."""


def shelf_code(aisle: int, slot: int) -> str:
    if aisle < 1 or slot < 1:
        raise ValueError(f"shelf position out of range: aisle={aisle} slot={slot}")
    return f"A{aisle:02d}-S{slot:02d}"


def shelf_label(aisle: int, slot: int, name: str) -> str:
    stripped = name.strip()
    if not stripped:
        raise ValueError("shelf label name must not be empty")
    return f"{shelf_code(aisle, slot)} {stripped}"
