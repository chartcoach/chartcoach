---
id: seed-collaborative-visualizations-accurately
title: Seed Collaborative Visualizations with Accurate Anchors
bibliography: references.bib
description: Ensure the first few interactions on a social visualization are accurate
  to prevent erroneous information cascades.
labels:
- impact:bias
- task:collaborate
- source:social-signals
- audience:community
---

## The Rule <!-- role: advice -->
Ensure the initial responses or annotations displayed on a collaborative visualization are accurate, or "seed" the system with correct examples before opening it to the public.

## The Logic <!-- role: reason -->
Social systems are subject to information cascades where early inputs define the behavior of future users.
*   **The Principle:** **Information Cascades.** Early biases are not corrected by subsequent users; they are amplified.
*   **The Evidence:** @hullman_impact_2011 demonstrated that a user's judgment is heavily influenced by the *distribution* of previous answers, but notably **not** by the *number* of people who gave them. An erroneous signal from 5 people was roughly as influential as an erroneous signal from 30 people. The first few inputs set the stage for all subsequent judgments.

## Where to Apply <!-- role: context -->
*   **User Goal:** Interpreting data in a public forum or crowdsourcing platform.
*   **System Type:** Asynchronous collaborative visualization tools where users see a history of interaction (e.g., "50 people tagged this point").

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The visualization is purely subjective (e.g., "How does this art make you feel?").
*   **Reason:** In subjective contexts, there is no "accurate" ground truth to anchor against, and social influence is a feature of community sentiment rather than a bug in data perception.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Requires active moderation or automated "bot" seeds to establish a baseline.
*   **The Risk:** "Seeding" data might be viewed as manipulative if not disclosed.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Displaying social metrics (like participation counts) to imply reliability.
*   **Why it fails:** @hullman_impact_2011 found that increasing the perceived number of participants ($n$) did not significantly change the weight users placed on the social signal. Users trusted a small group of wrong people just as much as a large group.

## How to Check <!-- role: check -->
*   **Visual Sign:** Look at the first 5-10 comments or annotations on a chart. Are they factually correct?
*   **The Test:** If the first few comments claim a correlation is "high" when it is statistically "low," monitor if subsequent users parrot this inaccuracy.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Manually review and remove clearly erroneous early annotations.
*   **Best Fix:** Implement a "warming up" period where the visualization is only visible to expert reviewers (or automated systems) to generate a baseline of accurate social signals before general release.
