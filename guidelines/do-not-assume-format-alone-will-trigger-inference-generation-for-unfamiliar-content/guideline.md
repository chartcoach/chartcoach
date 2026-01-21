---
id: do-not-assume-format-alone-will-trigger-inference-generation-for-unfamiliar-content
title: Do Not Rely on Chart Format Alone to Elicit Inferences for Unfamiliar Content
bibliography: references.bib
description: When topics are unfamiliar, viewers rely more on salient surface patterns
  and generate fewer main-effect inferences.
labels:
- chart:bar
- chart:line
- task:infer
- impact:comprehension
- data:multivariate
- audience:general
- custom:content-familiarity
- complexity:medium
- source:shah-freedman-2011
---

## The Rule <!-- role: advice -->

If the variables/topic are unfamiliar to your audience, do not expect the chart type by itself to produce main-effect inferences; plan to support inference-making explicitly.

## The Logic <!-- role: reason -->

Unfamiliar content reduces expectation-driven goal setting and makes viewers more likely to lean on bottom-up salience (e.g., visually prominent interaction patterns) rather than compute aggregations needed for main effects.

- **The Principle:** With low content familiarity, viewers default to surface-driven interpretation over inference generation.
- **The Evidence:** Viewers made far fewer main-effect inferences for unfamiliar graphs than familiar graphs, and were somewhat more likely to describe interactions for unfamiliar content [@shahBarLineGraph2011].

## Where to Apply <!-- role: context -->

- **User Goal:** Reach correct high-level takeaways (e.g., main effects) from complex graphs.
- **Data Type:** Three-variable graphs where inference requires mental aggregation.
- **Audience:** Novices to the topic/domain (unfamiliar variable names; low expectations).

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your only objective is to have viewers report the most visually salient pattern, regardless of whether it is a main effect.
- **Reason:** For unfamiliar content, salience-driven interaction descriptions may be sufficient for the task [@shahBarLineGraph2011].

## The Price <!-- role: costs -->

- **The Sacrifice:** Added explanatory support can reduce brevity and increase design/authoring effort.
- **The Risk:** Without support, viewers may produce “minimally digested” interpretations dominated by salient patterns rather than intended inferences [@shahBarLineGraph2011].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Swapping bar ↔ line expecting unfamiliar audiences to suddenly infer main effects.
- **Why it fails:** The familiarity gap remains; viewers still tend to rely on bottom-up cues instead of computing aggregates [@shahBarLineGraph2011].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers’ summaries describe conditional/trend patterns but omit overall statements.
- **The Test:** Compare summaries from a familiar vs unfamiliar audience; if unfamiliar users rarely state main effects, format alone isn’t enough [@shahBarLineGraph2011].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Provide explicit instructions/questions that ask for overall differences (main effects).
- **Best Fix:** Pair a supportive format (often bars for main effects) with guidance that tells viewers what kind of inference to make [@shahBarLineGraph2011].
