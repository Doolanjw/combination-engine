# Prompt Library

Five structured prompts — one for each step of the Combination Engine method.

Use them in sequence for a full search session, or jump to any individual step.

| Step | Prompt | Purpose |
|------|--------|---------|
| 1 | [Friction Point](./01-friction-point.md) | Extract a precise, falsifiable problem statement |
| 2 | [Contradiction](./02-contradiction.md) | Name the structural tension inside the problem |
| 3 | [Cross-Domain Search](./03-cross-domain-search.md) | Find analogous solutions across industries |
| 4 | [Expired Patents](./04-expired-patents.md) | Surface dormant ideas that current conditions may make viable |
| 5 | [Filter](./05-filter.md) | Kill weak candidates fast |

## How to Use

**In sequence:** Run Steps 1–5 as a complete session. Carry the output of each step as the input to the next.

**Selectively:** If you already have a well-formed friction point, skip to Step 2. If you have candidate mechanisms and need to evaluate them, jump to Step 5.

**With the CLI:** The [`tools/combination_engine.py`](../tools/combination_engine.py) script runs these prompts interactively and optionally calls the Anthropic API automatically.

## Tips

- Spend more time on Steps 1 and 2 than feels comfortable. A vague friction point produces vague candidates.
- Step 3 output is hypotheses, not answers. Treat every analogy as something to verify.
- Step 5 is meant to be brutal. Most candidates should fail.
