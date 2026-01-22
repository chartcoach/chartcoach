---
id: use-kde-density-plots-to-encode-per-sample-uncertainty-in-scatter-plots
title: "Render uncertain scatter plots as kernel density estimates using each sample\u2019\
  s uncertainty distribution"
bibliography: references.bib
description: Replace discrete points with a density image built from per-sample uncertainty
  distributions to reduce false inferences.
labels:
- chart:scatter
- task:explore
- visual:luminance
- impact:trust
- data:uncertain
- audience:expert
- complexity:advanced
---

## Encode uncertainty by density instead of discrete points in scatter plots <!-- role: advice -->

Render uncertain scatter plot data as a kernel density estimate (KDE) by summing each sample’s uncertainty distribution in data space. Display the resulting probability density function (PDF) as image intensity so uncertain values blur out while confident values remain visually salient.

## KDE density mapping aligns saliency with statistical confidence <!-- role: reason -->

Representing each uncertain sample as a distribution and summing them produces a PDF where high-certainty samples contribute sharper, higher-contrast structure and high-uncertainty samples contribute diffuse, low-contrast structure. This makes preattentive detection more likely for reliable structure and less likely for unreliable structure.

**Mechanism:** Large-variance distributions overlap and flatten, reducing local contrast and making “clusters” of uncertain means harder to perceive, while small-variance distributions create sharp peaks that remain distinguishable.

**Evidence:** Using per-sample distributions as KDE kernels produces density plots that draw attention to high-certainty values and prevent viewers from being drawn to uncertain values that can create false positives in discrete plots [@fengMatchingVisualSaliency2010]. Density-based representations also scale better than opaque glyphs under over-plotting because the PDF summarizes density directly [@fengMatchingVisualSaliency2010].

**Notes:** The KDE kernel is the sample’s own uncertainty distribution rather than an arbitrary, fixed kernel width.

## When to use KDE density scatter plots for uncertain data <!-- role: context -->

- **User Goal:** Identify patterns (clusters, trends, correlations) without being misled by unreliable measurements.
- **Task:** Visual exploration and hypothesis generation under uncertainty.
- **Data:** Bivariate values with per-sample uncertainty representable as statistical distributions (for example, normal distributions with per-dimension standard deviations).
- **Chart Setting:** Static or interactive scatter plot where over-plotting or uncertainty could create misleading apparent structure.
- **Audience:** Analysts who need to reason about reliability (for example, clinicians or scientists).
- **Success Criterion:** Viewers attend primarily to statistically confident structure and avoid inferring structure from uncertain values.

## When not to use KDE density scatter plots <!-- role: exceptions -->

**Break it when:** The task requires persistent identification and tracking of specific individual samples by identity in the scatter plot. **Why:** Direct PDF images summarize probability mass and can make individual points hard to pick out or reference [@fengMatchingVisualSaliency2010].

## Tradeoffs of density-based uncertainty encoding <!-- role: costs -->

**Sacrifice:** Individual sample identifiability is reduced because many samples merge into continuous density [@fengMatchingVisualSaliency2010]. **Risk:** Outliers may be deemphasized because low-probability contributions are visually faint [@fengMatchingVisualSaliency2010]. **Mitigation:** Use a complementary outlier-focused view or an outlier highlighting approach instead of relying on the PDF alone.

## Common mistakes when using density plots for uncertainty <!-- role: mistakes -->

- **Mistake:** Plot uncertain data as discrete points and encode uncertainty only by color or a legend. **Why it fails:** Discrete glyphs can still form visually salient but unreliable clusters, creating false positives that viewers notice before consulting uncertainty encodings [@fengMatchingVisualSaliency2010].
- **Mistake:** Use an arbitrary fixed KDE kernel width while ignoring per-sample uncertainty. **Why it fails:** The plot no longer reflects the modeled reliability of each point, so saliency is not proportional to confidence [@fengMatchingVisualSaliency2010].

## Quick checks for whether uncertainty is properly deemphasized <!-- role: check -->

**Failure Sign:** Viewers can quickly “see” clusters in regions known to be highly uncertain. **Quick Check:** Compare the discrete plot to the density plot; visually salient features should concentrate where uncertainty is low, not where uncertainty is high [@fengMatchingVisualSaliency2010]. **Stronger Test:** Verify that regions dominated by large-variance samples appear as broad, low-contrast structure rather than crisp clusters.

## What to do instead if KDE density is not workable <!-- role: fix -->

- Render a probabilistic (random-sample) scatter plot that samples from each point’s uncertainty distribution and animates over time to summarize the PDF without explicit density computation [@fengMatchingVisualSaliency2010].
- Compute the PDF at lower resolution (coarser grid) to get an approximate density image faster, then refine progressively when time allows [@fengMatchingVisualSaliency2010].
- Use linked views so the scatter plot can remain a summary while selection and details are handled elsewhere [@fengMatchingVisualSaliency2010].
- Separate outliers into a distinct overlay so they remain discoverable even when the PDF deemphasizes them [@fengMatchingVisualSaliency2010].
