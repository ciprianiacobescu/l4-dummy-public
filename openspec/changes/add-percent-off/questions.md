# Questions — add-percent-off

<!-- l4:questions v1
How to answer: write under "### Answer" and set **Status** to `answered`.
To accept the clarifier's suggestion as-is, set **Status** to `accepted`.
Status values: open · answered · accepted · answered-by-clarifier · dismissed · superseded
Kind values: technical · product · ambiguous · verdict. For a `verdict` question, start the answer with `accept` or
`reject`, then give your reason.
Do not change question IDs. Commit and push to the l4/… branch to resume the run. -->

<!-- l4:index:start -->
| ID | Status | Blocking | Kind | Question |
|----|--------|----------|------|----------|
| Q-001 | open | none | verdict | Criterion C-cc44872e (discount › Percent off in cents › Everything off): accept as satisfied? |
<!-- l4:index:end -->

---

## Q-001: Criterion C-cc44872e (discount › Percent off in cents › Everything off): accept as satisfied?

- **Status:** open
- **Blocking tasks:** none
- **Kind:** verdict
- **Asked:** round 2, verifier
- **Criteria:** C-cc44872e (discount › Percent off in cents › Everything off)

### Context
Criterion C-cc44872e (discount › Percent off in cents › Everything off) is needs human after round 2.

Scenario:
\- **WHEN** a promotion asks for `pricing.discount.percent_off(250, 100)`
\- **THEN** it returns exactly `250`

Why: uncovered: no adequate discriminating test traces it
Judge: pass
Tracing tests: none
Ignored tests: none

Answer `accept` if the criterion is satisfied as it stands, or `reject` and say why.
If the code is right and the scenarios are incomplete, `reject` with a scenario: WHEN ... THEN ...

### Options
1. accept
2. reject: <reason>, or WHEN ... THEN ... for a spec gap

### Answer
<!-- write below this line -->
