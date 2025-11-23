---
id: prioritize-rates-over-nnt
title: Prioritize Rate Reductions Over NNT
bibliography: references.bib
description: Use Relative or Absolute Risk Reductions instead of Number Needed to
  Treat (NNT) for general comprehension.
labels:
- task:communicate
- visual:text
- impact:comprehension
- data:statistical
- audience:novice
---

## The Rule <!-- role: advice -->

Prioritize displaying Absolute Risk Reduction (ARR) or Relative Risk Reduction (RRR) over Number Needed to Treat (NNT) when communicating treatment efficacy to general audiences.

## The Logic <!-- role: reason -->

The "Number Needed to Treat" (the number of patients who must be treated to prevent one bad outcome) is consistently less understood and perceived as less effective than rate-based formats.
*   **The Principle:** Computational Complexity
*   **The Evidence:** RRR was better understood (SMD 0.73) and perceived as larger (SMD 1.15) than NNT. ARR was also better understood (SMD 0.42) and perceived as larger (SMD 0.79) than NNT [@akl_using_2011].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.
*   **User Goal:** Understanding the magnitude of a treatment's benefit.
*   **Data Type:** Clinical trial results or intervention outcomes.
*   **Audience:** Patients and general consumers (and even many health professionals).

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.
*   **Scenario:** Specialized clinical economic analysis.
*   **Reason:** NNT is computationally useful for resource allocation (cost to prevent one event), provided the audience is highly trained in its interpretation.

## The Price <!-- role: costs -->

Be honest about the downsides.
*   **The Sacrifice:** The "individualized" perspective. NNT attempts to show the effort required for one success, which is a practical clinical reality that rates can obscure.
*   **The Risk:** People may overestimate the likelihood that *they specifically* will benefit if looking only at rates (Risk Reduction), whereas NNT implicitly communicates that many are treated without benefit.

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.
*   **The Wrong Fix:** Using NNT because it sounds "patient-centric."
*   **Why it fails:** "1 in 50 needs to be treated" is cognitively difficult to process compared to "Risk drops by 2%."

## How to Check <!-- role: check -->

*   **Visual Sign:** Look for labels like "NNT = 25" or "1 in X needed to treat."
*   **The Test:** Ask a layperson to explain what the number means. If they struggle, the format is failing.

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Convert NNT to Absolute Risk Reduction (ARR = 1/NNT) for the primary display.
*   **Best Fix:** Present the ARR (e.g., "2 fewer people in 100 had a heart attack") and relegate NNT to a footnote or detailed technical view.
