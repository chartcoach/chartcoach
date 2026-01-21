---
id: validate-crowdsourced-perception-by-replicating-lab-results
title: Replicate Known Lab Studies Before Trusting Crowdsourced Perception Data
bibliography: references.bib
description: Establish credibility of crowdsourced graphical perception experiments
  by reproducing benchmark lab findings first.
labels:
- chart:multiple
- task:evaluate
- visual:multiple
- impact:validity
- data:quantitative
- audience:researcher
- method:crowdsourcing
---

## The Rule <!-- role: advice -->

Replicate at least one established laboratory graphical-perception result on your crowdsourcing platform before using it to justify new visualization design conclusions.

## The Logic <!-- role: reason -->

Crowdsourced perception studies lose control over display type, lighting, and viewing distance, so the platform must be validated empirically. Heer & Bostock successfully replicated classic lab findings on spatial encodings and alpha-contrast gridlines using Mechanical Turk, showing that key rankings and statistical effects can match prior work despite higher variance [@heerCrowdsourcingGraphicalPerception2010a].

- **The Principle:** External validity through replication
- **The Evidence:** Replications of Cleveland & McGill and Stone & Bartram effects on MTurk [@heerCrowdsourcingGraphicalPerception2010a]

## Where to Apply <!-- role: context -->

- **User Goal:** Use perception results to choose encodings or parameter defaults
- **Data Type:** Quantitative comparisons (percent judgments, contrast settings)
- **Audience:** Visualization researchers and tool builders using crowdsourcing

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are not making generalizable perception claims (e.g., only collecting qualitative feedback).
- **Reason:** Replication is unnecessary if you are not inferring perceptual effectiveness from the crowd.

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional time and budget to run a benchmark replication.
- **The Risk:** If your replication fails, you must redesign the task or abandon conclusions.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Running only novel conditions and assuming crowdsourced results are reliable.
- **Why it fails:** Without a benchmark, uncontrolled display/environment factors may shift results without detection [@heerCrowdsourcingGraphicalPerception2010a].

## How to Check <!-- role: check -->

- **Visual Sign:** Your effect directions/rankings differ from canonical findings (e.g., position not outperforming length).
- **The Test:** Include an overlapped condition from a published lab study and confirm the same qualitative conclusion holds [@heerCrowdsourcingGraphicalPerception2010a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a small set of benchmark trials (one known effect) alongside your novel trials.
- **Best Fix:** Fully replicate a prior study’s key conditions first, then extend with new factors only after the replication matches [@heerCrowdsourcingGraphicalPerception2010a].
