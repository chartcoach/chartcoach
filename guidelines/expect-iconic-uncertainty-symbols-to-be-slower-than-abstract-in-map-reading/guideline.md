---
id: expect-iconic-uncertainty-symbols-to-be-slower-than-abstract-in-map-reading
title: Expect iconic uncertainty symbols to slow map-reading compared with abstract
  symbols
bibliography: references.bib
description: Iconic metaphoric uncertainty symbols can increase response time versus
  single-variable abstract symbols in both intuitiveness rating and aggregation tasks.
labels:
- chart:map
- task:compare
- visual:iconicity
- impact:speed
- data:uncertainty
- audience:expert
- complexity:advanced
---

## Prefer abstract uncertainty symbols when task speed matters in multi-symbol displays <!-- role: advice -->

When users must quickly scan or aggregate uncertainty across many points, prefer abstract symbols that vary a single visual variable over iconic metaphoric symbols.

## Why abstract symbols support faster judgments <!-- role: reason -->

Abstract symbols reduce interpretive load because viewers can rely on a single ordered cue, while iconic symbols require additional cognitive processing to recognize and map the metaphor.

**Mechanism:** Single-variable encodings are more likely to be processed as a direct perceptual order, while iconic signs add visual complexity and metaphor decoding steps.

**Evidence:** In symbol intuitiveness ranking, participants took longer to rate iconic symbol sets than abstract ones when pooling across uncertainty conditions [@maceachrenVisualSemioticsUncertainty2012]. In a region-level aggregation task, response times were also significantly slower overall for iconic versus abstract symbol sets when pooled across conditions [@maceachrenVisualSemioticsUncertainty2012].

**Notes:** Some individual uncertainty conditions deviated, so verify with your specific metaphor and task.

## When this applies to your visualization <!-- role: context -->

- **User Goal:** Make fast judgments about which region/item is less certain.
- **Task:** Visual search or aggregate comparison across multiple points.
- **Data:** Many symbols simultaneously visible; uncertainty encoded at each point.
- **Chart Setting:** Map-like displays or other point-per-region layouts.
- **Audience:** Users operating under time pressure or frequent scanning.
- **Success Criterion:** Low response time without sacrificing correctness.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The primary need is immediate conceptual matching between the uncertainty type and its depiction (teaching/communication), not fast scanning. **Why:** Metaphors can support meaning-making even if they slow performance.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Abstract encodings may feel less descriptive of the specific uncertainty type. **Risk:** Users may not distinguish different uncertainty categories as readily if multiple types are present. **Mitigation:** Use category labels or separate legend groupings for uncertainty types.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using visually complex icons for every uncertainty type in a dense map. **Why it fails:** Complexity increases time to aggregate across many points.
- **Mistake:** Assuming the “most intuitive” icon will also be the fastest in use. **Why it fails:** Higher intuitiveness can still come with slower processing.

## Quick tests <!-- role: check -->

**Failure Sign:** Users can answer correctly but take noticeably longer with icons. **Quick Check:** Time a few region-comparison tasks with iconic vs. abstract prototypes. **Stronger Test:** Run a small within-subject test and compare response time distributions.

## What to do instead <!-- role: fix -->

- Replace icons with a single-variable ordered encoding (e.g., fuzziness or value) for the uncertainty magnitude.
- Use iconic elements only in the legend or on-demand details, not on every point.
- Reserve icons for low-density views and switch to abstract encoding when zoomed out.
- Reduce icon complexity so the ordered cue dominates visually.
