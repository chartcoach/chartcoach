---
id: document-omissions-and-data-reductions
title: Disclose Variable Selection and Data Reduction Choices
bibliography: references.bib
description: Make framing-by-omission visible by stating what was excluded, aggregated,
  thresholded, or simplified.
labels:
- task:explain
- impact:trust
- impact:clarity
- custom:rhetoric:information-access
- audience:general-public
---

## The Rule <!-- role: advice -->

When you omit or simplify—through **variable selection**, **thresholding**, **outlier removal**, **aggregation/binning**, or **summaries**—explicitly state what was done and what was left out.

## The Logic <!-- role: reason -->

Information access rhetoric often works via omission and metonymy (part-for-whole substitutions); because these choices constrain what interpretations are possible, they can strongly frame the story even when not obvious to readers.

- **The Principle:** Omission constrains interpretation space
- **The Evidence:** [@hullmanVisualizationRhetoricFraming2011a]

## Where to Apply <!-- role: context -->

- **User Goal:** Judge whether the visualization is a fair representation of the phenomenon
- **Data Type:** Multi-variable datasets or complex phenomena needing simplification
- **Audience:** Readers lacking full domain context (common in journalism)

## When to Break It <!-- role: exceptions -->

- **Scenario:** Extremely space-constrained graphics where disclosure would prevent comprehension
- **Reason:** If disclosure overwhelms the primary message, provide a linked methods note instead.

## The Price <!-- role: costs -->

- **The Sacrifice:** Brevity and “clean” presentation
- **The Risk:** Disclosures can draw attention to limitations and weaken persuasive force.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Pretending the shown variables represent the whole phenomenon
- **Why it fails:** Metonymy can mislead by implying the part stands for the whole without warning [@hullmanVisualizationRhetoricFraming2011a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users could reasonably assume “this is all the relevant data,” but it is not
- **The Test:** List plausible alternative variables or ranges a reader might expect; if you excluded them, disclose.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a short note: “Shows X; excludes Y; values aggregated to Z.”
- **Best Fix:** Provide optional “view more variables/ranges” interaction or an appendix view showing what was omitted.
