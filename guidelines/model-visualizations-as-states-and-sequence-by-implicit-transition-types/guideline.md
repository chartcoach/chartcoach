---
id: model-visualizations-as-states-and-sequence-by-implicit-transition-types
title: Sequence Visualizations Using Implicit Transition Types
bibliography: references.bib
description: Construct sequences by identifying transitions that change only time,
  measure, dimension, or granularity between visualization states.
labels:
- task:sequence
- impact:structure
- data:multivariate
- audience:author
- custom:automation
- complexity:advanced
---

## The Rule <!-- role: advice -->

When building a linear narrative from a set of views, explicitly classify each view by four attributes—independent variable, dependent variable, time, and granularity—and sequence views using transitions that change only one attribute at a time.

## The Logic <!-- role: reason -->

The paper’s qualitative analysis shows professional narrative visualizations frequently use transition types that correspond to a single change along a data attribute; the authors then propose a graph-based sequencing approach that labels and prioritizes these implicit transition types [@hullmanDeeperUnderstandingSequence2013].

- **The Principle:** State-based representation + single-attribute transition labeling
- **The Evidence:** Transition types observed (temporal, comparison via measure/dimension walks, granularity) are operationalized by comparing view attributes; edges are weighted by transformation cost to prioritize simpler transitions [@hullmanDeeperUnderstandingSequence2013].

## Where to Apply <!-- role: context -->

- **User Goal:** Author or automatically suggest slideshow-style sequences from an existing set of charts
- **Data Type:** Data where (a) time can be detected, (b) measures vs. dimensions are identifiable, and/or (c) hierarchy/filtering levels exist
- **Audience:** Tool builders and analysts assembling narrative slide decks

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your key transitions are “explicit” (e.g., causal or question→answer) and cannot be inferred from attributes alone.
- **Reason:** The paper distinguishes explicit transition types (requiring creator interpretation) from implicit types (inferable); this rule targets the implicit ones [@hullmanDeeperUnderstandingSequence2013].

## The Price <!-- role: costs -->

- **The Sacrifice:** Up-front effort to annotate/encode the attributes of each view (especially granularity/hierarchy).
- **The Risk:** Misclassification of what’s independent vs. dependent can mislabel transitions.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating any two “related” charts as a valid transition without specifying what changed.
- **Why it fails:** Without attribute-based labeling and cost, you can generate too many possible transitions and end up with cognitively costly steps [@hullmanDeeperUnderstandingSequence2013].

## How to Check <!-- role: check -->

- **Visual Sign:** You cannot name what changed from slide to slide (time? measure? group? detail level?).
- **The Test:** For every adjacent pair, identify exactly one transition type: Temporal, Dimension Walk, Measure Walk, or Granularity; if you can’t, the transition is likely multi-change or unclear.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add missing metadata: tag each slide with its time, measure, dimension, and granularity level.
- **Best Fix:** Build a transition graph (views as nodes; labeled edges; weights by transformation cost) and choose a low-cost path that fits your narrative constraints [@hullmanDeeperUnderstandingSequence2013].
