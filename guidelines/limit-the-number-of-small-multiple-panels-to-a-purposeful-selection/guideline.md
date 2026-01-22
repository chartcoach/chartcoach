---
id: limit-the-number-of-small-multiple-panels-to-a-purposeful-selection
title: Limit small multiple panels to the categories that support your takeaway
bibliography: references.bib
description: Keep small multiples focused by selecting a manageable set of panels
  rather than showing everything.
labels:
- chart:line
- task:communicate
- visual:layout
- impact:clarity
- data:temporal
- audience:novice
- complexity:intermediate
---

## Limit small multiple panels to the categories that support your takeaway <!-- role: advice -->

Include fewer panels than you initially plan, keeping only categories that support the points you want readers to take away while still representing the situation truthfully. If readers must scroll through many panels to find what matters, reduce the panel set.

## Too many panels shifts work from the author to the reader <!-- role: reason -->

Small multiples remove overlap but can introduce a different burden: making readers hunt across dozens of panels to discover what’s interesting. A focused selection preserves the benefits of separation while keeping attention on the intended message.

**Mechanism:** Reducing panel count lowers search time and cognitive load, so readers spend effort interpreting rather than hunting.

**Evidence:** Showing many panels can overwhelm; it’s recommended to select panels carefully, keep those that support the takeaway, and check whether scrolling on mobile becomes too long [@muth_small_multiple_line_charts_2024].

**Notes:** “Truthful” selection means the subset should not misrepresent the overall pattern.

## When panel count becomes the main usability problem <!-- role: context -->

- **User Goal:** Understand a key message or pattern without extensive exploration.
- **Task:** Identify notable trends, contrasts, or outliers among categories.
- **Data:** Many categories; time series per category.
- **Chart Setting:** Mobile or narrow layouts where long scrolling is likely.
- **Audience:** General readers with limited time.
- **Success Criterion:** Readers can find the intended patterns quickly without exhaustive scanning.

## When you should show all categories <!-- role: exceptions -->

**Break it when:** The requirement is to provide a complete reference view of all categories. **Why:** Omission would violate the purpose of completeness, even if it reduces narrative focus [@muth_small_multiple_line_charts_2024].

## Tradeoffs of selecting panels <!-- role: costs -->

**Sacrifice:** You give up completeness and may invite questions about what was left out. **Risk:** Selection can be perceived as cherry-picking if not handled transparently. **Mitigation:** Ensure the subset supports the message without distorting the overall picture, and provide a way to access the full set when needed [@muth_small_multiple_line_charts_2024].

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Adding “lots of categories” just because overlap is no longer a problem. **Why it fails:** Readers face a discovery task the chart doesn’t guide, increasing effort and reducing comprehension [@muth_small_multiple_line_charts_2024].
- **Mistake:** Ignoring mobile scrolling length. **Why it fails:** The chart becomes tedious to navigate, so readers may abandon it before reaching key panels [@muth_small_multiple_line_charts_2024].

## Quick tests <!-- role: check -->

**Failure Sign:** The chart feels like a long, unguided gallery of panels. **Quick Check:** If you cannot summarize why each included panel is there, you likely have too many. **Stronger Test:** Test on a phone; if it takes long scrolling to reach the end, reduce panels or switch format [@muth_small_multiple_line_charts_2024].

## What to do instead <!-- role: fix -->

- Keep only the panels that support the key takeaways while maintaining an honest picture.
- Use sparklines in a searchable table when you need to include all categories.
- Split categories into smaller themed groups and show separate small-multiple blocks.
- Provide an additional “show all” view elsewhere if the main article needs focus [@muth_small_multiple_line_charts_2024].
