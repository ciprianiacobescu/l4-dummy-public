# Requirements Document

## Introduction

Buyers want to know how many units are left over after an order is served. It depends on no other spec.

## Requirements

### Requirement 1: Surplus

**User Story:** As a buyer, I need the surplus after an order so that I do not reorder too early.

#### Acceptance Criteria

1. WHEN `on_hand` is 9 and `wanted` is 4, THEN the system SHALL return 5.

2. WHEN `wanted` is at least `on_hand` (e.g., 3 on hand and 4 wanted), THEN the system SHALL return 0.

### Requirement 2: Input Validation

**User Story:** As a buyer, I need invalid counts rejected so that the surplus is never wrong.

#### Acceptance Criteria

1. WHEN `on_hand` or `wanted` is negative, THEN the system SHALL raise `ValueError`.
