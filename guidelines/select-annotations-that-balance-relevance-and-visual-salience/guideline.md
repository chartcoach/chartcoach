---
id: select-annotations-that-balance-relevance-and-visual-salience
title: Balance Topical Relevance with Visual Salience When Choosing Annotations
bibliography: references.bib
description: Choose annotations that are both relevant to the accompanying article
  and aligned with visually salient moments in the chart.
labels:
- chart:line
- task:select
- visual:annotation
- impact:engagement
- data:temporal
- audience:general
- domain:finance
---

## The Rule <!-- role: advice -->

Select annotations using both (1) topical relevance to the context article and (2) visual salience of the charted data, rather than relying on only one of these criteria.

## The Logic <!-- role: reason -->

Relevance-driven selection supports “aboutness” (the annotations match the story), while salience-driven selection supports attention and perceived explanation of chart behavior; the paper’s evaluation shows each improves its corresponding user-rated outcome over random selection, and combining them creates a practical tradeoff.

- **The Principle:** Multi-objective annotation improves both topical fit and alignment with attention-driving chart features.
- **The Evidence:** In user ratings, relevance-based charts were rated significantly more relevant than random, and salience-based charts were rated significantly better at explaining trends/oscillations than relevance-only or random; combined scoring improved over random but reflected a tradeoff relative to optimizing either objective alone [@hullmanContextifierAutomaticGeneration2013].

## Where to Apply <!-- role: context -->

- **User Goal:** Get context that is simultaneously about the article and informative about what the chart is doing.
- **Data Type:** Time series paired with time-indexed external content (e.g., news articles by date/week).
- **Audience:** Readers who will skim annotations and visually inspect chart movement.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The visualization is meant to be purely story-driven (topical context dominates) or purely data-driven (trend explanation dominates).
- **Reason:** Single-objective selection may be appropriate when the communication goal explicitly prioritizes one dimension over the other [@hullmanContextifierAutomaticGeneration2013].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may not maximize either relevance or salience perfectly.
- **The Risk:** If weighting between objectives is poorly chosen, the result can feel neither strongly relevant nor strongly explanatory [@hullmanContextifierAutomaticGeneration2013].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Selecting annotations only from visually extreme points (e.g., peaks/troughs) regardless of story topic.
- **Why it fails:** Users may see the chart as better “explained” but not relevant to the article’s topic [@hullmanContextifierAutomaticGeneration2013].
- **The Wrong Fix:** Selecting annotations only by text similarity and ignoring chart behavior.
- **Why it fails:** Users may perceive annotations as disconnected from the most attention-grabbing parts of the graph [@hullmanContextifierAutomaticGeneration2013].

## How to Check <!-- role: check -->

- **Visual Sign:** Many annotations cluster where the line is visually flat (relevance-only failure) or where major moves occur but the headlines feel off-topic (salience-only failure).
- **The Test:** For each annotation, verify (a) it shares key terms/themes with the input article snippet and (b) it aligns to a week/day with notable chart movement.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Re-rank candidate annotations by adding a second criterion (relevance or salience) and select from the top combined set.
- **Best Fix:** Use an explicit weighted integration of relevance and salience (and optionally news volume) and tune weights for the intended use case [@hullmanContextifierAutomaticGeneration2013].
