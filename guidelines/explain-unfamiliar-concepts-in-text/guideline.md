---
id: explain-unfamiliar-concepts-in-text
title: Explain Unfamiliar Concepts in Text
bibliography: references.bib
description: Prevent misinterpretation of complex visuals like uncertainty ranges
  by defining them in captions or surrounding prose.
labels:
- impact:clarity
- impact:trust
- audience:novice
- visual:annotation
- data:uncertainty
- task:interpret
---

## The Rule <!-- role: advice -->

Define technical terms, baselines, and uncertainty ranges in the accompanying text or captions. Do not rely solely on visual encodings or legends to explain complex concepts to lay audiences.

## The Logic <!-- role: reason -->

Visualizing uncertainty or complex baselines without textual explanation creates ambiguity. When lay viewers encounter unexplained uncertainty ranges (like shaded areas), they often mistake the visual variance for data unreliability or distrust the source. Explicit text bridges the gap between visual representation and conceptual understanding.

*   **The Principle:** Disambiguation.
*   **The Evidence:** Experts note that without explanation, uncertainty looks like unreliability to lay viewers [@schuster_being_2024]. Practitioners emphasize that while shaded ranges seem intuitive to designers, text is safer for avoiding confusion [@schuster_who_2023].

## Where to Apply <!-- role: context -->

Use this whenever your chart includes statistical nuance that falls outside common knowledge.

*   **Audience:** General public or non-subject-matter experts.
*   **Data Type:** Future scenarios, climate models, or uncertainty ranges (e.g., confidence intervals).
*   **Specific Elements:** Technical baselines (e.g., "1850–1900 reference period") or probability bands.

## When to Break It <!-- role: exceptions -->

*   **Scenario:** Scientific or technical publications for expert audiences.
*   **Reason:** Experts are trained to interpret standard error bars and confidence intervals without remedial explanation; over-explaining may feel patronizing.

## The Price <!-- role: costs -->

*   **The Sacrifice:** Increases the reading time and word count surrounding the visualization.
*   **The Risk:** If the visual is separated from the text (e.g., shared as an isolated image), the context is lost.

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Creating an overly complex legend that explains *how* to read the chart rather than *what* the data represents.
*   **Why it fails:** Legends disconnect the explanation from the data; users often skip them.
*   **The Omission:** Assuming "Standard Error" or specific historical baselines are common knowledge.

## How to Check <!-- role: check -->

*   **Visual Sign:** A chart containing shaded regions or error bars with no corresponding sentence in the title, subtitle, or caption explaining them.
*   **The Test:** Ask a non-expert, "What does this shaded area mean?" If they say "It looks messy" or "The data is bad," you have failed to explain the concept.

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Add a sentence to the chart caption: "The shaded area represents the range of possible outcomes."
*   **Best Fix:** Integrate the definition into the chart's subtitle or annotation layer so the explanation is unavoidable (e.g., "Temperatures may vary within this range (shaded area) depending on future emissions").
