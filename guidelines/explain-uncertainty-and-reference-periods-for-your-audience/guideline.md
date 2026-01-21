---
id: explain-uncertainty-and-reference-periods-for-your-audience
title: Explain unfamiliar concepts in accompanying text
bibliography: references.bib
description: "Add short, plain-language explanations for concepts like uncertainty\
  \ ranges, scenarios, baselines, and reference periods so viewers don\u2019t misinterpret\
  \ the chart."
labels:
- chart:line
- chart:area
- task:interpret
- visual:annotation
- impact:clarity
- impact:trust
- data:uncertainty
- data:temporal
- audience:novice
- audience:general-public
---

## The Rule <!-- role: advice -->

Explain any potentially unfamiliar concept (e.g., uncertainty ranges, future scenarios, baselines/reference periods, or timeframes) in the caption or surrounding text so viewers know what it means and how to read it.

## The Logic <!-- role: reason -->

Unexplained statistical or domain conventions can be misread as errors or “unreliable data,” and unfamiliar reference periods can block interpretation altogether. A brief explanation offloads complexity from the visual while preserving correct interpretation and trust, especially for lay audiences.

- **The Principle:** Reduce concept ambiguity by pairing visual encodings with plain-language interpretation guidance.
- **The Evidence:** Viewers may misunderstand or distrust uncertainty visuals without explanation, and experts often recommend explaining uncertainty in accompanying text when it is not central [@schuster_being_2024; @schuster_who_2023]. Viewers can also be confused by unexplained baselines/reference periods (e.g., “1850–1900”), which captions can clarify [@schuster_being_2024].

## Where to Apply <!-- role: context -->

This advice is designed for charts where correct understanding depends on concepts that some viewers may not already know.

- **User Goal:** Interpret what the chart implies (not just read values), especially about risk, change, or projections.
- **Data Type:** Temporal or scenario-based data; any display with uncertainty intervals/bands, confidence ranges, projections, baselines, or reference periods.
- **Audience:** General public, mixed-expertise stakeholders, or any group where statistical conventions are not guaranteed.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The chart’s main purpose is to teach uncertainty/scenarios/baselines themselves (e.g., training materials, technical explainer articles).
- **Reason:** The explanation should be integrated into the graphic more directly (annotations, callouts, step-by-step decoding) rather than relegated to minimal surrounding text.

## The Price <!-- role: costs -->

- **The Sacrifice:** Extra words and layout space in captions or surrounding text.
- **The Risk:** Over-explaining can slow expert readers or distract from the primary message if the text becomes too long.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding an uncertainty band or scenario shading with no caption guidance (“grey area = uncertainty”) and assuming it is self-evident.
- **Why it fails:** Some viewers interpret the band as unreliability or error rather than quantified uncertainty, reducing trust and comprehension [@schuster_being_2024; @schuster_who_2023].
- **The Wrong Fix:** Using technical shorthand for baselines/timeframes (e.g., “relative to 1850–1900”) without stating what that means.
- **Why it fails:** Viewers may not know what the reference period is for, undermining interpretation [@schuster_being_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** Uncertainty/scenario elements (bands, ranges, multiple futures) or baseline references appear, but there is no plain-language caption/annotation explaining how to interpret them.
- **The Test:** Ask a non-expert to explain what the band/range/reference period means and how it should affect their conclusion; if they describe it as “the data is unreliable” or can’t explain the baseline, you need clearer text.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a one- to two-sentence caption defining the concept and how to read it (e.g., what the shaded range represents; what “1850–1900” is used for; what “scenario” means).
- **Best Fix:** Pair the caption with targeted on-chart annotations (callout pointing to the band/reference period) and a short “How to read this” line, keeping the chart clean while making the interpretation unambiguous [@schuster_being_2024; @schuster_who_2023].
