---
id: use-qualification-tasks-to-prevent-misunderstanding-in-crowdsourced-vis-studies
title: Require a Qualification Task to Ensure Participants Understand the Chart Judgment
  Task
bibliography: references.bib
description: Use brief qualification quizzes to prevent unusable responses caused
  by instruction misunderstanding.
labels:
- chart:multiple
- task:judge
- visual:multiple
- impact:data-quality
- data:quantitative
- audience:researcher
- method:crowdsourcing
---

## The Rule <!-- role: advice -->

Gate participation with a short qualification task that verifies users can interpret the stimulus and follow instructions before they see real trials.

## The Logic <!-- role: reason -->

In Heer & Bostock’s MTurk replications, omitting qualification led to over 10% unusable responses; adding qualification reduced incorrect/verifiably wrong responses to well under 1% across studies [@heerCrowdsourcingGraphicalPerception2010a]. The qualification is not to select “good perceivers,” but to remove confusion about task format.

- **The Principle:** Reduce instruction-induced noise
- **The Evidence:** Pilot without qualification produced >10% unusable responses; qualified runs had ~0.4–1.6% removed as outliers/invalid [@heerCrowdsourcingGraphicalPerception2010a]

## Where to Apply <!-- role: context -->

- **User Goal:** Accurate perceptual judgments (percent estimation, differences, parameter adjustment)
- **Data Type:** Quantitative values encoded visually
- **Audience:** Crowdsourced participants unfamiliar with study conventions

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is trivially self-evident and has no specialized response format.
- **Reason:** Qualification overhead may be unnecessary if misunderstanding risk is minimal.

## The Price <!-- role: costs -->

- **The Sacrifice:** Extra engineering/design work and some participant drop-off.
- **The Risk:** Overly “training” qualifications may bias responses if they teach strategies rather than format.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a qualification that filters for accuracy on the actual perceptual variable.
- **Why it fails:** It can bias the sample by excluding legitimately variable perception rather than excluding confusion [@heerCrowdsourcingGraphicalPerception2010a].

## How to Check <!-- role: check -->

- **Visual Sign:** Many nonsensical entries (empty, non-numeric, wildly out-of-range) or wrong answers on easy verification items.
- **The Test:** Run a small pilot with and without qualification and compare unusable-response rate as Heer & Bostock did [@heerCrowdsourcingGraphicalPerception2010a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add 2 labeled examples plus 2–3 multiple-choice checks where wrong options are “grossly wrong.”
- **Best Fix:** Add a qualification tailored to the interaction modality (e.g., confirm the user can set alpha to 0 and 1 in an interactive contrast task) [@heerCrowdsourcingGraphicalPerception2010a].
