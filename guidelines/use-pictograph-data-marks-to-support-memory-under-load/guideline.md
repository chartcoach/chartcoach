---
id: use-pictograph-data-marks-to-support-memory-under-load
title: Use pictographs as data marks when viewers must remember values under cognitive
  load
bibliography: references.bib
description: When working memory is crowded by intervening information, pictograph-based
  data marks reduce recall error compared to simple shapes.
labels:
- chart:bar
- task:recall
- visual:shape
- impact:memorability
- data:categorical
- audience:general
- memory:high-load
---

## Use pictographs in the data encoding when users must retain values across intervening content <!-- role: advice -->

Use pictographs as the marks that encode the data (stacked or stretched) when viewers must remember chart values while also processing additional charts or information. Keep the pictographs tied directly to the data marks rather than as separate decoration.

## Pictorial identity can reduce interference between successive datasets <!-- role: reason -->

When memory is taxed by competing information, distinct pictorial identities can help separate one dataset from another, reducing interference and improving recall of the values.

**Mechanism:** Pictographs add distinctive visual-semantic cues to each category, providing additional retrieval hooks that are less likely to collide with other recently viewed numeric information.

**Evidence:** In a 1-back memory task that required retaining the prior chart while viewing a new one, pictograph charts produced lower recall error than charts using simple shapes as marks [@harozISOTYPEVisualizationWorking2015a]. In immediate recall without intervening load, pictographs did not reliably reduce error compared to simple shapes, indicating the benefit is specific to crowded memory conditions [@harozISOTYPEVisualizationWorking2015a].

**Notes:** The observed advantage under load did not depend on stacking versus stretching in that experiment.

## Scenarios with successive charts or competing information <!-- role: context -->

- **User Goal:** Keep values from a chart in mind while continuing to read, view, or compare other material.
- **Task:** Recall values from a previous chart after seeing another chart.
- **Data:** Small sets of categories with modest numeric ranges.
- **Chart Setting:** Articles with multiple figures, slide decks, or dashboards where attention shifts between views.
- **Audience:** General audiences; readers who are scanning and switching context.
- **Success Criterion:** Lower recall error after an intervening visualization.

## When pictographs may not help <!-- role: exceptions -->

**Break it when:** The viewer’s task is immediate extraction with minimal memory load and labels are already clear. **Why:** In low-load immediate recall, pictographs did not produce a reliable memory advantage over simple shapes [@harozISOTYPEVisualizationWorking2015a].

## Tradeoffs of pictograph marks <!-- role: costs -->

**Sacrifice:** You may add visual complexity and require icon design/selection effort. **Risk:** Poorly chosen or hard-to-discriminate pictographs can reduce legibility. **Mitigation:** Use simple, distinct pictographs and keep them consistently mapped to categories.

## Common misapplications <!-- role: mistakes -->

- **Mistake:** Adding pictographs only as background or decoration to “make it memorable.” **Why it fails:** Superfluous imagery increased error and slowed responses in the tested tasks [@harozISOTYPEVisualizationWorking2015a].
- **Mistake:** Replacing clear text labels with pictograph-only labels to “increase visual encoding.” **Why it fails:** Pictograph axis labels increased recall error in the tested working-memory task [@harozISOTYPEVisualizationWorking2015a].

## Quick tests <!-- role: check -->

**Failure Sign:** People confuse which values belonged to which earlier chart after they view another chart. **Quick Check:** Run a simple 1-back recall test (ask about the prior chart) using shape marks vs pictograph marks. **Stronger Test:** Test recall after a realistic intervening task (reading a paragraph or viewing a second chart) and measure absolute error.

## What to do instead <!-- role: fix -->

- Use pictographs as the actual data marks, not as detached decoration.
- Keep text labels for categories while adding pictographs to the marks if category identity must be retained.
- Reduce interference by separating charts into clearer sections if pictographs are not feasible.
- Limit the number of categories per chart so category identity remains distinct across views.
