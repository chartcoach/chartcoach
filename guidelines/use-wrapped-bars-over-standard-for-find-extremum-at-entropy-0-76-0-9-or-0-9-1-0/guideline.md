---
id: use-wrapped-bars-over-standard-for-find-extremum-at-entropy-0-76-0-9-or-0-9-1-0
title: "Use wrapped bar charts for find-extremum when normalized entropy is 0.76\u2013\
  0.90 or 0.90\u20131.00"
bibliography: references.bib
description: For find-extremum performance, wrapped bar charts were ranked above standard
  bar charts at higher normalized-entropy bins in the extracted results.
labels:
- chart:bar
- task:find-extremum
- visual:length
- impact:accuracy
- data:categorical
- audience:general
- data:entropy
- variant:wrapped-bar
---

## Prefer wrapped bars at higher entropy bins for extreme-value tasks <!-- role: advice -->

For find-extremum tasks on categorical bar charts, choose a wrapped bar chart over a standard bar chart when your normalized entropy falls in the 0.76–0.90 or 0.90–1.00 ranges.

## Why this entropy condition matters in the extracted ranking <!-- role: reason -->

Within the extracted design set that varies by entropy bins, the best-performing (highest-ranked) designs for accuracy were wrapped bar charts in higher entropy bins, and they were significantly better than multiple lower-ranked alternatives, indicating that wrapping can remain beneficial even when values are more evenly spread than the most concentrated cases.

**Mechanism:** Wrapping preserves visibility of smaller bars while keeping a linear-length encoding, supporting accurate extreme-value identification under the tested entropy conditions.

**Evidence:** In the extracted find-extremum accuracy ranking over entropy-binned designs, the wrapped-bar designs for entropy 0.76–0.90 and 0.90–1.00 were ranked above the standard-bar designs for those bins (with the standard-bar designs grouped below) and the reported significance pairs show the top wrapped designs outperform several lower-ranked designs [@karduniBoisWrappedBar2020]. This entropy-conditioned guidance comes from collated graphical perception knowledge formatted for recommendation rules [@zengReviewCollationGraphical2023].

**Notes:** This guideline is strictly tied to the entropy bins present in the extracted designs and should not be extrapolated to other entropy thresholds.

## Context: When this applies <!-- role: context -->

- **User Goal:** Correctly pick the smallest or largest category.
- **Task:** find-extremum.
- **Data:** Nominal categories with quantitative values; normalized entropy in 0.76–0.90 or 0.90–1.00 (as binned in the extracted designs).
- **Chart Setting:** Static vertical bar charts using bar length on a linear scale, comparing standard vs. wrapped variants.
- **Audience:** General audiences or analysts performing quick extreme-value judgments.
- **Success Criterion:** Higher accuracy for extreme-value identification.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** You cannot compute or reasonably estimate normalized entropy for the dataset you are charting. **Why:** The trigger condition for this guideline is the entropy bin.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Viewers must parse wrapped segments, which can add reading effort. **Risk:** If viewers misunderstand wrapping, they may misidentify which bar is actually largest. **Mitigation:** Validate comprehension with a quick internal review before deploying widely.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Treating “entropy in the bin” as a guarantee of improvement for every dataset and audience. **Why it fails:** The extracted evidence is task- and bin-specific, and other unmodeled factors can affect results.

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Extreme-value identification errors remain common in a standard bar chart even though values are not extremely concentrated. **Quick Check:** Compute normalized entropy and confirm it falls in 0.76–0.90 or 0.90–1.00, then compare a wrapped vs. standard mock-up for smallest/largest identification. **Stronger Test:** Run a short A/B task test (find smallest, find largest) and compare accuracy.

## Fix: What to do instead <!-- role: fix -->

- Keep the standard bar chart when extremes are already unambiguous and accuracy issues are not observed.
- Provide direct labeling for the smallest and largest categories if the goal is communication rather than discovery.
- Add a supplementary view that focuses on extremes if wrapping is not acceptable to your audience.
