---
id: standardize-effect-format-across-endpoints
title: Use the Same Effect Format Across Endpoints
bibliography: references.bib
description: Present all endpoints using the same effect measures to avoid inconsistent
  interpretation and decisions.
labels:
- chart:table
- task:compare
- visual:consistency
- impact:clarity
- data:risk
- audience:expert
- domain:clinical-trials
---

## The Rule <!-- role: advice -->

Within a report, present each endpoint using a **consistent set of effect measures** (e.g., always include relative risk + absolute risk, or always include absolute risk + NNT), rather than mixing formats across outcomes.

## The Logic <!-- role: reason -->

Because physicians’ perceived effectiveness and treatment inclination changed when identical outcomes were described using different measures, mixing formats across endpoints can cause readers to over-weight outcomes framed as relative risk and under-weight others, creating inconsistent judgments [@bucherInfluenceMethodReporting1994].

- **The Principle:** Framing effects differently across outcomes introduces avoidable interpretation variance.
- **The Evidence:** The same underlying trial data produced different ratings and treatment inclinations depending on whether results were expressed as relative risk reduction, absolute risk reduction, or NNT [@bucherInfluenceMethodReporting1994].

## Where to Apply <!-- role: context -->

- **User Goal:** Compare benefits and harms across multiple endpoints (e.g., non-fatal MI, fatal MI, all-cause mortality).
- **Data Type:** Multi-endpoint trial summaries, abstracts, evidence tables, guideline summaries.
- **Audience:** Clinicians interpreting overall net benefit.

## When to Break It <!-- role: exceptions -->

- **Scenario:** A specific endpoint cannot support a measure (e.g., insufficient data to compute NNT for that endpoint).
- **Reason:** Consistency should not force fabrication; instead, omit the unavailable measure and explain why.

## The Price <!-- role: costs -->

- **The Sacrifice:** More complex tables/figures and longer text.
- **The Risk:** Overly dense presentation if not structured clearly (e.g., too many columns).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Headlining relative risk for “positive” outcomes while using absolute numbers only for neutral/negative outcomes.
- **Why it fails:** Relative-risk framing increased perceived effectiveness and willingness to treat in the experiment, so selective use can bias impressions [@bucherInfluenceMethodReporting1994].

## How to Check <!-- role: check -->

- **Visual Sign:** One endpoint is described in “% relative risk reduction” while another is “events per 1000,” with no parallel measure.
- **The Test:** Scan each endpoint row/paragraph and confirm the same effect fields appear for every endpoint.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add the missing complementary measure(s) for endpoints currently presented in only one format.
- **Best Fix:** Build a uniform endpoint table where each endpoint is reported in the same measure set and time horizon, as implied by the differential responses observed in [@bucherInfluenceMethodReporting1994].
