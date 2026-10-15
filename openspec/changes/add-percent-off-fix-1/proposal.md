# Proposal: fix 1 for add-percent-off

## Why
The verifier found problems in `add-percent-off` that this change fixes. The findings are listed below with their ids; each task of this change names the ones it answers.

## What Changes
- F-a2855589 (major): Criterion discount › Percent off in cents › Everything off fails: Decided by human in Q-001: the code is right, but no test traces this criterion. Add a test that asserts `pricing.discount.percent_off(250, 100) == 250`.. rejected by human: the code is right, but no test traces this criterion. Add a test that asserts `pricing.discount.percent_off(250, 100) == 250`.

## Impact
The code and the tests of `add-percent-off`.
