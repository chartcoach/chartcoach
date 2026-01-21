---
id: simplify-quantitative-documents-by-removing-extraneous-information
title: Remove Extraneous Details from Quantitative Patient Documents
bibliography: references.bib
description: Reduce document-literacy burden by stripping irrelevant complexity and
  highlighting what users must act on.
labels:
- task:find
- task:calculate
- impact:clarity
- impact:accessibility
- audience:general-public
- domain:health
- artifact:document
- source:ancker-2007
---

## The Rule <!-- role: advice -->

In patient-facing quantitative documents (e.g., labels), remove nonessential information and foreground the numbers needed for the task.

## The Logic <!-- role: reason -->

Many errors come from navigation, selecting relevant numbers, and choosing the right operation—not just arithmetic—so simplifying the document reduces document-literacy demands.

- **The Principle:** Document literacy as a limiting factor in quantitative tasks
- **The Evidence:** [@anckerRethinkingHealthNumeracy2007]

## Where to Apply <!-- role: context -->

- **User Goal:** Extracting and using numbers correctly (e.g., doses, nutrition totals)
- **Data Type:** Tables, labels, multi-field forms, mixed text-and-number layouts
- **Audience:** Patients with varying literacy/numeracy, especially those prone to misapplying serving size or including extraneous fields [@anckerRethinkingHealthNumeracy2007]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Regulatory or clinical requirements mandate inclusion of specific fields.
- **Reason:** You may need to keep required content but can still reorder or visually de-emphasize it. [@anckerRethinkingHealthNumeracy2007]

## The Price <!-- role: costs -->

- **The Sacrifice:** Less comprehensive information density
- **The Risk:** Omitting details some users want unless you provide an “additional details” pathway [@anckerRethinkingHealthNumeracy2007]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping everything and adding bolding everywhere.
- **Why it fails:** Visual noise increases scanning difficulty and doesn’t reduce the need to decide what’s relevant. [@anckerRethinkingHealthNumeracy2007]

## How to Check <!-- role: check -->

- **Visual Sign:** Users pick the wrong number (e.g., per serving vs per container) or use irrelevant fields.
- **The Test:** Observe users doing a task (e.g., compute a total); if they hesitate over “which number to use,” the document is too complex. [@anckerRethinkingHealthNumeracy2007]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reorder content so the task-critical numbers come first and secondary numbers are separated.
- **Best Fix:** Redesign the document around the user’s tasks (e.g., include totals for the whole package and remove/relocate distracting fields). [@anckerRethinkingHealthNumeracy2007]
