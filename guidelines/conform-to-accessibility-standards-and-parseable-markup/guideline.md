---
id: conform-to-accessibility-standards-and-parseable-markup
title: Conform to Accessibility Standards
bibliography: references.bib
description: Ensure charts meet applicable accessibility standards and use unambiguous,
  parseable markup so assistive technologies can interpret them reliably.
labels:
- chart:any
- task:audit
- visual:any
- impact:accessibility
- data:any
- audience:practitioner
- principle:robust
- source:chartability
---

## The Rule <!-- role: advice -->

Make the chart conform to all applicable accessibility standards (e.g., WCAG 2.1, Section 508, or equivalent) and treat it as a failure until it has been fully evaluated for compliance [@elavskyHowAccessibleMy2022].

## The Logic <!-- role: reason -->

Standards compliance increases the likelihood that the chart will work with users’ assistive technologies by ensuring content is implemented in ways that can be interpreted consistently.

- **The Principle:** Robust compatibility through unambiguous parsing and standards-aligned implementation
- **The Evidence:** Content should use markup that can be unambiguously parsed (e.g., proper nesting and unique start/end tags) so assistive technologies can interpret it reliably [@w3c_understanding_ensure], and Chartability frames standards conformance as a Robust requirement for accessible data experiences [@elavskyHowAccessibleMy2022].

## Where to Apply <!-- role: context -->

Use this rule whenever you publish or ship a chart or data interface where people may rely on assistive technology.

- **User Goal:** Access and operate the chart using their assistive technologies of choice
- **Data Type:** Any (because standards conformance is implementation-dependent rather than data-dependent) [@elavskyHowAccessibleMy2022]
- **Audience:** Designers, developers, and auditors evaluating visualization accessibility [@elavskyHowAccessibleMy2022]

## When to Break It <!-- role: exceptions -->

Do not break this rule; instead, limit your claims.

- **Scenario:** An early prototype or internal draft where a full standards evaluation has not been performed yet
- **Reason:** You may proceed for iteration speed, but you must not claim the chart is accessible or compliant until it is evaluated against applicable requirements [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

Following standards conformance requirements adds process and verification overhead.

- **The Sacrifice:** More time spent auditing against standards and validating implementation details [@elavskyHowAccessibleMy2022]
- **The Risk:** If you rely on assumptions instead of evaluation, you may ship charts that fail compatibility expectations for assistive technologies (i.e., a Robust failure) [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Claiming accessibility because the chart “looks fine” visually or because a subset of checks passed
- **Why it fails:** Chartability treats standards conformance as a baseline Robust requirement; without full evaluation, you cannot know the chart meets applicable requirements [@elavskyHowAccessibleMy2022].
- **The Wrong Fix:** Using markup that is difficult for assistive technologies to interpret (e.g., ambiguous structure)
- **Why it fails:** If markup cannot be unambiguously parsed, assistive technologies may interpret content inconsistently or unreliably [@w3c_understanding_ensure].

## How to Check <!-- role: check -->

- **Visual Sign:** You cannot credibly state which standards the chart meets, or you have not evaluated it against relevant requirements (treat as an automatic failure) [@elavskyHowAccessibleMy2022].
- **The Test:** Audit the chart against all relevant WCAG 2.1, Section 508, or equivalent requirements and verify the implementation uses unambiguous, parseable markup that assistive technologies can interpret reliably [@w3c_understanding_ensure] [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Do not claim compliance; label the chart as not yet evaluated and schedule a standards-based audit as required by Chartability’s Robust guidance [@elavskyHowAccessibleMy2022].
- **Best Fix:** Bring the chart into conformance with all applicable standards and ensure the underlying markup is unambiguously parseable so assistive technologies can interpret content consistently and reliably [@w3c_understanding_ensure] [@elavskyHowAccessibleMy2022].
