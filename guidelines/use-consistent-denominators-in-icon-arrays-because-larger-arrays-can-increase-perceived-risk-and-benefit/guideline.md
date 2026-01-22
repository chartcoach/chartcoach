---
id: use-consistent-denominators-in-icon-arrays-because-larger-arrays-can-increase-perceived-risk-and-benefit
title: Use a consistent icon-array denominator because larger denominators can inflate
  perceived risk reduction
bibliography: references.bib
description: Changing icon-array size (e.g., 100 vs 1,000) can change perceived seriousness
  and perceived helpfulness even when risks are equivalent.
labels:
- chart:icon-array
- task:judge
- visual:quantity
- impact:perception
- data:probability
- audience:general
- domain:health-risk
---

## Keep the same total number of icons when comparing risks or benefits <!-- role: advice -->

Keep the icon-array denominator consistent (the same total number of icons) across conditions you want viewers to compare, because larger arrays can make the same risk and risk reduction feel larger.

## Why denominator size changes perceived magnitude <!-- role: reason -->

When the total set is larger, the absolute number of affected icons increases even if the percentage is identical, which can make outcomes and changes feel more substantial.

**Mechanism:** Viewers may weight the visible count of affected icons more than the underlying ratio, shifting judgments of seriousness and helpfulness.

**Evidence:** In visual conditions, using 1,000 icons (vs. 100) led to higher perceived helpfulness of screening (perceived risk reduction), and showed a tendency toward higher perceived seriousness of baseline risk, despite equivalent underlying probabilities [@galesicUsingIconArrays2009].

**Notes:** The study manipulated denominators directly (100 vs. 1,000) while holding percentages constant.

## When denominator consistency is critical <!-- role: context -->

- **User Goal:** Compare baseline risk vs treated risk, or compare options across panels.
- **Task:** Judge seriousness or helpfulness from the display.
- **Data:** Equivalent probabilities that could be displayed with different denominators.
- **Chart Setting:** Side-by-side icon arrays, multi-panel decision aids, or repeated measures over multiple scenarios.
- **Audience:** General audiences, including those relying on visual impression rather than calculation.
- **Success Criterion:** Perceived differences track real differences, not formatting differences.

## When not to follow this exactly <!-- role: exceptions -->

**Break it when:** You intentionally want to communicate a fixed population framing (e.g., always “out of 1,000”) and will not mix denominators anywhere in the same experience. **Why:** The perception shift arises when denominator choices vary or when the chosen denominator itself changes impression.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** A single denominator may force very small risks to be visually tiny or hard to see. **Risk:** If you choose a very large denominator, the display may become dense and harder to scan. **Mitigation:** Treat denominator as a global design constraint and validate readability with quick user checks.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Mixing 100-icon and 1,000-icon arrays within the same material for equivalent percentages. **Why it fails:** Viewers may infer different seriousness or benefit from the denominator change rather than from the data.

## Quick tests <!-- role: check -->

**Failure Sign:** Users rate one scenario as more serious/helpful even though the percentage risk and reduction are the same.\
**Quick Check:** Verify denominators are identical across all icon arrays meant for comparison.\
**Stronger Test:** Ask users to compare two equal-percentage scenarios displayed with different denominators and see if perceived differences emerge.

## What to do instead <!-- role: fix -->

- Standardize on one denominator across the full set of icon arrays in a document or tool.
- If you must change denominators, separate the displays so they are not directly compared and label the denominator prominently.
- Use the same denominator for baseline and treated arrays within each scenario to preserve comparability.
- If small risks become imperceptible at a fixed denominator, shift the task to a numeric ratio-only presentation for those cases.
