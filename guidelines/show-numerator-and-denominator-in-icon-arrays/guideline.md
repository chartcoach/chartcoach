---
id: show-numerator-and-denominator-in-icon-arrays
title: Show Both Affected and Unaffected People in Icon Arrays
bibliography: references.bib
description: Include the full population (denominator) in icon arrays to support accurate
  risk understanding and avoid numerator-only focus.
labels:
- chart:icon-array
- task:communicate-risk
- visual:part-to-whole
- impact:comprehension
- impact:transparency
- data:probability
- audience:general-public
- domain:health
---

## The Rule <!-- role: advice -->

Design icon arrays to depict the full denominator (all individuals), clearly distinguishing affected from unaffected individuals.

## The Logic <!-- role: reason -->

The study’s icon arrays were constructed as full arrays with affected individuals marked (and unaffected individuals visible), and this format improved comprehension of medical risk reduction. Showing the full denominator supports interpreting a risk as “X out of N” rather than focusing only on the numerator.

- **The Principle:** Part-to-whole visibility reduces misinterpretation of proportions
- **The Evidence:** [@galesicUsingIconArrays2009]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand baseline risk and risk with treatment as proportions of a population
- **Data Type:** Binary outcome risks (event vs no event)
- **Audience:** Broad audiences, particularly where risk literacy/numeracy varies

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are intentionally communicating only absolute counts without implying a rate (e.g., “number affected” without a reference population).
- **Reason:** The paper’s findings pertain to risk/proportion understanding; it does not evaluate numerator-only displays for other goals [@galesicUsingIconArrays2009].

## The Price <!-- role: costs -->

- **The Sacrifice:** More icons to render and more visual density
- **The Risk:** Large arrays can look busy if poorly spaced or scaled

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing only affected icons (numerator) as the “icon array”
- **Why it fails:** It removes the denominator context that supports interpreting risk as a proportion, which is central to the paper’s approach and results [@galesicUsingIconArrays2009].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers cannot tell “out of how many” the affected icons come.
- **The Test:** Ask users to state the denominator from the graphic alone; if they can’t, the display likely lacks denominator context.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add the missing denominator icons in a consistent grid and mark affected ones distinctly.
- **Best Fix:** Use a full grid-based array with a clear legend or label (e.g., “black = affected”) and keep baseline vs treatment arrays aligned [@galesicUsingIconArrays2009].
