---
id: avoid-log-scales-for-public-risk-communication
title: Avoid Logarithmic Scales in Public Risk Displays
bibliography: references.bib
description: Do not rely on log scales for communicating risk magnitude to general
  audiences.
labels:
- chart:axis
- task:compare
- visual:position
- impact:clarity
- data:proportion
- audience:general-public
- domain:risk-communication
---

## The Rule <!-- role: advice -->

Avoid logarithmic scales when communicating risk magnitudes to the general public.

## The Logic <!-- role: reason -->

Log scales are difficult for most people to interpret, especially for very small probabilities, undermining comprehension of differences.

- **The Principle:** Scale comprehension limits for non-expert audiences
- **The Evidence:** [@lipkusNumericVerbalVisual2007]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand and compare absolute magnitudes of rare vs less-rare risks
- **Data Type:** Very small probabilities (e.g., 1 in 100,000 vs 1 in 1,000,000)
- **Audience:** Patients/public without specialized training

## When to Break It <!-- role: exceptions -->

- **Scenario:** The audience is trained and expects log scales (e.g., technical experts) and the chart is clearly labeled and taught.
- **Reason:** Expert users may need log compression to compare across orders of magnitude. [@lipkusNumericVerbalVisual2007]

## The Price <!-- role: costs -->

- **The Sacrifice:** Linear scales may require more space or truncation strategies.
- **The Risk:** Without a log scale, extremely small and moderate probabilities may not fit comfortably on one axis.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using log scale to “fit everything,” assuming readers will understand.
- **Why it fails:** Readers misread distance as linear change. [@lipkusNumericVerbalVisual2007]

## How to Check <!-- role: check -->

- **Visual Sign:** Tick marks increase by powers of 10 (…, 0.1, 1, 10, 100 …) on the same axis.
- **The Test:** Ask a layperson what “twice as far” means on the axis—if they answer linearly, the chart will mislead.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace with a linear scale focused on the relevant range.
- **Best Fix:** Split into panels or use a ladder-style comparison with clear numeric labels rather than a log axis. [@lipkusNumericVerbalVisual2007]
