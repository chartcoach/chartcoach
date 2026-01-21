---
id: include-verifiable-questions-to-deter-gaming-in-crowdsourced-chart-judgments
title: Add Verifiable Checks So Incorrect Work Is Easy to Detect
bibliography: references.bib
description: Use questions with objectively checkable answers to discourage gaming
  and enable rejecting invalid submissions.
labels:
- chart:multiple
- task:answer
- visual:multiple
- impact:data-quality
- data:quantitative
- audience:researcher
- method:crowdsourcing
---

## The Rule <!-- role: advice -->

Include at least one verifiable component in each trial (or task block) so obviously incorrect responses can be rejected.

## The Logic <!-- role: reason -->

Heer & Bostock used verifiable questions (e.g., “which marked value is smaller?”) to validate responses, finding extremely low wrong-answer rates (e.g., 0.4%) and enabling clean filtering of invalid work [@heerCrowdsourcingGraphicalPerception2010a]. Verifiable elements discourage gaming because blatantly wrong answers can be rejected without ambiguity.

- **The Principle:** Auditability increases response reliability
- **The Evidence:** Very low incorrect verification responses and low outlier rejection rates across experiments [@heerCrowdsourcingGraphicalPerception2010a]

## Where to Apply <!-- role: context -->

- **User Goal:** Provide accurate estimates or settings
- **Data Type:** Tasks where a ground truth exists (value comparisons, parameter targets)
- **Audience:** Crowdsourced workers with varying motivation

## When to Break It <!-- role: exceptions -->

- **Scenario:** Tasks have no objective correctness (pure preference/likert-only).
- **Reason:** You cannot meaningfully reject work as “wrong” without ground truth.

## The Price <!-- role: costs -->

- **The Sacrifice:** Slightly longer tasks and more UI elements.
- **The Risk:** Poorly designed checks can accidentally reject valid work if ambiguous.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using “gotcha” checks unrelated to the task.
- **Why it fails:** It tests attention to trivia rather than ability to do the perceptual work and can unfairly reject participants.

## How to Check <!-- role: check -->

- **Visual Sign:** A spike of responses that violate basic constraints (e.g., choosing the larger item as “smaller”).
- **The Test:** Compute the error rate on the verifiable component; it should be near-zero if the task is clear, as in [@heerCrowdsourcingGraphicalPerception2010a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a “smaller/larger” identification step before the numeric estimate.
- **Best Fix:** Design the task so meaningful completion is as easy as cheating (simple checks plus clear rejection criteria) [@heerCrowdsourcingGraphicalPerception2010a].
