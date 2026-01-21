---
id: tailor-quantitative-information-to-personal-relevance
title: Tailor Quantitative Information to Include Only Personally Relevant Facts
bibliography: references.bib
description: Reduce document complexity and improve comprehension by tailoring quantitative
  content to the individual.
labels:
- task:decide
- impact:clarity
- impact:usability
- audience:general-public
- domain:health
- artifact:decision-aid
- source:ancker-2007
---

## The Rule <!-- role: advice -->

Tailor patient-facing quantitative information so it contains only facts relevant to that person and decision.

## The Logic <!-- role: reason -->

Tailoring reduces document-literacy burden by removing irrelevant material and presenting manageable chunks, supporting better comprehension and decision-making.

- **The Principle:** Reducing document demands via tailored content
- **The Evidence:** [@anckerRethinkingHealthNumeracy2007]

## Where to Apply <!-- role: context -->

- **User Goal:** Making screening/treatment choices with decision aids or portals
- **Data Type:** Risk estimates, option comparisons, personalized values/data
- **Audience:** Patients who may be overwhelmed by dense, generic quantitative content [@anckerRethinkingHealthNumeracy2007]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Users need broad, non-personal educational context (e.g., learning general concepts).
- **Reason:** Over-tailoring can hide important background or alternatives. [@anckerRethinkingHealthNumeracy2007]

## The Price <!-- role: costs -->

- **The Sacrifice:** Engineering and content effort to collect inputs and generate personalized outputs
- **The Risk:** Incorrect tailoring inputs can produce misleading recommendations or numbers [@anckerRethinkingHealthNumeracy2007]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Providing the same dense table to everyone and expecting users to pick what applies.
- **Why it fails:** Selecting relevant facts is a major source of error in document-based quantitative tasks. [@anckerRethinkingHealthNumeracy2007]

## How to Check <!-- role: check -->

- **Visual Sign:** Users skip content, miss key numbers, or can’t identify which numbers apply to them.
- **The Test:** Ask users “Which of these numbers is about you?”; confusion indicates insufficient tailoring. [@anckerRethinkingHealthNumeracy2007]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reorder and collapse sections to highlight personally relevant fields first.
- **Best Fix:** Build a tailored workflow that requests key inputs and outputs only the personalized quantitative facts needed for the decision. [@anckerRethinkingHealthNumeracy2007]
