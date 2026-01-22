---
id: conform-to-wcag-and-parses-compatibly
title: Conform to applicable accessibility standards and use unambiguous, compatible
  parsing
bibliography: references.bib
description: Ensure the chart meets all applicable accessibility requirements and
  is implemented with markup that assistive technologies can parse reliably.
labels:
- chart:all
- task:evaluate
- visual:all
- impact:accessibility
- data:any
- audience:all
- principle:robust
- standard:wcag-2-1
---

## Standards compliance and compatible parsing <!-- role: advice -->

Make the chart conform to all applicable accessibility standards (for example, Web Content Accessibility Guidelines (WCAG) 2.1, Section 508, or an equivalent standard) and implement it with markup that can be parsed unambiguously by assistive technologies.

## Why standards compliance and parsing robustness matter <!-- role: reason -->

Accessibility standards define testable requirements that increase the chance that a chart works across compliant assistive technologies and platforms, and robust parsing reduces the risk that assistive technologies interpret the same chart differently or fail to interpret it at all.

**Mechanism:** Standards-based requirements constrain implementation to interoperable patterns, and unambiguous parsing reduces variability and failure in assistive technology interpretation.

**Evidence:** Content should use markup that can be unambiguously parsed (for example, properly nested elements and non-ambiguous tags) so assistive technologies can interpret it consistently and reliably [@w3c_understanding_ensure]. Chartability treats lack of standards conformance as an automatic failure until a chart can be fully evaluated, emphasizing robust compatibility with standards and assistive technologies [@elavskyHowAccessibleMy2022].

**Notes:** This guideline supports using standards alongside Chartability-style auditing rather than replacing standards.

## Where this applies in chart authoring and delivery <!-- role: context -->

- **User Goal:** Access and use the chart’s information and functionality through a compliant assistive technology and/or accessibility settings.
- **Task:** Verify accessibility and interoperability before publishing or deploying a chart.
- **Data:** Any.
- **Chart Setting:** Any chart delivered in a standards-governed environment where WCAG 2.1, Section 508, or equivalent requirements apply.
- **Audience:** People using compliant assistive technologies and teams auditing for accessibility.
- **Success Criterion:** The chart passes all relevant accessibility requirements and does not break or change meaning due to parsing or interpretation differences.

## When not to follow it <!-- role: exceptions -->

**Break it when:** No accessibility compliance standard is applicable to the environment in which the chart is used. **Why:** The “applicable standards” set cannot be defined, so conformance cannot be evaluated against a recognized baseline.

## Tradeoffs of strict conformance gating <!-- role: costs -->

**Sacrifice:** Time and effort to run a full standards-based evaluation in addition to chart-specific checks. **Risk:** Treating “not yet evaluated” as “failed” can delay delivery even when issues are minor. **Mitigation:** Use the “automatic failure until evaluated” rule as a workflow gate rather than a final quality label.

## Common ways this fails in practice <!-- role: mistakes -->

**Mistake:** Declaring a chart “accessible” without verifying it against applicable standards. **Why it fails:** It leaves unknown gaps that a full evaluation would reveal, and Chartability treats this as an automatic failure until evaluated [@elavskyHowAccessibleMy2022].

**Mistake:** Shipping markup that is ambiguous or inconsistently structured. **Why it fails:** Assistive technologies may interpret the content inconsistently or unreliably when parsing is not unambiguous [@w3c_understanding_ensure].

## Quick checks for standards conformance and parsing <!-- role: check -->

**Failure Sign:** The chart has not been evaluated against any applicable standard, or its markup structure cannot be parsed consistently by assistive technologies. **Quick Check:** Confirm there is explicit, documented evidence that the chart was evaluated against applicable requirements (for example, WCAG 2.1 or Section 508). **Stronger Test:** Perform a full standards-based evaluation and verify that the markup is unambiguously parseable in line with compatible parsing expectations [@w3c_understanding_ensure].

## Fixes when the chart does not conform <!-- role: fix -->

- Evaluate the chart against the applicable accessibility standard set and record pass/fail results as part of the delivery process.
- Update chart implementation to use markup that can be parsed unambiguously, including properly nested elements and non-ambiguous start/end tags.
- Treat missing standards evaluation as a blocking issue until the chart can be fully evaluated, consistent with standards-gated auditing practice.
- Re-audit after changes to confirm standards conformance and parsing compatibility remain intact across updates.
