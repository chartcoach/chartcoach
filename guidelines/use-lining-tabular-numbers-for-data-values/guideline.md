---
id: use-lining-tabular-numbers-for-data-values
title: Use lining, tabular numerals for chart and table numbers
bibliography: references.bib
description: Ensure numbers are uniform-height and equal-width so values align and
  are easy to compare in charts and tables.
labels:
- chart:table
- task:compare
- visual:typography
- impact:readability
- data:quantitative
- audience:general
- scope:numerals
---

## Set numeric text in lining, tabular figures <!-- role: advice -->

Use a font (or numeral setting) that provides lining numerals and tabular numerals for axes, tooltips, labels, and tables.

## Uniform numerals improve comparability and alignment <!-- role: reason -->

Chart reading often involves comparing many numeric strings, where irregular numeral shapes and widths add noise; lining figures keep consistent height, and tabular figures keep consistent width so columns and digit counts become easier to judge.

**Mechanism:** Equal-height numerals reduce shape variability across values, and equal-width numerals create reliable vertical alignment and faster visual parsing in columns and repeated labels.

**Evidence:** Oldstyle numerals are described as beautiful in paragraphs but harder to read in tables/tooltips/axis ticks, while tabular numerals are recommended because they align and make digit length comparisons more immediate [@muth_fonts_2022].

**Notes:** Many common sans-serif families include tabular, lining figures, but you need to confirm the figure style exists and is enabled [@muth_fonts_2022].

## Apply when numbers appear in lists, columns, or repeated ticks <!-- role: context -->

- **User Goal:** Compare magnitudes and read precise values quickly.
- **Task:** Scan axes, tooltips, data labels, and table columns.
- **Data:** Quantitative values shown as many separate numbers (especially in columns).
- **Chart Setting:** Tables, dense charts, dashboards, and tooltips with multiple fields.
- **Audience:** Broad audiences, including readers who skim quickly.
- **Success Criterion:** Values line up cleanly and can be compared without rereading.

## Prefer proportional figures only for paragraph-like narrative text <!-- role: exceptions -->

- **Break it when:** Numbers are embedded in running prose and you prioritize typographic texture over alignment. **Why:** Proportional figures can look nicer in paragraphs, where column alignment is not the goal [@muth_fonts_2022].

## Alignment can look rigid outside tables <!-- role: costs -->

**Sacrifice:** Tabular numerals can look slightly less “natural” in paragraph text. **Risk:** Using tabular figures everywhere can make narrative annotations feel typographically stiff. **Mitigation:** Use tabular figures for axes/tables/tooltips and allow proportional figures for longer prose annotations if needed [@muth_fonts_2022].

## Don’t mix numeral styles unintentionally across the same view <!-- role: mistakes -->

- **Mistake:** Using oldstyle or proportional numerals for axis ticks or table cells. **Why it fails:** Non-lining heights and variable widths make numbers harder to scan and disrupt alignment cues that support comparison [@muth_fonts_2022].

## Verify both height and width behavior in real examples <!-- role: check -->

**Failure Sign:** Table columns look ragged or digit counts are hard to judge at a glance. **Quick Check:** Place several values with different digits (e.g., 124.17 and 680.90) in a column and see if decimals and overall widths align. **Stronger Test:** Compare a screenshot of the same table with tabular numerals toggled on vs. off and check which version you can scan faster [@muth_fonts_2022].

## Use font features or switch families if needed <!-- role: fix -->

- Enable tabular and lining numerals via font features (if your tool supports them).
- Choose a font family known to include tabular, lining figures for UI/data use.
- If you need to bold some values in tables, consider a multiplexed (uniwidth) option so widths don’t shift between weights.
- If your chosen brand font lacks suitable numerals, keep the brand font for titles and use a data-friendly font for numeric fields [@muth_fonts_2022].
