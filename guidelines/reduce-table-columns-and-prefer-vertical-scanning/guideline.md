---
id: reduce-table-columns-and-prefer-vertical-scanning
title: Minimize table columns and prefer more rows than columns to improve readability
bibliography: references.bib
description: "Make tables easier to read\u2014especially on mobile\u2014by reducing\
  \ columns and structuring data for vertical scanning."
labels:
- chart:table
- task:read
- visual:layout
- impact:readability
- data:tabular
- audience:general
- device:mobile
---

## Keep tables narrow and optimized for vertical scanning <!-- role: advice -->

Minimize the number and width of columns, and structure the table so information is primarily scanned down columns rather than across many fields.

## Narrow, vertical layouts reduce scanning errors and mobile friction <!-- role: reason -->

Dense horizontal layouts force readers to track across the page, which is slower and more error-prone, and it breaks more easily on small screens.

**Mechanism:** Fewer and narrower columns reduce eye travel and wrapping, and vertically aligned, sortable columns match how people skim lists (like dictionaries), improving scan efficiency.

**Evidence:** Fewer columns make tables more readable (especially on mobile), and swapping structure to have more rows than columns supports easier vertical skimming; column width can be reduced with icons/abbreviations, moving repeated words to headers, and shorter/rounded number formats [@muth_tables_2019].

**Notes:** This is about reducing cognitive and layout load, not about removing essential meaning.

## When this guidance is most relevant <!-- role: context -->

- **User Goal:** Read and compare entries quickly without losing their place.
- **Task:** Skimming, scanning, and quick comparison across entries.
- **Data:** Many fields per entity, long text labels, or large numbers with long formatting.
- **Chart Setting:** Responsive web pages and mobile consumption; limited horizontal space.
- **Audience:** General audiences who will not read the entire table cell-by-cell.
- **Success Criterion:** Key values remain readable without horizontal scrolling or excessive wrapping.

## When you may need more columns anyway <!-- role: exceptions -->

**Break it when:** The table’s purpose depends on showing many fields side-by-side in a single view and removing columns would change the meaning of the table. **Why:** The table would no longer provide the intended “at a glance” completeness for that use case [@muth_tables_2019].

## Tradeoffs of narrowing columns <!-- role: costs -->

**Sacrifice:** You may lose detail or specificity when abbreviating labels or rounding numbers. **Risk:** Over-abbreviation can confuse readers or introduce ambiguity. **Mitigation:** Keep essential information explicit in headers and reserve shortening for repetitive or low-importance detail [@muth_tables_2019].

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Including every available column “because it exists.” **Why it fails:** The table becomes hard to read and especially fragile on mobile layouts [@muth_tables_2019].
- **Mistake:** Forcing wide numeric formats in narrow spaces. **Why it fails:** Excess digits and separators bloat columns and reduce scannability [@muth_tables_2019].

## Quick checks to validate table narrowness <!-- role: check -->

**Failure Sign:** Readers need to scroll horizontally or regularly misread values from adjacent columns. **Quick Check:** If a reader cannot scan a row without visually “getting lost,” the table is too wide. **Stronger Test:** View on a phone-sized viewport; if key columns don’t fit without awkward wrapping, reduce or restructure columns [@muth_tables_2019].

## Practical alternatives when the table is too wide <!-- role: fix -->

- Remove non-essential columns and keep only the information required for the reader’s likely questions [@muth_tables_2019].
- Replace repeated words in cells with a single column header that carries that context [@muth_tables_2019].
- Shorten numbers with compact formats or rounding where exact precision is not required for the table’s purpose [@muth_tables_2019].
- Swap rows and columns so the most important items become vertically scannable columns instead of many side-by-side fields [@muth_tables_2019].
