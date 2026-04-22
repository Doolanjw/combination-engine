# Clinic Waiting Room — Full Five-Step Walkthrough

**Core transfer:** Queue psychology from theme parks, airports, and restaurants → outpatient clinic experience  
**Steps illustrated:** All five steps, end-to-end

This is the worked example from Appendix A of the manuscript, expanded into a full framework walkthrough. It is a good starting point if the method is new to you — the problem is concrete, the analogy set is accessible, and the filtering logic is easy to follow.

---

## Step 1: Define the Friction Point

**Raw input:** "Patients are frustrated while waiting in clinics."

**Refined friction point:**
> Patients wait 15–30 minutes after clinic check-in with no visible progress indicator, producing measurable anxiety even when total wait time is clinically acceptable.

**What this friction point is NOT:**
- Not about reducing actual wait time (a separate, harder problem involving scheduling and staffing)
- Not about general patient satisfaction scores
- Not about clinical outcomes or care quality
- Not about scheduling efficiency

**Why the refinement matters:** Separating "wait time" from "wait experience" opens a much larger solution space. The actual duration may be fixed by clinical constraints. The perception of that duration is not.

---

## Step 2: State the Contradiction

- The clinic must avoid disclosing exact queue position — because communicating position creates patient gaming of the system and exposes scheduling complexity the clinic cannot commit to
- The clinic must reduce patient anxiety during the wait — because unmanaged anxiety reduces trust and satisfaction independent of clinical quality
- These conflict because the most direct anxiety reducer (knowing your position) is operationally problematic to provide accurately

**TRIZ parameter pair:** Reliability (27) vs. Loss of information (24) → candidate inventive principles: Preliminary action (10), Feedback (23), Intermediary (24)

---

## Step 3: Cross-Domain Search

**Prompt used:**
```
My contradiction: A service system must reduce customer anxiety during an uncertain
wait without revealing specific queue position, which would create gaming behavior
and operational complexity.

Ignore healthcare entirely. Find cases where this structural tension was resolved.
```

**Candidates returned:**

| Domain | Mechanism | Decade | Transferability |
|--------|-----------|--------|-----------------|
| Theme parks (Disney) | Psychological queue design: visible progress milestones, environmental engagement, "what's next" signaling without position disclosure. Reduces perceived wait by 15–30% without reducing actual wait. | 1970s–present | **High** — same structural problem, extensive validated research |
| Airports | Visual separation of queues by type creates perceived progress and status without disclosing global position | 2000s | **Medium** — requires operational redesign of physical space |
| Restaurants (pager systems) | Removes the customer from the queue environment entirely by changing where waiting happens | 1970s | **High** — direct mechanism; patients could wait elsewhere |
| Elevators (floor indicators) | Shows "elevator coming" signal without revealing exact position — manages uncertainty without commitment to precision | 1980s | **Medium** — mechanism is transferable; context differs |
| Call centers (estimated wait messaging) | Provides a probabilistic range rather than a precise number, managing expectations without commitment | 1990s | **High** — low cost to implement, directly analogous |

**Highest-transferability mechanism:** Disney's queue psychology research. Core finding: perceived wait is more important than actual wait. Progress visibility, environmental engagement, and milestone signaling reduce perceived wait time without reducing actual wait time. Decades of validated operational data across multiple venues and cultures.

---

## Step 4: Mine Expired Patents

**Prompt used:**
```
My friction point: Patients perceive waits as longer than they are when given no
progress signal in clinic environments.

Search for expired patents related to: queue management, wait perception, psychological
queue design, waiting room experience, estimated wait time communication systems.
```

**Candidates returned:**

**1. Psychological queue segmentation (1980s, entertainment venues)**
Mechanism: Creating visible sub-queues — "zones" or checkpoints — that patients pass through, giving a sense of forward progress without disclosing global queue position.
- Why it stalled: Designed for large-footprint theme park architecture; not adaptable to small clinic spaces.
- What changed: Digital displays and signage enable virtual segmentation without physical redesign. A screen can create a "checkpoint" without a structural zone.

**2. Probabilistic wait estimation (1990s, telephony)**
Mechanism: Using rolling-average queue data to communicate a range ("approximately 10–20 minutes") rather than an exact position or time.
- Why it stalled: Computational overhead was non-trivial in early telephony infrastructure.
- What changed: Trivial to compute from EMR scheduling data; implementable via SMS or waiting room display at near-zero marginal cost.

**3. Engagement-diversion systems (1970s, bank queuing)**
Mechanism: Installing information displays, news content, or entertainment in queuing environments to redirect attention away from the wait.
- Why it stalled: Content management required manual updates; expensive for small deployments.
- What changed: Managed digital display content is now commodity infrastructure. A clinic can subscribe to a content management system for less than the cost of one staff hour per week.

---

## Step 5: Filter Hard

**Candidates entering filter:**
1. Milestone display (virtual queue zones via digital screen)
2. Probabilistic wait range communication (SMS or display)
3. Engagement-diversion display (managed content screens)

| Candidate | Physics | Regulatory | Economics | Moat | Dependencies | Result |
|-----------|:-------:|:----------:|:---------:|:----:|:------------:|--------|
| Milestone display | Pass | Pass | Pass (~$300–600/display) | Fail | Pass | **Survives** |
| Probabilistic wait SMS | Pass | Pass | Pass (near-zero marginal cost) | Fail | Medium (needs EMR queue access) | **Survives** |
| Engagement diversion | Pass | Pass | Pass | Fail | Pass | **Survives** |

**On the moat failures:** None of these mechanisms has a durable IP moat — they are well-known techniques with prior art. This is not a stop signal; it changes the business model implication. These are execution plays, not technology plays. A clinic group that deploys broadly before competitors builds a patient experience advantage through brand and operational consistency, not exclusivity.

**On the keystone dependency flag (SMS):** Requires access to EMR queue data via API. If the EMR vendor restricts that access, the mechanism breaks. Worth verifying before committing to implementation.

---

## Surviving Candidates

Two mechanisms pass all five tests without qualification:

**Milestone display** — Adapts Disney's queue psychology research to a clinical footprint via digital screens. No new technology required. Implementable in days. Evidence base is robust. No moat, so move fast.

**Engagement diversion** — Commodity infrastructure. No friction points. Deploy as a baseline alongside whichever primary intervention is chosen.

**Probabilistic wait SMS** — High value if EMR API access is confirmed. Verify the keystone dependency before committing.

---

## What This Example Illustrates

**The method is not about finding inventions — it is about finding better starting points.** None of the surviving candidates is a novel invention. All three are cross-domain imports with clear prior art. The value is in knowing they exist, knowing they have been validated in adjacent contexts, and deploying them before competitors think to look.

**Failing the moat test is information, not a stop sign.** Knowing early that the moat is absent means you build your strategy around speed and distribution rather than IP protection.

**AI and the Combination Engine are front-of-pipeline tools.** These candidates still require implementation, staff training, patient testing, and iteration. The engine narrows the space of what to test. It does not replace the testing.
