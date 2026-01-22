---
id: avoid-overreliance-on-tables-and-basic-charts-for-memorability
title: Avoid tables, bar charts, and line charts when the primary success metric is
  memorability
bibliography: references.bib
description: Tables and common basic charts tended to be less memorable than more
  distinctive visualization types in recognition-based tests.
labels:
- chart:table
- chart:bar
- chart:line
- task:recall
- visual:form
- impact:memorability
- data:any
- audience:general
- evidence:experiment
---

## Avoid common chart forms when memorability is the main objective <!-- role: advice -->

Avoid using tables, bar charts, and line charts as your primary form when you need the visualization to be remembered as an image.

## Why common chart forms can be forgettable <!-- role: reason -->

Common forms tend to share highly similar visual layouts across many instances, increasing interference and confusion during recognition.

**Mechanism:** When many items share the same template-like structure, fewer unique cues remain for memory, increasing false alarms and lowering sensitivity.

**Evidence:** Bars, lines, points, and tables scored lower on memorability than more distinctive types such as diagrams and grid/matrix visualizations; tables were especially low when pictograms were removed [@borkinWhatMakesVisualization2013a].

**Notes:** Memorability here is quantified using a sensitivity index that penalizes both misses and confusions.

## When this guidance applies <!-- role: context -->

- **User Goal:** Recognize or recall a specific visualization later.
- **Task:** Differentiate one item from many similar items.
- **Data:** Any; particularly repeated reporting where many charts share a format.
- **Chart Setting:** Static publishing contexts; rapid scanning.
- **Audience:** Broad audiences; limited time.
- **Success Criterion:** High recognition with low confusion.

## When to still use common chart forms <!-- role: exceptions -->

**Break it when:** The primary requirement is consistency with established reporting formats rather than memorability. **Why:** Standard forms may be required even if they are less distinctive in recognition tasks [@borkinWhatMakesVisualization2013a].

## Tradeoffs of avoiding common charts <!-- role: costs -->

**Sacrifice:** Familiarity and conventional interpretability expectations.\
**Risk:** Alternative forms may draw attention but not improve comprehension.\
**Mitigation:** Separate memorability goals from comprehension goals and evaluate both.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Trying to make a standard bar/line/table “memorable” only by minor styling tweaks that preserve the same template look. **Why it fails:** The visualization may remain confusable with others in the same category, which lowers memorability scores through false alarms [@borkinWhatMakesVisualization2013a].

## Quick checks <!-- role: check -->

**Failure Sign:** Viewers describe the chart as “a typical bar/line chart” without recalling its topic or distinguishing features.\
**Quick Check:** Ask someone to pick your chart from a set of similar charts after a short break; frequent mix-ups indicate low memorability.\
**Stronger Test:** Measure hit rate and false-alarm rate in a small repeat-detection stream containing many charts of the same common type.

## What to do instead <!-- role: fix -->

- Use a more distinctive visualization type that still fits the data structure, such as a diagram-like representation or grid/matrix form.
- Add a human-recognizable pictorial element to create a stronger identity cue.
- Increase the number of distinct colors to make the image easier to discriminate.
- Add structured, topic-relevant non-data ink that creates a distinctive overall shape without obscuring the display.
