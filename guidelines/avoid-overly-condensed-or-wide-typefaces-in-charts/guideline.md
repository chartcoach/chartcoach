---
id: avoid-overly-condensed-or-wide-typefaces-in-charts
title: Avoid overly condensed or overly wide typefaces for chart text
bibliography: references.bib
description: Use normal-width fonts for chart labels; condensed faces hinder legibility
  and wide faces waste space.
labels:
- chart:generic
- task:scan
- visual:typography
- impact:readability
- data:generic
- audience:general
- scope:font-width
---

## Use normal-width typefaces for most chart and table text <!-- role: advice -->

Choose a normal-width typeface for chart and table labels, avoiding very condensed (narrow) fonts and very wide fonts for most small text.

## Extreme widths harm either legibility or layout economy <!-- role: reason -->

Condensed faces squeeze letterforms until they become harder to decipher, while wide faces consume space and force smaller sizes or more line breaks; both outcomes reduce the readability of dense chart scaffolding.

**Mechanism:** Letter recognition depends on internal spacing and distinct shapes; narrowing reduces distinguishability, and widening reduces available layout room for the same information.

**Evidence:** Narrow fonts are described as more difficult to read and often signaling a cramped compromise, while wide fonts are easy to read but consume too much space; normal-width is presented as the newsroom norm and generally safest [@muth_fonts_2022].

**Notes:** If space is tight, smaller normal-width text can outperform larger condensed text in readability [@muth_fonts_2022].

## Apply in dense labeling situations and space-constrained layouts <!-- role: context -->

- **User Goal:** Read many labels quickly and accurately.
- **Task:** Scan category labels, axis ticks, tooltips, and table headers.
- **Data:** Any, especially high-cardinality categorical labels.
- **Chart Setting:** Responsive embeds, dashboards, mobile, or tight column widths.
- **Audience:** General audiences; skim readers.
- **Success Criterion:** Labels remain legible without awkward truncation or cramped appearance.

## Condensed can work for large display text with a deliberate style <!-- role: exceptions -->

- **Break it when:** You use an extremely condensed face only for very large text and the condensed look is a deliberate design choice. **Why:** At large sizes, condensed letterforms can remain legible and become a distinctive visual style [@muth_fonts_2022].

## Normal width may force abbreviation or fewer labels <!-- role: costs -->

**Sacrifice:** You may need to shorten labels, reduce tick density, or adjust layout rather than “solving” space with condensed fonts. **Risk:** Over-correcting with abbreviations can reduce clarity. **Mitigation:** Prefer layout changes that preserve full wording where possible (wrapping, rotation, or fewer labels) [@muth_fonts_2022].

## Don’t treat condensed as a free way to fit more text <!-- role: mistakes -->

- **Mistake:** Switching to a condensed font to keep the same font size in a cramped layout. **Why it fails:** Reduced character spacing makes labels harder to read and can look like an unintentional compromise [@muth_fonts_2022].

## Compare readability at the final pixel size <!-- role: check -->

**Failure Sign:** Labels feel cramped, retro in an unintended way, or require careful decoding. **Quick Check:** Compare the same chart with a normal-width font at a slightly smaller size versus a condensed font at a larger size and choose the version that reads faster. **Stronger Test:** Ask a reader to read several labels aloud quickly; if they hesitate more with the condensed face, revert [@muth_fonts_2022].

## Solve space problems with layout choices, not extreme font widths <!-- role: fix -->

- Switch from condensed/wide fonts to a normal-width family for small text.
- Reduce label density by showing fewer ticks or fewer category labels.
- Adjust layout to create room (wrap labels, change chart margins, or increase chart height).
- Use large condensed type only for big display elements where legibility remains strong [@muth_fonts_2022].
