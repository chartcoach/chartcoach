---
id: deprioritize-granularity-transitions-when-choosing-the-next-step
title: Deprioritize Granularity Shifts as the Immediate Next Slide
bibliography: references.bib
description: When selecting the next visualization at equal cost, prefer temporal
  or comparison transitions over granularity changes.
labels:
- task:sequence
- task:drill-down
- impact:preference
- audience:general
- complexity:basic
---

## The Rule <!-- role: advice -->

When choosing what comes next (and the alternatives are equal-cost, single-change transitions), do not default to a general-to-specific or specific-to-general shift; prefer temporal or comparison transitions first.

## The Logic <!-- role: reason -->

In cost-constant choices, granularity transitions were less preferred than temporal transitions and less preferred than both dimension and measure walks, suggesting drill-down/roll-up steps are not as favored as immediate adjacency moves in a linear narrative [@hullmanDeeperUnderstandingSequence2013].

- **The Principle:** Transition-type preference influences perceived fit
- **The Evidence:** Type ranking from the study: Temporal > (Dimension | Measure) > Granularity [@hullmanDeeperUnderstandingSequence2013].

## Where to Apply <!-- role: context -->

- **User Goal:** Decide which of several “one-step” options should follow the current slide
- **Data Type:** Hierarchical or filterable data (e.g., country → region → city; overview → filtered subset)
- **Audience:** General audiences in slideshow-style stories

## When to Break It <!-- role: exceptions -->

- **Scenario:** The narrative goal is explicitly “overview then detail” as the central rhetorical structure.
- **Reason:** The paper reports average preferences, not that granularity transitions are ineffective—only that they are less preferred than other equal-cost moves [@hullmanDeeperUnderstandingSequence2013].

## The Price <!-- role: costs -->

- **The Sacrifice:** You might postpone details that could answer stakeholder questions quickly.
- **The Risk:** If you never drill down, the story can remain too abstract.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using repeated zoom/filter steps as the primary way to move the story forward.
- **Why it fails:** Users preferred other transition types over granularity in direct next-step selection at equal cost [@hullmanDeeperUnderstandingSequence2013].

## How to Check <!-- role: check -->

- **Visual Sign:** The story repeatedly alternates between “overview” and “detail” even when time or a consistent comparison could connect slides.
- **The Test:** For each adjacency choice, if a temporal or comparison step exists at the same cost, choose it over granularity.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap slide order so drill-down/roll-up happens after establishing context through time or comparison.
- **Best Fix:** Use granularity changes sparingly and place them where “detail” is the intended payoff rather than the default connective tissue [@hullmanDeeperUnderstandingSequence2013].
