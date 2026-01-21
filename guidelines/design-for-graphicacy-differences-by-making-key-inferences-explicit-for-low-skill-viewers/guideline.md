---
id: design-for-graphicacy-differences-by-making-key-inferences-explicit-for-low-skill-viewers
title: Make Key Inferences Explicit for Low-Graphicacy Audiences
bibliography: references.bib
description: Low graphicacy viewers are unlikely to generate main-effect inferences
  even when the format supports them, so important inferences should be explicitly
  represented or prompted.
labels:
- chart:bar
- chart:line
- task:infer
- impact:accessibility
- data:multivariate
- audience:novice
- custom:graphicacy
- complexity:medium
- source:shah-freedman-2011
---

## The Rule <!-- role: advice -->

When your audience may have low graphicacy, explicitly represent or prompt the key inferences you need them to take away (e.g., main effects), rather than expecting them to compute them from the chart.

## The Logic <!-- role: reason -->

Main-effect statements require mental transformations (e.g., aggregating across a third variable). In the study, higher graphicacy predicted more main-effect inferences; low-skilled viewers did not reliably produce these inferences even when viewing bar graphs that otherwise supported them.

- **The Principle:** Inference generation depends on domain-general graph skills, not just the visual format.
- **The Evidence:** High-skilled viewers made more main-effect inferences than low-skilled viewers; the strongest inference generation occurred for high-skilled viewers with familiar data in bar graphs [@shahBarLineGraph2011].

## Where to Apply <!-- role: context -->

- **User Goal:** Ensure accurate takeaway beyond surface patterns (especially main effects).
- **Data Type:** Multivariate (three-variable) displays where aggregation is needed.
- **Audience:** General public, students, or any group with mixed/unknown graph literacy.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are evaluating spontaneous interpretation or want unprompted “what stands out” responses.
- **Reason:** Making inferences explicit changes the task by guiding what viewers report [@shahBarLineGraph2011].

## The Price <!-- role: costs -->

- **The Sacrifice:** More annotation/prompts can reduce perceived neutrality and increase clutter.
- **The Risk:** Over-guidance may narrow attention to the prompted inference and reduce exploration of other relationships [@shahBarLineGraph2011].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming a “better” chart type (e.g., bar) is sufficient for low-skill audiences.
- **Why it fails:** The limiting factor is often the viewer’s ability to perform mental computations from the display, not just the encoding [@shahBarLineGraph2011].

## How to Check <!-- role: check -->

- **Visual Sign:** Users restate only obvious surface patterns (e.g., “the lines go down”) and omit overall comparisons.
- **The Test:** Split-test with and without explicit prompts; if only the prompted version yields the intended inference for low-skill users, you needed explicit support [@shahBarLineGraph2011].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a short question or instruction that asks for the intended inference (“Overall, which group is higher?”).
- **Best Fix:** Combine a supportive format (often bars for main effects) with explicit inference cues for audiences likely to have low graphicacy [@shahBarLineGraph2011].
