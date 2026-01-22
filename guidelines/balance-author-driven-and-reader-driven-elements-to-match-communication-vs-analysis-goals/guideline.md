---
id: balance-author-driven-and-reader-driven-elements-to-match-communication-vs-analysis-goals
title: Balance author-driven structure and reader-driven exploration to match the
  intended goal
bibliography: references.bib
description: Choose how linear, messaged, and interactive the experience should be
  based on whether you prioritize storytelling or analysis.
labels:
- chart:interactive
- task:decide
- visual:interaction
- impact:fit-for-purpose
- data:multivariate
- audience:mixed
- narrative:balance
---

## Balance author-driven and reader-driven elements to fit the goal <!-- role: advice -->

Decide explicitly how much narrative control the author retains versus how much story discovery the reader can do, and design the ordering, messaging, and interactivity to match that balance. Use more linear ordering and heavier messaging when efficient communication is the goal, and more open interaction and less prescribed ordering when analysis is the goal.

## Ordering, messaging, and interactivity jointly determine narrative control <!-- role: reason -->

Narrative visualization sits on a spectrum between strict storytelling and free-form exploration. A mismatch between the intended purpose and the control balance can produce either an over-constrained “presentation” or an under-guided “tool” that fails to communicate.

**Mechanism:** Aligning control balance to purpose ensures the user’s actions and attention are consistent with the desired outcome (comprehension versus discovery).

**Evidence:** Narrative visualizations are characterized along an author-driven to reader-driven spectrum, where author-driven designs are linear with heavy messaging and minimal interactivity, while reader-driven designs have no prescribed ordering, minimal messaging, and free interactivity [@segelNarrativeVisualizationTelling2010].

**Notes:** Hybrid structures (martini glass, interactive slideshow, drill-down story) provide common ways to strike a balance.

## When balance decisions drive design choices <!-- role: context -->

- **User Goal:** Either learn a story efficiently or explore data to discover stories.
- **Task:** Ranges from guided understanding to open-ended hypothesis generation.
- **Data:** Any, but tension is strongest for complex data with many possible views.
- **Chart Setting:** Web narratives that can incorporate both messaging and interaction.
- **Audience:** Varies; novices tend to need more author-driven scaffolding.
- **Success Criterion:** Users achieve the intended outcome without feeling lost or constrained.

## When a single extreme is appropriate <!-- role: exceptions -->

- **Break it when:** You are producing a non-interactive film/video or a fixed presentation intended to be consumed linearly. **Why:** The format already enforces author-driven control.
- **Break it when:** You are building a dedicated analysis environment for experts. **Why:** Reader-driven exploration is the primary value and imposed narrative can impede work.

## Tradeoffs of choosing a balance point <!-- role: costs -->

**Sacrifice:** Either narrative efficiency (if too reader-driven) or exploratory freedom (if too author-driven). **Risk:** Mixed signals can confuse users about whether they should read or interact. **Mitigation:** Use clear structural patterns that separate or integrate narrative and interaction deliberately.

## Common balance failures <!-- role: mistakes -->

- **Mistake:** Adding interactivity everywhere while still expecting a linear, author-led story to land. **Why it fails:** Readers can digress and miss the intended message.
- **Mistake:** Providing a dense interactive tool with minimal messaging for a general audience. **Why it fails:** Users may not know what to look for or what conclusions matter.

## Checks for purpose-fit <!-- role: check -->

**Failure Sign:** Users describe the experience as “a tool” when it was meant as a story, or “a slideshow” when it was meant for exploration. **Quick Check:** State the intended outcome and see if ordering, messaging, and interaction all support it. **Stronger Test:** Observe whether users naturally read, interact, or abandon based on the provided affordances.

## Fixes when the balance is off <!-- role: fix -->

- Increase messaging and tighten ordering by moving to an interactive slideshow or guided stem.
- Defer powerful interactions until after the narrative to form a martini glass structure.
- Reduce prescribed ordering and messaging and expose filtering/drill-down when analysis is the goal.
- Add orientation aids (consistent platform, progress indicators) so hybrid designs remain coherent.
