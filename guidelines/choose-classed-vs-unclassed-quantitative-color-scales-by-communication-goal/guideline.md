---
id: choose-classed-vs-unclassed-quantitative-color-scales-by-communication-goal
title: Choose Classed or Unclassed Color Scales Based on Your Communication Goal
bibliography: references.bib
description: Decide between classed and unclassed quantitative color scales by whether
  you need brackets and readability or nuance and reader-driven interpretation.
labels:
- chart:choropleth
- task:encode
- visual:color
- impact:clarity
- data:quantitative
- audience:general
- decision:classed-vs-unclassed
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

Use a **classed** (binned/stepped) color scale when you need readers to identify **statistical brackets** or **read value ranges**; use an **unclassed** (continuous) color scale when you need a **nuanced view** or want to **avoid interpreting the data for readers**. Start by viewing the data unclassed, then decide whether to simplify into classes. [@muth_classed_vs_unclassed_2021]

## The Logic <!-- role: reason -->

Classed scales deliberately simplify: they make category-like groupings salient, which helps readers quickly see who falls above/below a threshold and estimate ranges more reliably. Unclassed scales preserve fine-grained variation, supporting detection of subtle transitions, outliers, and local comparisons without forcing a designer-chosen bin structure. [@muth_classed_vs_unclassed_2021]

- **The Principle:** Trade-off between **simplification for bracket recognition/value estimation** vs **fidelity for nuanced pattern reading**
- **The Evidence:** Comparative findings and synthesis discussed in [@muth_classed_vs_unclassed_2021]

## Where to Apply <!-- role: context -->

- **User Goal:**
  - Bracket question: “Is this region above/below a benchmark (e.g., national average)?” → classed
  - Range reading: “Which value band is this in?” (especially in static outputs) → classed
  - Pattern/nuance question: “How smoothly do values change?” “How does my area compare to neighbors?” “Where are outliers?” → unclassed
- **Data Type:** Quantitative values encoded with a sequential or diverging color scale (often choropleths/maps, but applicable to any quantitative color encoding). [@muth_classed_vs_unclassed_2021]
- **Audience:** Especially helpful for general audiences and mixed audiences where fast bracket recognition or reliable range reading matters. [@muth_classed_vs_unclassed_2021]

## When to Break It <!-- role: exceptions -->

- **Scenario:** The data is **not continuous** (ordinal categories like Likert responses, clothing sizes, ranks).
  - **Reason:** A continuous (unclassed) gradient implies in-between values that don’t exist; use classed instead. [@muth_classed_vs_unclassed_2021]
- **Scenario:** You need readers to judge **specific statistical cutoffs** (e.g., “top decile,” “>2 standard deviations above mean”).
  - **Reason:** Unclassed scales make it harder to see membership in predefined brackets. [@muth_classed_vs_unclassed_2021]
- **Scenario:** Your goal is precise “reading” from the legend in a **static** context (print/PDF) without tooltips.
  - **Reason:** Unclassed values are inherently more guess-like; classed ranges are more confidently readable. [@muth_classed_vs_unclassed_2021]

## The Price <!-- role: costs -->

- **The Sacrifice:**
  - Choosing **classed** sacrifices nuance; within-bin differences disappear and outliers can be lumped together. [@muth_classed_vs_unclassed_2021]
  - Choosing **unclassed** sacrifices easy bracket membership and reliable range reading; viewers may only make “good guesses.” [@muth_classed_vs_unclassed_2021]
- **The Risk:**
  - Classing can steer the message by how bins are defined, potentially hiding important local differences. [@muth_classed_vs_unclassed_2021]
  - Unclassed can underserve statistical objectives (benchmarks become visually ambiguous). [@muth_classed_vs_unclassed_2021]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using an unclassed gradient for inherently ordinal data.
  - **Why it fails:** It falsely suggests intermediate categories. [@muth_classed_vs_unclassed_2021]
- **The Wrong Fix:** Using very few classes to show a broad pattern when nuance matters.
  - **Why it fails:** It over-simplifies and masks meaningful differences (e.g., neighbor comparisons, abrupt vs smooth transitions). [@muth_classed_vs_unclassed_2021]
- **The Wrong Fix:** Assuming unclassed automatically removes interpretive burden from the designer.
  - **Why it fails:** Other choices (e.g., legend design) still strongly shape interpretation. [@muth_classed_vs_unclassed_2021]

## How to Check <!-- role: check -->

- **Visual Sign:**
  - If your story is about a threshold/benchmark but the map looks like a smooth wash with no clear “above vs below,” you likely needed classes. [@muth_classed_vs_unclassed_2021]
  - If important local differences (e.g., border-to-border comparisons) vanish into identical colors, you likely over-classed. [@muth_classed_vs_unclassed_2021]
- **The Test:** State your core question as a yes/no:
  - “Do I need readers to identify membership in predefined brackets or read ranges confidently?” → classed
  - “Do I want readers to see subtle differences, transitions, and local comparisons?” → unclassed [@muth_classed_vs_unclassed_2021]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch the scale type: toggle between classed and unclassed, then re-check whether the result matches the intended question (brackets vs nuance). [@muth_classed_vs_unclassed_2021]
- **Best Fix:** Start from an unclassed view to understand subtle variation, then (only if needed) introduce classes that align with your explicit statistical objective (e.g., below/above benchmark) or value-reading needs. [@muth_classed_vs_unclassed_2021]
