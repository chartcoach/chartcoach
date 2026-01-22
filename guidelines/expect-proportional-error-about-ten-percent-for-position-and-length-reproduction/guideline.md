---
id: expect-proportional-error-about-ten-percent-for-position-and-length-reproduction
title: Plan for roughly 10% proportional error when people reproduce bar or dot values
  from memory
bibliography: references.bib
description: When viewers reproduce a single bar or dot value after brief viewing,
  typical error scales with the value at about a tenth of it.
labels:
- chart:bar
- chart:dot
- task:estimate
- task:read-value
- visual:position
- visual:length
- impact:accuracy
- data:proportional
- audience:general
- complexity:advanced
---

## Budget for ~10% value-level noise in memory-based readouts <!-- role: advice -->

Assume that memory-based readout of a single encoded value (bar height or dot position) will include error on the order of about one tenth of the value. Treat small differences that are below that scale as potentially indistinguishable without added supports.

## Proportional (Weber-like) noise in reproduced magnitudes <!-- role: reason -->

When viewers reproduce a previously seen magnitude, error tends to grow with the magnitude itself, consistent with proportional noise. This means that absolute error increases for larger values, but percent error can stay roughly similar across the range.

**Mechanism:** Variability in perceptual/memory representation scales with stimulus magnitude, increasing absolute error for larger values while keeping proportional error comparatively stable.

**Evidence:** Across multiple experiments using method-of-adjustment reproduction for bars and dots, average reproduction error was about 10% of the actual value, and absolute error increased with larger presented values. [@mccolemanNoMarkIsland2021]

**Notes:** This guideline is about memory-based reproduction/readout, not about all possible chart-reading tasks.

## When proportional error matters in design decisions <!-- role: context -->

- **User Goal:** Distinguish values and make decisions based on single-value readout.
- **Task:** Read a value, remember it briefly, and use it later (e.g., compare across views, screens, or steps).
- **Data:** Percent-like scales (1–99%) or other bounded magnitudes.
- **Chart Setting:** Interfaces where values disappear, change, or require users to switch views.
- **Audience:** Any audience, especially when relying on quick glances.
- **Success Criterion:** Differences that matter are larger than typical perceptual/memory noise.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The task does not involve remembering a value (the value remains visible for direct inspection). **Why:** The reported error pattern is measured under brief presentation plus reproduction from memory.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Designing for larger separations can reduce information density. **Risk:** Over-applying a single “10%” budget may oversimplify performance for specialized contexts. **Mitigation:** Use this as an initial sizing heuristic and confirm with a task-matched pilot.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Treating very small percentage differences as reliably readable after view switching. **Why it fails:** Typical proportional error can swamp those differences in memory-based use.

## Quick tests <!-- role: check -->

**Failure Sign:** Users report “these look the same” or reverse which is larger after switching views. **Quick Check:** If your important differences are routinely under ~10% of the value magnitude, flag the design for validation. **Stronger Test:** Ask representative users to view a value briefly and then reproduce it; compute percent error and compare it to your required decision threshold.

## What to do instead <!-- role: fix -->

- Keep the value visible while the user performs downstream decisions instead of requiring recall.
- Add direct value labels when small differences must be acted on.
- Reduce the number of required cross-view comparisons by co-locating values that must be compared.
- Use interaction that preserves a stable reference while changing context (so users do not rely on memory alone).
