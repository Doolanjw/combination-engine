# Step 5: Filter Hard

Most candidates fail. The point of filtering is to kill weak ideas fast so you invest only in viable ones. This step is meant to be brutal — a short list is the goal.

---

## Prompt Template

```
I have the following candidate mechanisms for solving [FRICTION POINT FROM STEP 1]:

[LIST CANDIDATES FROM STEPS 3 AND 4 — one short paragraph per candidate describing
the mechanism and its source domain]

Apply the following kill tests to each, in order. Stop at first failure.

Kill test 1 — Physics: Does this mechanism violate any physical constraint in my
application environment? (Temperature range, scale, energy budget, latency, material tolerance)

Kill test 2 — Regulatory: Does applying this mechanism trigger any regulatory regime
that would make deployment prohibitively slow or costly in [DOMAIN / GEOGRAPHY]?

Kill test 3 — Economics: Even if it works technically, do the unit economics make sense
at realistic scale? What does the mechanism cost to implement, and what is the value delivered?

Kill test 4 — Moat: If this works, how long before a well-resourced competitor reproduces it?
Is there anything durable here, or is this a speed/distribution play?

Kill test 5 — Keystone dependency: Does this mechanism depend on a single supplier, API,
regulation, or material that could be withdrawn or changed?

For each candidate: Pass or Fail at each test, with one sentence stating the reason
for any failure. Return only the candidates that pass all five tests, each with a
one-paragraph synthesis of what makes it defensible.
```

---

## Notes on Filtering

**Physics first, always.** Regulatory and economic objections can sometimes be engineered around. Physics cannot.

**Be honest about the moat.** Most mechanisms have no durable moat. That does not make them worthless — it means you need a speed, distribution, or data advantage rather than a technology one. Knowing this early is valuable.

**A short list is the goal.** If five candidates survive, something went wrong in Step 3. One or two survivors is a success.

**Dead candidates are still useful.** Knowing why an idea fails — and at which test — sharpens the search frame for the next round.

---

## After Filtering

Surviving candidates are hypotheses, not inventions. The next step is the cheapest experiment that could confirm or falsify the mechanism in your specific context.

The Combination Engine surfaces candidates. It does not validate them.
