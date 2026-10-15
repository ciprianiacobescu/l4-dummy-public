# Verification: kiro:invoice-line: PASS (round 1)

traceability: 9/9 criteria covered by a discriminating test

- Base: `41c545e6f8c296d6e6486169af3bd9209882dfe6`
- Head: `bda2461c1c7951f2256c1a0a246fd51e0747a014`
- Implementer profiles: deepseek
- Judge: claude-judge (claude-sonnet-5-5), 1 call(s), prompt sha256 `ab4ddafd573d2b25f30fcc08e01b23bf2892137a7050282f42975e7423a9c36d`
- Judge replies of claude-judge (this unit, all rounds): valid 1, repaired 0, retried 0, discarded 0; this round: valid
- independence: declared (unverified): claude-judge anthropic (served claude-sonnet-5-5), deepseek deepseek (declared)
- Cost: $0.0517

## Ladder

| Step | Name | Status | Seconds | Note |
|---|---|---|---|---|
| 0 | preconditions | ok | 0.0 | base l4/main@41c545e6f8 contained |
| 1 | integrity | ok | 0.1 | 7 sub-checks; scope: 4 changed file(s) |
| 2 | build | ok | 0.1 |  |
| 3 | tests | ok | 0.3 |  |
| 4 | traceability | ok | 0.0 | 9/9 criteria covered |
| 4a | audit sampling | not_run | 0.0 | roles.verifier_agent is empty |
| 5 | ui test generation | not_run | 0.0 | verifier.playwright.enabled is off |
| 6 | quality | ok | 0.0 | diff coverage not measured: coverage.py is not importable in the project environment |
| 8 | s1 judge | not_run | 0.0 | roles.s1_judge is empty |
| 9 | judge | ok | 9.1 | 1 call(s) |
| 10 | aggregation | ok | 0.0 | PASS |

## Gates

| Gate | Status | Command | Log |
|---|---|---|---|
| setup | pass | `uv sync --frozen` | .l4-out/gates/r-20261015T0546Z-d8a7/021-setup.log |
| test | pass | `.venv/bin/python -m pytest --junitxml=.l4-out/junit.xml` | .l4-out/gates/r-20261015T0546Z-d8a7/022-test.log |

## Integrity

| Check | Status | Note |
|---|---|---|
| protected paths | ok | no protected path differs from the base |
| pre-existing tests | ok | 1 test file(s) compared with the base |
| red-green freeze | ok | 1 task(s): red and green compared |
| test path freeze | ok | 1 harness step commit(s) checked |
| content scan | ok | no result-manipulating construct in the changed support and runner files |
| suppressions | skipped | no new suppression comment |
| tdd history | ok | 3 task(s); red tests passing at head: step 3 |

## Traceability

| Id | Criterion | State | Tests (status, proof) | Not evidence |
|---|---|---|---|---|
| C-47c7a274 | Req 1.1 | covered | tests.test_invoice::test_invoice_line_leaves_ledger_unchanged (passed, zero_value); tests.test_invoice::test_invoice_line_three_units_amounts (passed, zero_value) | - |
| C-bd29d7e5 | Req 1.2 | covered | tests.test_invoice::test_invoice_line_vat_rounds_half_up (passed, zero_value) | - |
| C-4c441964 | Req 1.3 | covered | tests.test_invoice::test_invoice_line_leaves_ledger_unchanged (passed, zero_value) | - |
| C-1a62d66b | Req 2.1 | covered | tests.test_invoice::test_invoice_line_rejects_qty_above_on_hand (passed, pre_satisfied) | - |
| C-a2d99d30 | Req 2.2 | covered | tests.test_invoice::test_invoice_line_accepts_qty_equal_to_on_hand (passed, pre_satisfied) | - |
| C-b100e3f9 | Req 2.3 | covered | tests.test_invoice::test_invoice_line_rejects_sku_never_received (passed, pre_satisfied) | - |
| C-d55dc7c2 | Req 3.1 | covered | tests.test_invoice::test_invoice_line_rejects_qty_below_one_before_stock_check (passed, pre_satisfied) | - |
| C-58ea14ea | Req 3.2 | covered | tests.test_invoice::test_invoice_line_rejects_negative_price_before_stock_check (passed, pre_satisfied) | - |
| C-d7631753 | Req 3.3 | covered | tests.test_invoice::test_invoice_line_passes_negative_rate_vat_error_through_unchanged (passed, pre_satisfied) | - |

## Evidence

### Needs attention

- diff coverage not measured: coverage.py is not importable in the project environment

### Files

| Path | Module | Label | Why |
|---|---|---|---|
| `.kiro/specs/invoice-line/.l4/ledger/r-20261015T0546Z-d8a7.jsonl` |  | none | exempt: harness, spec or documentation path |
| `.kiro/specs/invoice-line/tasks.md` |  | none | exempt: harness, spec or documentation path |
| `src/billing/invoice.py` | billing | relevant | named in the spec |
| `tests/test_invoice.py` |  | relevant | new test file |

### Changed functions

Diff coverage not measured: coverage.py is not importable in the project environment

### Tests

45 of 45 passed, 0 failed, 0 errored, 0 skipped.
9 of 9 new tests passed.

## Criteria

| Id | Criterion | Judge | Result | Reason |
|---|---|---|---|---|
| C-47c7a274 | Req 1.1 | pass | pass | the judge passed it and a discriminating test passes |
| C-bd29d7e5 | Req 1.2 | pass | pass | the judge passed it and a discriminating test passes |
| C-4c441964 | Req 1.3 | pass | pass | the judge passed it and a discriminating test passes |
| C-1a62d66b | Req 2.1 | pass | pass | the judge passed it and a discriminating test passes |
| C-a2d99d30 | Req 2.2 | pass | pass | the judge passed it and a discriminating test passes |
| C-b100e3f9 | Req 2.3 | pass | pass | the judge passed it and a discriminating test passes |
| C-d55dc7c2 | Req 3.1 | pass | pass | the judge passed it and a discriminating test passes |
| C-58ea14ea | Req 3.2 | pass | pass | the judge passed it and a discriminating test passes |
| C-d7631753 | Req 3.3 | pass | pass | the judge passed it and a discriminating test passes |

## Findings

- [minor, judge] Order of qty vs price checks when both invalid unpinned (spec gap) (criterion C-58ea14ea): Both qty<1 and negative price invalid: both raise ValueError, so only message differs.

## New tests (red then green, `task.red_ok` in the ledger)

- `tests.test_invoice::test_invoice_line_accepts_qty_equal_to_on_hand` (task 2.1): passed
- `tests.test_invoice::test_invoice_line_leaves_ledger_unchanged` (task 1.1): passed
- `tests.test_invoice::test_invoice_line_passes_negative_rate_vat_error_through_unchanged` (task 3.1): passed
- `tests.test_invoice::test_invoice_line_rejects_negative_price_before_stock_check` (task 3.1): passed
- `tests.test_invoice::test_invoice_line_rejects_qty_above_on_hand` (task 2.1): passed
- `tests.test_invoice::test_invoice_line_rejects_qty_below_one_before_stock_check` (task 3.1): passed
- `tests.test_invoice::test_invoice_line_rejects_sku_never_received` (task 2.1): passed
- `tests.test_invoice::test_invoice_line_three_units_amounts` (task 1.1): passed
- `tests.test_invoice::test_invoice_line_vat_rounds_half_up` (task 1.1): passed
