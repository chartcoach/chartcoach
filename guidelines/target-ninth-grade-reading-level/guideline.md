---
id: target-ninth-grade-reading-level
title: Write All Chart Text at a Ninth-Grade Reading Level or Lower
bibliography: references.bib
description: Keep all chart text, including alternative text, at grade 9 reading level
  or below, and define any necessary jargon in simple language.
labels:
- chart:general
- task:understand
- visual:text
- impact:accessibility
- data:any
- audience:general
- source:chartability
---

## The Rule <!-- role: advice -->

Write all user-facing text in the data experience—including captions, instructions, annotations, labels, and alternative text—at a reading grade level of 9 or lower [@elavskyHowAccessibleMy2022]. If you must use complex or unfamiliar terms, provide clear definitions or supplementary explanations written at grade 9 or below [@w3c_understanding_meaningful].

## The Logic <!-- role: reason -->

Reducing reading complexity lowers cognitive load and makes written explanations and supports (including definitions for unfamiliar terms) more reliably understandable to a broader range of readers, including people with cognitive disabilities [@w3c_understanding_meaningful].

- **The Principle:** Minimize cognitive load by simplifying language and supplementing unfamiliar terms.
- **The Evidence:** Chartability’s “Reading level inappropriate” heuristic requires grade 9 or lower for all text and alt text [@elavskyHowAccessibleMy2022], and WCAG guidance recommends providing definitions/supplements for complex or unfamiliar terms to support understanding [@w3c_understanding_meaningful].

## Where to Apply <!-- role: context -->

This advice is designed for any visualization or data interface that includes text meant to explain, guide, or summarize.

- **User Goal:** Understand what the chart shows and how to interpret it without ambiguity.
- **Data Type:** Any (since the rule governs explanatory text, not encoding).
- **Audience:** General audiences, including readers who benefit from simpler language or supplementary definitions [@elavskyHowAccessibleMy2022].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The domain requires specialized terminology (e.g., technical, legal, medical, or scientific terms).
- **Reason:** Some terms cannot be simplified without changing meaning; in these cases, keep the specialized term but add simple, grade-9-or-lower definitions or supplementary explanations [@elavskyHowAccessibleMy2022] [@w3c_understanding_meaningful].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less concise or less technical-sounding prose; additional space/time needed for definitions or supplementary text.
- **The Risk:** Over-simplifying can remove nuance if complex terms are replaced instead of being defined accurately; supplementary text can lengthen the experience [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping the original complex copy and only adding more dense text.
- **Why it fails:** More text that is still complex increases cognitive load rather than reducing it, and does not provide meaningful supplementation for unfamiliar terms [@w3c_understanding_meaningful].
- **The Wrong Fix:** Simplifying visible text but leaving alternative text (or other hidden/supporting text) at a higher reading level.
- **Why it fails:** Chartability requires the grade-9 threshold for all text, including alternative text [@elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Captions, instructions, or descriptions contain long, dense sentences; heavy jargon; or unexplained specialized terms.
- **The Test:** Run all chart text (including alternative text) through a readability tool that estimates grade level and verify the result is grade 9 or below [@hemingwayapp_hemingway_editor] [@elavskyHowAccessibleMy2022]. If specialized terms appear, verify they have accompanying definitions or supplements written at grade 9 or below [@w3c_understanding_meaningful].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Use a readability tool to identify complex sentences/wording and rewrite until the text evaluates to grade 9 or below; keep meaning intact while shortening sentences and simplifying phrasing [@hemingwayapp_hemingway_editor] [@elavskyHowAccessibleMy2022].
- **Best Fix:** Keep any required technical terms, but add short, clear definitions or supplementary explanations in grade-9-or-lower language so readers can understand unfamiliar terminology without leaving the experience [@w3c_understanding_meaningful] [@elavskyHowAccessibleMy2022].
