"""Stock helpers of the eval base project."""


def units_short(on_hand: int, wanted: int) -> int:
    """How many units are missing to serve `wanted` from `on_hand`."""
    return max(wanted - on_hand, 0)


def units_surplus(on_hand: int, wanted: int) -> int:
    """How many units are left over after serving `wanted` from `on_hand`."""
    if on_hand < 0 or wanted < 0:
        raise ValueError("on_hand and wanted must be non-negative")
    return max(on_hand - wanted, 0)
