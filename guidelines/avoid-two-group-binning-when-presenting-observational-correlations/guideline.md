---
id: avoid-two-group-binning-when-presenting-observational-correlations
title: Avoid binning continuous observational data into two groups when presenting
  correlations
bibliography: references.bib
description: Two-group binning can invite causal interpretations by turning an association
  into an apparent condition comparison.
labels:
- chart:bar
- chart:text
- task:compare
- visual:aggregation
- impact:trust
- data:continuous
- audience:novice
- custom:causality
---

## Do not collapse continuous data into a two-group contrast <!-- role: advice -->

Avoid splitting a continuous predictor into only two groups and presenting group averages when the data are observational and causality is not established. Use a more granular display that does not imply a binary “treatment vs control” comparison.

## Why two-group summaries invite causal framing <!-- role: reason -->

Turning a continuous relationship into a two-level contrast makes it easy to reason as if there are two conditions and one causes the other, which aligns with everyday causal templates. This can encourage counterfactual thinking (“if we move from low to high, Y will change”) even when the data only show association.

**Mechanism:** Two-group contrasts compress the relationship into a simple comparison that maps onto causal schemas of condition → outcome.

**Evidence:** Participants showed relatively high causal agreement for the two-group summary formats (bar-like summaries and parallel text descriptions) compared with formats that did not force a binary grouping. [@xiongIllusionCausalityVisualized2020]

**Notes:** The paper identifies two-bar bar charts as a notable case that can particularly invite causal interpretations.

## When to avoid two-group binning <!-- role: context -->

- **User Goal:** Prevent overconfident causal takeaways from correlational evidence.
- **Task:** Compare levels of Y across values of X without implying an intervention.
- **Data:** Continuous X and Y from survey/observational sources.
- **Chart Setting:** Reports where a binary story would be especially persuasive (e.g., “more vs less,” “before vs after” without a true intervention).
- **Audience:** Viewers who may equate “difference between two bars” with “effect of a change.”
- **Success Criterion:** Viewers describe the relationship without counterfactual causal language.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The underlying measure is genuinely binary or the analysis is explicitly defined as a two-group comparison. **Why:** In those cases, two groups are the data structure rather than an imposed simplification.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** More granular displays can be less immediately punchy than a two-group contrast. **Risk:** Viewers may struggle to extract a single headline difference. **Mitigation:** Provide a concise associative takeaway while still showing the more granular structure.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Choosing a two-group split because it “simplifies the story.” **Why it fails:** The simplification can increase perceived causality beyond what the evidence supports.
- **Mistake:** Presenting a two-group bar chart and assuming adding “survey data” in a footnote prevents causal inference. **Why it fails:** High causal agreement occurred even when the data were described as survey-based.

## Quick tests <!-- role: check -->

**Failure Sign:** The audience interprets the two groups as an intervention (“if we move people from group A to group B, outcomes will improve”). **Quick Check:** Re-express the same data using more bins and see whether causal language decreases in paraphrases. **Stronger Test:** Collect causal agreement ratings for a two-group version versus a multi-bin version.

## What to do instead <!-- role: fix -->

- Increase the number of bins/groups so the relation is not reducible to a single binary contrast.
- Use a scatter-style view that shows individual observations rather than only group averages.
- Provide a depiction that reveals within-bin variability instead of only a mean per group.
- If a grouped summary must be shown, pair it with a less-aggregated view that demonstrates dispersion.
