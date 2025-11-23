---
id: ensure-white-space-for-counting
title: Ensure Visual Separation Between Icons
bibliography: references.bib
description: Provide distinct white space between icons in arrays to support users
  who rely on counting strategies.
labels:
- chart:icon-array
- visual:density
- visual:whitespace
- task:count
- audience:expert
---

## The Rule <!-- role: advice -->
Ensure there is distinct white space between individual units in an icon array. Avoid solid, touching blocks that merge into a single mass unless the specific intent is area-estimation.

## The Logic <!-- role: reason -->
Users with higher numeracy skills tend to process pictographs by **counting** individual icons rather than estimating the total colored area. Distinct shapes with gaps facilitate this process.
*   **The Principle:** **Countability.** Irregular shapes (like person icons) naturally create white space between units, making them distinct. Rectangular blocks often fit together tightly, reducing them to a "bar chart" texture that inhibits counting [@zikmund-fisher_blocks_2014].
*   **The Evidence:** The study found that highly numerate and graphically literate participants had much better calibration (correlation between perceived and actual risk) when using distinct restroom icons compared to blocks. The authors attribute this to the "white space" making icons potentially "more distinct and easy to count" [@zikmund-fisher_blocks_2014].

## Where to Apply <!-- role: context -->
*   **User Goal:** Precise understanding of probability (e.g., "12 out of 100").
*   **Audience:** Audiences with moderate to high numeracy who are likely to attempt counting to verify the data.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The audience has very low numeracy and struggles with counting.
*   **Reason:** Low-numeracy users may rely on "gist" processing (judging the size of the colored blob vs. the grey blob). In this specific case, tightly packed blocks that form a solid bar might be easier to estimate visually [@zikmund-fisher_blocks_2014].

## The Price <!-- role: costs -->
*   **The Sacrifice:** The chart will take up more screen real estate (lower data density) due to the required padding between icons.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** using "pixel" style grids where squares touch perfectly.
*   **Why it fails:** This forces the user to rely solely on area estimation, removing the ability to verify the number by counting, which disadvantages numerate users [@zikmund-fisher_blocks_2014].

## How to Check <!-- role: check -->
*   **Visual Sign:** Do the active icons form a single, solid geometric shape?
*   **The Test:** Can you easily count five icons in the middle of the grid without losing your place?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a 1px-2px white border around every icon in the grid.
*   **Best Fix:** Switch to an irregular icon shape (like a person or circle) that naturally prevents the edges from merging visually.
