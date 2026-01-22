---
id: display-pre-study-odds-when-many-hypotheses-are-tested
title: Display pre-study odds when many relationships are tested, especially in discovery-oriented
  analyses
bibliography: references.bib
description: When thousands of hypotheses are probed, most statistically significant
  findings can be false unless prior odds are high.
labels:
- chart:table
- task:screen
- visual:annotation
- impact:trust
- data:high-dimensional
- audience:expert
- domain:discovery-research
---

## Make hypothesis multiplicity explicit with pre-study odds <!-- role: advice -->

When visualizing results from high-throughput or massive-testing studies, explicitly display the implied pre-study odds (true vs not-true relationships) for any individual claim. If the implied odds are extremely low, label individual significant hits as low-probability until independently confirmed.

## Why massive testing makes “hits” unreliable <!-- role: reason -->

If a field tests far more relationships than are plausibly true, the ratio of true to not-true relationships (R) is tiny; even with conventional α and moderate power, the positive predictive value for any single significant relationship becomes extremely low.

**Mechanism:** Showing the true-to-null ratio (or an equivalent “expected true hits” framing) prevents readers from confusing “a hit exists” with “this hit is likely true” in settings dominated by low priors.

**Evidence:** The probability a significant finding is true depends strongly on the ratio of true to not-true relationships tested (R), and PPV becomes extremely low in discovery-oriented research where tested relationships can exceed true ones by orders of magnitude [@ioannidisWhyMostPublished2005]. In a worked example of genome-wide testing with very low R, a p ≈ 0.05 association yields a very low post-study probability of truth even before considering bias or multiple teams [@ioannidisWhyMostPublished2005].

**Notes:** This is about interpretation of individual claimed relationships, not the value of discovery pipelines as generators of candidates.

## When this applies in evidence displays <!-- role: context -->

- **User Goal:** Interpret “top hits” from screening studies without overtrusting them.
- **Task:** Judge reliability of individual findings under massive hypothesis testing.
- **Data:** Many parallel tests (genes, biomarkers, exposures, model variants), typically with small effects.
- **Chart Setting:** Hit lists, volcano plots, Manhattan plots, ranked feature tables, “top-N” dashboards.
- **Audience:** Researchers, translational teams, journal readers.
- **Success Criterion:** Readers recognize low per-hit truth probability and demand confirmation.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The visualization only summarizes pre-specified, limited hypotheses in a confirmatory design with high pre-study plausibility. **Why:** The true-to-null ratio is not extremely small, so per-claim PPV need not be dominated by multiplicity.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Additional explanation and assumptions about how many true relationships exist. **Risk:** Readers may argue about the assumed number of true relationships and mistake it for a fixed known quantity. **Mitigation:** Present a plausible range of R values and show sensitivity of interpretation across that range.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Presenting “top hits” as discoveries without indicating the tiny base rate of true relationships. **Why it fails:** It encourages a narrative of certainty in contexts where most hits are expected to be false.
- **Mistake:** Using only extreme color/size emphasis for the smallest p-values. **Why it fails:** It can make bias or multiplicity-driven extremes look like strong evidence of truth.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers believe a random “top hit” is more likely true than false without any replication. **Quick Check:** Ask “Out of 100 displayed hits, how many do you expect to be real?”—if the display doesn’t help answer, it’s missing pre-study odds context. **Stronger Test:** Add an R sensitivity slider in a prototype and see whether user confidence changes appropriately as R decreases.

## What to do instead <!-- role: fix -->

- Add a compact “tested vs expected true” annotation (e.g., “~30 true among 30,000 tested” as a scenario) to contextualize R.
- Show a scenario-based positive predictive value (PPV) band for an individual hit under plausible R and power values.
- Separate “candidate-generating” results from “confirmed” results with distinct sections and restrained styling for candidates.
- Include an explicit replication-needed label for any single-claim highlight drawn from massive testing.
