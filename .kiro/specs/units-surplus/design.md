# Design Document

## Overview

A new function in the existing module `src/inventory/stock.py`, next to `units_short`.

## Components and Interfaces

### `src/inventory/stock.py`

**Function:** `units_surplus(on_hand: int, wanted: int) -> int`

- Returns `max(on_hand - wanted, 0)`.
- Raises `ValueError` when either argument is negative.

## Testing Strategy

Unit tests in `tests/test_surplus.py`, one per acceptance criterion.
