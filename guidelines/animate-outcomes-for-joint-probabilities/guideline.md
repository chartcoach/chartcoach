---
id: animate-outcomes-for-joint-probabilities
title: Animate Hypothetical Outcomes to Convey Joint Probabilities
bibliography: references.bib
description: Use Hypothetical Outcome Plots (HOPs) instead of error bars or violin
  plots when users need to assess the reliability of variable ordering.
labels:
- chart:hypothetical-outcome-plot
- chart:error-bar
- chart:violin-plot
- task:compare
- task:estimate-probability
- visual:animation
- impact:accuracy
- audience:novice
- data:distribution
---

## The Rule <!-- role: advice -->
When asking users to estimate the probability that one variable is larger than another (e.g., $P(B > A)$) or larger than multiple others, use animated Hypothetical Outcome Plots (HOPs) rather than static error bars or violin plots.

## The Logic <!-- role: reason -->
Static representations of distributions, such as error bars and violin plots, require viewers to possess statistical background knowledge and perform complex visual integrations to understand joint probabilities (the relationship between two variables). In contrast, [@hullman_hypothetical_2015] demonstrate that HOPs—which animate a finite set of individual draws from a distribution—allow viewers to use "finite" thinking strategies. Users can simply count the number of times one bar is higher than another across frames (e.g., "B is higher than A in most frames") rather than abstracting over probability densities. This significantly improves accuracy for inferences about variable ordering.

## Where to Apply <!-- role: context -->
*   **User Goal:** Assessing the reliability of variable ordering (e.g., "Is Treatment B reliably better than Treatment A?") or comparing multivariate distributions.
*   **Data Type:** Two or more random variables (independent or correlated).
*   **Audience:** Both lay readers and those with some statistical knowledge, as both groups struggle with static uncertainty abstractions.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The primary task is estimating the specific mean of a single variable with high variance.
*   **Reason:** [@hullman_hypothetical_2015] found that for univariate mean estimation in high-variance conditions, static error bars performed better because visually integrating a line jumping over large distances is difficult.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Precision in viewing the complete distribution structure at a glance.
*   **The Risk:** Users view only a finite number of draws, introducing sampling error. They may get an imprecise picture if they do not watch enough frames.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using overlapping error bars to imply significance or non-significance.
*   **Why it fails:** Viewers consistently misinterpret the statistical meaning of overlapping intervals and struggle to derive $P(B > A)$ from them [@hullman_hypothetical_2015].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you displaying static intervals (error bars) or shapes (violins) for a task asking "How often is X > Y"?
*   **The Test:** Ask a user to estimate the probability that B > A. If they resort to heuristics about the overlap of the bars, the static representation is failing.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Replace the static error bar with a text annotation stating the probability (e.g., "B is greater than A in 95% of cases").
*   **Best Fix:** Implement an animated HOP where the bar height changes to reflect individual draws from the underlying distribution, looping through a set of outcomes.
