# Step 2: State the Contradiction

TRIZ's core insight: most hard engineering problems are hidden contradictions — two properties that must simultaneously be true, but cannot be under current constraints. Naming the contradiction precisely narrows the search to patents that resolved the same structural tension.

---

## Prompt Template

```
My friction point is: [PASTE OUTPUT FROM STEP 1]

Help me identify the core contradiction: what two things must simultaneously be
true for this problem to be solved, but cannot both be true given current constraints?

Format it as:
- The system must be [PROPERTY A] — because [REASON]
- The system must also be [PROPERTY B] — because [REASON]
- These conflict because [WHY THEY CANNOT BOTH BE TRUE TODAY]

Then identify which TRIZ engineering parameters this maps to. List the top 2–3
candidate parameter pairs and the inventive principles associated with them.
```

---

## Why This Step Matters

Most people frame hard problems as tradeoffs and accept them. TRIZ begins from a more demanding assumption: many tradeoffs are not real constraints — they are signs the problem has been framed too narrowly.

The useful shift is from "Which side of the tradeoff should I accept?" to "How have other inventors resolved contradictions like this without accepting the tradeoff?"

---

## Example

**Friction point:** Field sensors must transmit data frequently but cannot carry a large battery.

**Contradiction:**
- The system must transmit frequently — because the application requires near-real-time monitoring
- The system must also use minimal power — because it runs on a coin cell for five years
- These conflict because transmission frequency and power draw scale together under conventional radio protocols

**TRIZ parameter pair:** Speed (9) vs. Reliability (27) → inventive principles: Parameter change (35), Preliminary action (10), Extraction (2), Partial action (16)

---

## TRIZ Parameter Reference (Selected)

| # | Parameter | # | Parameter |
|---|-----------|---|-----------|
| 1 | Weight of moving object | 21 | Power |
| 3 | Length of moving object | 23 | Loss of substance |
| 9 | Speed | 27 | Reliability |
| 10 | Force | 33 | Adaptability |
| 12 | Shape | 36 | Device complexity |
| 13 | Stability | 39 | Productivity |

Full contradiction matrix and 40 inventive principles: [triz-journal.com](https://triz-journal.com/)
