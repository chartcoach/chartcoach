---
id: use-paired-icon-arrays-for-treated-vs-untreated-comparisons
title: Show Treated and Untreated Groups as Separate Paired Icon Arrays
bibliography: references.bib
description: Use one icon array per option (e.g., treated vs. untreated) to support
  accurate comparisons of medical risks.
labels:
- chart:icon-array
- task:compare
- visual:small-multiples
- impact:clarity
- data:two-groups
- audience:patients
- bias:denominator-neglect
- domain:health
---

## The Rule <!-- role: advice -->

When communicating risk reduction across two options, show one icon array for the treated group and a separate icon array for the untreated group.

## The Logic <!-- role: reason -->

Separating options into distinct icon arrays makes each option’s “whole” visible, helping viewers compare proportions rather than raw event counts. Across the reviewed studies, icon arrays accompanying numeric descriptions reduced denominator neglect and improved correctness of risk reduction estimates with unequal denominators [@garcia-retameroUsingVisualAids2012].

## Where to Apply <!-- role: context -->

- **User Goal:** Compare two medical options (take treatment vs. not take treatment).
- **Data Type:** Two proportions that may have different denominators (unequal group sizes).
- **Audience:** Patients and lay decision-makers, including those prone to focusing on absolute counts.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The decision problem is not comparative (only one option/risk) and the denominator is already transparent and fixed.
- **Reason:** The main benefit described in the review is reducing errors that arise when comparing options with unequal denominators [@garcia-retameroUsingVisualAids2012].

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires more layout space than a single combined graphic.
- **The Risk:** If viewers have low graph literacy, the added graphics may not yield full benefits [@garcia-retameroUsingVisualAids2012].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Combining both groups into one undifferentiated display or presenting only the two numerators side-by-side.
- **Why it fails:** It can keep attention on numerators and obscure the denominators, reinforcing denominator neglect [@garcia-retameroUsingVisualAids2012].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers can easily point to “how many total” and “how many affected” for each option separately.
- **The Test:** Ask viewers to compute or describe which option has the lower risk in proportional terms; frequent numerator-based answers indicate the pairing isn’t working [@garcia-retameroUsingVisualAids2012].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Split a single display into two labeled panels (treated vs. untreated).
- **Best Fix:** Use two clearly separated icon arrays with consistent highlighting of affected individuals and explicit totals [@garcia-retameroUsingVisualAids2012].
