# The Combination Engine

> Most innovation is recombination, not invention from scratch. The barrier is not a shortage of ideas — it is a shortage of visibility across domains.

Bernard Sadow spent forty years watching people carry heavy luggage before attaching wheels to a suitcase in 1970. The wheel had existed for five thousand years. So had the suitcase. The gap was not technology. It was a failure to see two existing things together.

This repository is the companion to *The Combination Engine* — a manuscript on using AI and the public patent record to find non-obvious innovation opportunities: combinations of existing solutions that no one has yet connected.

---

## What's Here

| Directory | Contents |
|-----------|----------|
| [`manuscript/`](./manuscript/) | Full manuscript — patents, AI, and combinatorial innovation |
| [`prompts/`](./prompts/) | Five-step prompt library for structured cross-domain patent search |
| [`examples/`](./examples/) | Worked case studies applying the framework end-to-end |
| [`tools/`](./tools/) | Python CLI that walks through the five-step method |

---

## The Five-Step Method

The Combination Engine is a method, not a product:

1. **Define the friction point** — one sentence, no buzzwords, no solution embedded in the problem
2. **State the contradiction** — what two things must simultaneously be true for the problem to be solved, but currently cannot be
3. **Search across domains** — who else resolved this structural tension, under what vocabulary, in what decade
4. **Mine expired patents** — what was tried before that current conditions might now make viable
5. **Filter hard** — what would kill any candidate solution quickly

AI handles search breadth. You handle judgment.

---

## Quick Start

### Use the prompts directly

Copy any prompt from [`prompts/`](./prompts/) into ChatGPT, Claude, or any capable LLM. The prompts are designed to work with the public-facing version of any model.

### Run the CLI tool

```bash
pip install -r tools/requirements.txt
python tools/combination_engine.py
```

Single step:

```bash
python tools/combination_engine.py \
  --step friction \
  --input "field sensors drain batteries in 6 months but need 5-year deployment" \
  --domain "industrial IoT"
```

With Anthropic API (optional — the tool works without it):

```bash
export ANTHROPIC_API_KEY=your_key_here
python tools/combination_engine.py --auto --output session.json
```

---

## Read the Examples First

If the method is new to you, start with the examples before the prompts:

- [Bullet Train / Kingfisher](./examples/bullet-train-kingfisher.md) — geometry transfer from a diving bird to rail infrastructure
- [Halicin / Antibiotic Discovery](./examples/halicin-antibiotic.md) — AI-assisted cross-domain compound reassignment
- [Clinic Waiting Room](./examples/clinic-waiting-room.md) — full five-step walkthrough from problem to filtered candidates

---

## The Manuscript

*The Combination Engine* covers:

- The combinatorial nature of innovation, and why the lone-genius story is misleading
- How patent documents work — anatomy, classifications, and why patents beat academic papers for cross-domain search
- How AI reads the patent record — embeddings, semantic search, cross-domain matching, and what AI cannot do
- TRIZ: what Soviet patent examiner Genrich Altshuller discovered about recurring patterns inside invention
- Expired patents as public-domain opportunity — four conditions that make old ideas newly viable
- Three worked case studies across pharma, rail, and medical devices
- The tools available today (free and commercial), with honest assessments of each
- Where this goes next — the obviousness paradox under AI, democratization, and what remains irreducibly human

Full manuscript: [`manuscript/`](./manuscript/)

---

## Why This Matters

The USPTO has issued more than eleven million patents, with hundreds of thousands added annually. The most valuable combinations sit between fields — and partial visibility across those fields is not enough.

AI does not invent. It is a hypothesis machine: one that can search the archive more broadly and cross domains more systematically than any unaided human. The human driver's job is to recognize when an analogy is structural rather than verbal, test it against physics and economics, and decide which hypotheses deserve belief.

The people best positioned to benefit will not necessarily be the ones with the biggest budgets or the most sophisticated tools. They will be the ones who combine machine breadth with human depth.

---

*Jonathan Doolan, 2026*
