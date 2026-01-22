---
id: include-font-size-variation-only-when-it-does-not-undermine-group-reading
title: Include font size variation only when it does not undermine within-group reading
bibliography: references.bib
description: Use font size variation cautiously, because its benefit depends on having
  strong spatial grouping.
labels:
- chart:word-cloud
- task:infer
- visual:size
- impact:readability
- data:categorical
- audience:novice
- domain:text
---

## Vary font sizes only within strongly grouped layouts, not as a substitute for grouping <!-- role: advice -->

Use font size variation only when words are already clearly grouped by topic so viewers can still read and integrate each group. Do not rely on font size variation to compensate for a mixed Wordle-style layout.

## Font size variation interacts with layout organization <!-- role: reason -->

Font size variation can be compatible with high performance when group structure is clear, but it does not repair the core problem of mixed-category placement. In evaluations, font-size variation improved performance within column groupings but did not improve Wordle-style layouts, indicating that grouping dominates and size variation can be neutral or detrimental when words are interleaved.

**Mechanism:** When grouping is clear, size variation can add visual interest without disrupting the viewer’s ability to aggregate cues; when grouping is unclear, size variation adds additional heterogeneity that does not help bind the correct cues.

**Evidence:** In grouped column layouts, multiple font sizes yielded higher category-guessing scores than single-font columns, while in Wordle-style layouts multiple font sizes did not improve performance and interacted negatively with the Wordle format [@hearstEvaluationSemanticallyGrouped2020]. Overall, Wordle-style layouts underperformed grouped layouts regardless of font sizing [@hearstEvaluationSemanticallyGrouped2020].

**Notes:** The tested task emphasized rapid topic inference, not frequency estimation.

## When this font-size rule applies <!-- role: context -->

- **User Goal:** Infer underlying topics from sets of cue words.
- **Task:** Rapid category/topic identification.
- **Data:** Words grouped into topics; relative importance may or may not be meaningful.
- **Chart Setting:** Word-cloud-like displays where typography is used for emphasis or aesthetics.
- **Audience:** Readers who need readability and quick integration over decorative complexity.
- **Success Criterion:** Maintaining or improving topic inference accuracy while keeping the design visually engaging.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The viewer must treat every word as equally important evidence for inferring the topic. **Why:** Over-emphasizing some words via size can bias attention away from other necessary cues, especially in dense layouts [@hearstEvaluationSemanticallyGrouped2020].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Restricting size variation can reduce the “playful” typographic feel. **Risk:** Excessive size variation can make grouped regions harder to scan as a set, especially when groups are not separated strongly. **Mitigation:** Keep variation moderate and validate that viewers can still identify all intended topics under a short viewing time.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Increasing font size variation in a Wordle-style layout to “add structure.” **Why it fails:** Performance did not improve for Wordle-style layouts with multiple font sizes, indicating size variation does not solve intermixing [@hearstEvaluationSemanticallyGrouped2020].
- **Mistake:** Using large size differences that cause a few words to dominate within a group. **Why it fails:** Dominant words can pull attention away from other cue words needed for correct topic inference [@hearstEvaluationSemanticallyGrouped2020].

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers recall only the largest words and miss topics that require integrating several smaller cues. **Quick Check:** Ask viewers to infer each topic and note whether they ignore smaller words within groups. **Stronger Test:** Compare performance of a moderate-size-variation version vs a flatter typography version while keeping grouping constant.

## What to do instead <!-- role: fix -->

- Reduce the range of font sizes while keeping strong topic grouping intact.
- Move emphasis from size to grouping cues such as whitespace and consistent per-group color.
- If typographic play is needed, vary style within a group without creating extreme dominance by a single word.
- If readability suffers, switch to a grouped list or columnar presentation of words.
