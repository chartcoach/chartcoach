---
id: define-and-operationalize-stakeholder-insight-needs-first
title: Operationalize Stakeholder Insight Needs Before You Touch the Data
bibliography: references.bib
description: Translate stakeholder questions into explicit insight needs to guide
  every later visualization decision.
labels:
- task:categorize
- task:rank
- task:compare
- task:trend
- task:correlate
- impact:clarity
- audience:novice
- audience:expert
- source:borner-2019
---

## The Rule <!-- role: advice -->

Operationalize the stakeholder’s real-world problem into one or more explicit insight needs (e.g., compare, rank, find trends) before selecting data, analyses, or chart types.

## The Logic <!-- role: reason -->

Unclear goals lead to mismatched analyses and encodings; the framework treats insight needs as the first constraint that structures the whole workflow from acquisition through interpretation.

- **The Principle:** Insight-need–driven visualization workflow
- **The Evidence:** [@bornerDataVisualizationLiteracy2019]

## Where to Apply <!-- role: context -->

- **User Goal:** Any sensemaking or communication task where “what are we trying to learn?” is still ambiguous
- **Data Type:** Any (the insight need determines what data and transformations are required)
- **Audience:** Analysts, designers, or students working from stakeholder prompts

## When to Break It <!-- role: exceptions -->

- **Scenario:** Exploratory work where the goal is explicitly “discover possible questions”
- **Reason:** You may iterate, but you still need to record provisional insight needs as you go so later choices are assessable [@bornerDataVisualizationLiteracy2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Extra up-front time and stakeholder back-and-forth
- **The Risk:** Overconstraining exploration if you lock into a single need too early

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Picking a favorite chart first and retrofitting a question to it
- **Why it fails:** It reverses the paper’s workflow ordering and commonly yields irrelevant or misleading outputs [@bornerDataVisualizationLiteracy2019].

## How to Check <!-- role: check -->

- **Visual Sign:** The chart “looks nice” but nobody can say what decision it supports.
- **The Test:** Ask: “Which insight need(s) from the framework does this answer?” If you can’t name them, the problem wasn’t operationalized [@bornerDataVisualizationLiteracy2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Write a one-sentence question that maps to a single insight need (e.g., “Which category is largest?” → comparison).
- **Best Fix:** List all stakeholders, enumerate their insight needs, and treat them as requirements that drive data acquisition, analysis, and visualization choices [@bornerDataVisualizationLiteracy2019].
