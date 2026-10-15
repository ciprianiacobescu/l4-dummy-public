"""Stock helpers of the eval base project."""


def units_short(on_hand: int, wanted: int) -> int:
    """How many units are missing to serve `wanted` from `on_hand`."""
    return max(wanted - on_hand, 0)


def units_surplus(on_hand: int, wanted: int) -> int:
    """How many units are left over after serving `wanted` from `on_hand`."""
    raise NotImplementedError
