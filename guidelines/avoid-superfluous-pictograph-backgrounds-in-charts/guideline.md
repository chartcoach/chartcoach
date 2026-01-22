---
id: avoid-superfluous-pictograph-backgrounds-in-charts
title: Avoid superfluous decorative pictograph backgrounds in charts
bibliography: references.bib
description: Decorative background imagery that does not encode data reduces recall
  accuracy and slows information retrieval.
labels:
- chart:bar
- task:read-value
- visual:imagery
- impact:clarity
- data:categorical
- audience:general
- embellishment:superfluous
---

## Avoid non-data background imagery in charts <!-- role: advice -->

Avoid adding decorative pictograph images to a chart when the image does not encode any data value. Keep imagery either absent or directly tied to the data marks.

## Superfluous imagery diverts attention from data encoding <!-- role: reason -->

Decorative imagery competes with the chart’s data marks for attention and working memory resources, making it harder to encode and retrieve the intended quantities and comparisons.

**Mechanism:** Non-data pictures create an additional perceptual object that viewers must parse and suppress, increasing distraction and interfering with memory for the chart’s values.

**Evidence:** Working-memory recall error increased substantially when a bar chart included a superfluous background pictograph compared to an unembellished bar chart [@harozISOTYPEVisualizationWorking2015a]. Response times for answering “more/fewer” questions were slower only in the superfluous-background condition relative to the standard bar chart [@harozISOTYPEVisualizationWorking2015a].

**Notes:** The cost is specific to imagery that is not part of the data mapping; pictographs used as data marks did not show comparable performance costs in these tasks.

## Charts where users must read or remember values <!-- role: context -->

- **User Goal:** Extract and retain quantitative values from a chart.
- **Task:** Read off values, compare values, or recall recently seen values.
- **Data:** Small categorical sets with discrete numeric values.
- **Chart Setting:** Static chart in a report, dashboard, or article; limited viewing time or divided attention.
- **Audience:** Mixed literacy; time-constrained viewers.
- **Success Criterion:** Lower error and faster responses without added confusion.

## When decorative imagery may be unavoidable <!-- role: exceptions -->

**Break it when:** A background image is required for branding or editorial art direction and cannot be removed. **Why:** The constraint is external to the visualization task, so performance must be protected via other design choices.

## Tradeoffs of removing decorative imagery <!-- role: costs -->

**Sacrifice:** You may lose some aesthetic appeal or thematic framing. **Risk:** Over-correcting can produce a chart that is less inviting to initially open. **Mitigation:** Use engagement-oriented techniques that do not add non-data imagery within the plotting area.

## Common ways this goes wrong <!-- role: mistakes -->

- **Mistake:** Using a large faded icon “behind” bars to signal the topic. **Why it fails:** Even irrelevant imagery measurably increases recall error and slows responses in the tested tasks [@harozISOTYPEVisualizationWorking2015a].
- **Mistake:** Treating any added picture as “harmless because it’s subtle.” **Why it fails:** The tested superfluous condition impaired both memory and speed despite being visually integrated as a background [@harozISOTYPEVisualizationWorking2015a].

## Fast checks before shipping <!-- role: check -->

**Failure Sign:** People mention the picture when asked about the data, or hesitate when reading values. **Quick Check:** Temporarily remove the background image; if the chart becomes easier to read instantly, the image is likely competing with the data. **Stronger Test:** Run a short timed “which is more/less?” task and a brief recall task with and without the background.

## Alternatives that preserve clarity <!-- role: fix -->

- Remove the background pictograph entirely from the plotting area.
- Move thematic imagery outside the chart area (e.g., in a title block) so it does not overlap data marks.
- Encode the theme by using pictographs as the data marks themselves rather than as decoration.
- Add concise text annotation to provide context instead of a picture.
