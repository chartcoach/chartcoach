---
id: sort-small-multiple-panels-by-a-meaningful-metric-and-say-what-it-is
title: Sort small multiple panels by a meaningful metric and state the order
bibliography: references.bib
description: Order panels by start, end, change, or another relevant metric so readers
  see the intended structure first.
labels:
- chart:line
- task:rank
- visual:layout
- impact:clarity
- data:temporal
- audience:novice
- complexity:intermediate
---

## Sort small multiple panels by a meaningful metric and state the order <!-- role: advice -->

Sort small multiple panels using an order that supports what readers should notice first, such as end value, start value, range, percent change, or difference. State the sorting logic in the chart description when it is not self-evident.

## Panel order controls scanning and interpretation <!-- role: reason -->

In small multiples, readers often scan in reading order; the first panels become the implicit reference for what “normal” looks like. A meaningful sort turns the panel grid into an organized argument (e.g., highest-to-lowest at the end), whereas arbitrary order forces readers to search without guidance.

**Mechanism:** Ordering reduces search and sets expectations, making patterns and extremes easier to find.

**Evidence:** Meaningful sorting (by start value, end value, range, percent change, or difference) helps readers navigate many panels and supports specific questions; stating sort order in the chart description can clarify the intended structure [@muth_small_multiple_line_charts_2024].

**Notes:** If no meaningful order exists, alphabetical ordering is better than none.

## When readers need help navigating many panels <!-- role: context -->

- **User Goal:** Quickly find extremes or understand how categories relate by a key metric.
- **Task:** Scan for highest/lowest, biggest increase/decrease, or most variability.
- **Data:** Many categories shown as panels; a computable metric exists for ordering.
- **Chart Setting:** Small multiples arranged in a grid or list where order is visually salient.
- **Audience:** Readers likely to scan in reading order and stop early.
- **Success Criterion:** The ordering itself conveys structure and reduces time to find relevant panels.

## When to avoid metric-based sorting <!-- role: exceptions -->

**Break it when:** The categories have an externally meaningful fixed order (such as a standard sequence readers expect). **Why:** Reordering may confuse navigation or conflict with how readers look up categories [@muth_small_multiple_line_charts_2024].

## Tradeoffs of sorting <!-- role: costs -->

**Sacrifice:** Sorted order can make it harder to locate a specific named category quickly. **Risk:** Readers may not realize the order is intentional and misread the layout as arbitrary. **Mitigation:** Communicate the sort rule in the description or accompanying text [@muth_small_multiple_line_charts_2024].

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Leaving panels in an arbitrary order. **Why it fails:** Readers get no navigation help and must do extra work to find patterns [@muth_small_multiple_line_charts_2024].
- **Mistake:** Sorting by a metric but not telling readers. **Why it fails:** The structure is invisible, so readers may miss the intended comparison [@muth_small_multiple_line_charts_2024].

## Quick tests <!-- role: check -->

**Failure Sign:** Readers ask “Why are these panels arranged this way?” **Quick Check:** If you have more than a handful of panels, try sorting by end value and see if the chart becomes easier to scan. **Stronger Test:** Ask someone to find the biggest increase; if sorting makes it much faster, keep it and label the order [@muth_small_multiple_line_charts_2024].

## What to do instead <!-- role: fix -->

- Sort panels by end value, start value, range, percent change, or difference, depending on the story.
- Use alphabetical order when no meaningful metric is available.
- Write the sorting rule in the chart description.
- If sorting hinders lookup, provide a searchable alternative (such as a table with sparklines) [@muth_small_multiple_line_charts_2024].
