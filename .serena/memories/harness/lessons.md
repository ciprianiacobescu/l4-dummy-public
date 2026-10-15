<!-- l4:lessons v1 — harness-owned; propose changes via .serena/memories/inbox/ -->

## L-8d816d0e · Recurring red failure: vacuous
- **Source:** l4 kg propose 2026-10-14: n = 2 units, n = 5 attempts
- **Dedupe key:** kg-a-vacuous
- **Reinforced:** 1 · 2026-10-15
The task attempt failure "vacuous" was recorded in 2 separate units, 5 times in all.

In the red phase, each criterion needs a new test that fails by assertion when the stubbed function returns its zero value (0, False, "", None, an empty list). Assert on the returned value with an exact expected value. When the expected answer equals the zero value, add a case whose expected answer differs from it. For an object, assert `result is not None` first, then its attributes. A test that only raises an error (TypeError, AttributeError on None) or only checks that nothing is raised does not count.
