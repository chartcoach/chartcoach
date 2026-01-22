---
id: show-bias-sensitivity-alongside-significant-results
title: Show bias sensitivity (u) alongside significant results when design and analysis
  flexibility is high
bibliography: references.bib
description: Flexibility in design, outcomes, and analyses can convert non-findings
  into findings; visual summaries should include a bias sensitivity view.
labels:
- chart:annotation
- task:assess
- visual:text
- impact:trust
- data:inferential
- audience:expert
- domain:research-quality
---

## Add a bias-sensitivity view when analytic flexibility is high <!-- role: advice -->

When summarizing significant findings from studies with many analytic choices, display how conclusions would change under plausible levels of bias (the fraction of non-findings that become findings). If bias sensitivity cannot be shown, avoid presenting the significant result as a stable endpoint.

## Why flexibility and selective reporting erode truth probability <!-- role: reason -->

Bias from design, data, analysis, and reporting choices can increase the apparent rate of statistically significant findings beyond what chance would produce, lowering the post-study probability that a reported significant finding is true.

**Mechanism:** A bias-sensitivity display makes the reader consider how much undisclosed flexibility could have shifted results across the significance boundary, reducing overinterpretation of borderline significant findings.

**Evidence:** Incorporating bias (u) into the predictive-value framework reduces PPV as bias increases across a wide range of powers and pre-study odds, meaning significant findings become less likely to be true in the presence of bias [@ioannidisWhyMostPublished2005]. Greater flexibility in designs, definitions, outcomes, and analytical modes increases the potential for transforming negative results into positive ones, undermining the reliability of claimed findings [@ioannidisWhyMostPublished2005].

**Notes:** Bias here includes selective outcome reporting and analysis/presentation choices that systematically favor significance.

## When this applies in evidence displays <!-- role: context -->

- **User Goal:** Decide whether a reported significant effect is robust to reasonable analytic variation.
- **Task:** Interpret reliability under potential selective reporting or outcome/analysis flexibility.
- **Data:** Observational or exploratory results; multiple outcomes/subgroups; many plausible model specifications.
- **Chart Setting:** Summary figures in papers, dashboards of model results, meta-research audits.
- **Audience:** Experts and decision-makers who may act on reported effects.
- **Success Criterion:** Reduced reliance on borderline significance; clearer uncertainty about robustness.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The analysis and outcomes are tightly protocol-driven with minimal flexibility and comprehensive reporting. **Why:** The plausible bias fraction is low enough that a bias-sensitivity overlay adds little decision value.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** More complexity and the need to communicate assumptions about bias levels. **Risk:** Users may misinterpret bias scenarios as accusations of misconduct rather than sensitivity analysis. **Mitigation:** Frame u as a structural property of flexible workflows, not as intent.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Reporting only the most favorable model/outcome as the “result.” **Why it fails:** It hides the flexibility that can manufacture significance and inflates perceived certainty.
- **Mistake:** Using decorative confidence language (“robust,” “strong”) without any sensitivity depiction. **Why it fails:** It substitutes rhetoric for evidence about how bias affects PPV.

## Quick tests <!-- role: check -->

**Failure Sign:** Small changes in reasonable analysis choices would plausibly flip the significance call, yet the display looks definitive. **Quick Check:** Ask whether the viewer can tell how many analytic paths could have been taken and whether results are stable across them. **Stronger Test:** Recompute the displayed takeaway under a few plausible alternative definitions/outcomes; if the conclusion changes, the visualization needs bias sensitivity.

## What to do instead <!-- role: fix -->

- Add a sensitivity panel that shows PPV (or qualitative confidence) across a small range of u values under stated power and R scenarios.
- Display multiple plausible specifications (outcomes, covariate sets, subgroups) rather than only the single best-looking estimate.
- Annotate whether outcomes and analyses were pre-specified versus selected after looking at data.
- Visually de-emphasize borderline p-values near 0.05 and emphasize uncertainty when flexibility is high.
