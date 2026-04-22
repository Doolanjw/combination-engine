# Step 3: Cross-Domain Search

The combination insight rarely comes from your own field. This prompt surfaces how adjacent — and distant — domains resolved the same structural contradiction. The output is a set of candidate analogies, not answers.

---

## Prompt Template

```
My contradiction is: [PASTE OUTPUT FROM STEP 2]

Ignore my specific domain ([DOMAIN]) entirely.

Search your knowledge of patents, engineering history, and product development
across all other fields for cases where this same structural tension was resolved —
where [PROPERTY A] and [PROPERTY B] were made to coexist without accepting the tradeoff.

For each example:
1. Name the domain and approximate decade
2. Describe how the contradiction was resolved (the mechanism, not the product name)
3. Identify what enabling condition made the solution possible
4. Rate transferability to my domain: High / Medium / Low, with one sentence of reasoning

Return 5–8 examples. Prioritize diversity of domain over completeness of any single example.
```

---

## Follow-Up Prompt

Once you have candidates:

```
From the list above, take the [2–3] highest-transferability examples. For each one,
describe what a literal transplant into [MY DOMAIN] would look like — not a metaphor,
but an actual mechanism. What would change? What would break? What assumptions
would I be importing from the source domain?
```

---

## Key Principles

**Ask by mechanism, not by industry.** Don't say "find me medical devices." Say "find cases where intermittent transmission replaced continuous monitoring."

**Transfer does not require identity.** A kingfisher is not a bullet train. Water entry is not tunnel pressure. The useful question is not "What object is the same as mine?" but "Who else resolved this kind of structural tension under different conditions?"

**Look for the enabling condition.** Solutions from other fields usually became possible when a material, process, or regulation changed. That enabling condition may now exist in your domain.

**Treat all output as hypotheses.** A semantic relationship in language is not the same as a workable combination in the physical world. Every candidate from this step requires verification against physics, economics, and regulation.
