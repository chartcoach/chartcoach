---
id: group-by-performance-not-total-rank
title: "Group visualizations by performance tiers rather than creating a definitive total ranking"
tags:
  - impact:logos
  - impact:perceptual
  - impact:ethical
  - task:rank
  - task:compare
evidence:
  strength: medium
  summary: "A 2016 Bayesian re-analysis of graphical perception data demonstrated that many visualizations have statistically indistinguishable performance, making a strict total ranking misleading. Grouping charts into performance tiers more accurately reflects the evidence and statistical uncertainty."
sources:
  - type: research
    ref: "Kay & Heer, 2016"
    url: "https://doi.org/10.1109/TVCG.2015.2467671"
    note: "This paper's core methodological argument is that a partial ranking based on statistical uncertainty is more robust than a total ranking that ignores error."
    role: primary
  - type: research
    ref: "Harrison et al., 2014"
    url: "https://doi.org/10.1109/TVCG.2014.2346979"
    note: "An example of a study that produced a total ranking, which the primary source argues can be misleading."
    role: related
---

## Guidance

When comparing the effectiveness of different visualization designs, group them into performance tiers (e.g., 'high precision', 'medium precision'). Differences *between* tiers should be statistically meaningful, while differences *within* a tier can be considered negligible. Avoid creating a strict, ordered list (1st, 2nd, 3rd...) unless the differences are all large and significant.

## Why

Creating a strict total ranking can be misleading because it amplifies small, statistically insignificant differences in performance. This suggests a superiority of one design over another that may not actually exist and could simply be due to random chance or noise in the experiment. Grouping designs into tiers provides a more robust and honest assessment of the evidence, preventing designers from over-interpreting minor variations.

### Core Principle

Acknowledge and communicate uncertainty in evidence. Design decisions should be based on statistically meaningful differences, not on noise.

## When it applies

- When evaluating and comparing multiple chart designs based on user study results.
- When creating style guides or visualization recommendation systems.
- When interpreting academic research on graphical perception to derive practical takeaways.

## Exceptions

- If performance differences between all tested designs are very large and all pairwise comparisons are statistically significant, a total ranking might be justified. However, this is rare in practice.

## Trade-offs

- A partial ranking is more nuanced and statistically sound, but is less simple than a total ranking. It requires more careful communication to explain why certain designs are "in the same group" rather than providing a single "best" option.

## Signs of Trouble

- **False Precision:** A design guide claims "Chart A is better than Chart B" based on a study where the reported performance difference was very small or not statistically significant.
- **Dogmatic Recommendations:** A recommendation system always suggests the same single "best" chart for a task, without considering other equally effective alternatives.
- **Overstating Evidence:** A presentation or report makes strong claims about the superiority of one design over another based on their relative positions in a ranking, without mentioning the magnitude or statistical significance of the difference.

## How to Improve

- **Quick Fix: Add a Caveat.** When citing research that uses a total ranking, add a note of caution: "The performance of the top three charts was very similar, so any could be a good choice." This adds necessary context without requiring a full re-analysis.

- **Moderate Approach: Visualize the Uncertainty.** When presenting comparison results, use charts that show uncertainty, such as bar charts with error bars or plots of posterior distributions. This visually communicates which differences are meaningful and which are not.

- **Comprehensive Approach: Conduct a Bayesian Analysis.** When analyzing experimental data, use methods that account for uncertainty and can directly test for practical equivalence (e.g., Bayesian estimation, region of practical equivalence testing). Present the results as a partial order or grouped ranking, explicitly stating which designs are statistically indistinguishable.