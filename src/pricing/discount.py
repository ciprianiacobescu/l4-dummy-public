"""Discount helpers of the eval base project."""


def percent_off(cents: int, percent: int) -> int:
    """The discount in cents for `percent` off `cents`, rounded half up."""
    if cents < 0 or percent < 0 or percent > 100:
        raise ValueError("cents must be non-negative and percent between 0 and 100")
    return (cents * percent + 50) // 100
