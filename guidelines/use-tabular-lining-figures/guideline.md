---
id: use-tabular-lining-figures
title: Use tabular lining figures for data values
bibliography: references.bib
description: Ensure numbers align vertically and comparable values have equal width.
labels:
- visual:typography
- data:numerical
- chart:table
- task:compare
- impact:precision
---

## The Rule <!-- role: advice -->

Select a font or OpenType feature that displays numbers as **tabular** (monospaced) and **lining** (uniform height). Avoid proportional or oldstyle figures for data.

## The Logic <!-- role: reason -->

Different fonts handle numbers differently.
1.  **Lining vs. Oldstyle:** Lining numbers "line up" at the same height. Oldstyle numbers dip below or rise above the line, which is beautiful in paragraphs but hard to read in tables or axis ticks.
2.  **Tabular vs. Proportional:** In tabular figures, every digit has the same width (e.g., a "1" takes as much space as an "8"). This ensures that numbers with the same digit count align vertically and are visibly the same length, allowing users to instantly compare magnitudes [@muth_fonts_2022].

*   **The Principle:** Vertical Alignment and Magnitude Perception
*   **The Evidence:** [@muth_fonts_2022] illustrates that with proportional figures, `1,111.17` looks shorter than `680.90`, misleading the eye.

## Where to Apply <!-- role: context -->

*   **User Goal:** Comparing values down a column or comparing magnitudes visually.
*   **Data Type:** Numerical data, financial reports, tooltips.
*   **Component:** Tables, axis ticks, tooltips.

## When to Break It <!-- role: exceptions -->

*   **Scenario:** Paragraph text or narrative descriptions.
*   **Reason:** Proportional figures look better in flowing text because an "8" deserves more space than a "1," and a "W" deserves more than a "J" [@muth_fonts_2022].

## The Price <!-- role: costs -->

*   **The Sacrifice:** Tabular figures can look slightly uneven in kerning (spacing) when used in sentences.
*   **The Risk:** If you use a font that *only* has proportional figures, columns of numbers will appear wavy and unaligned.

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Manually adding spaces to align numbers.
*   **Why it fails:** It breaks responsiveness and accessibility.
*   **The Wrong Fix:** Using a full Monospace font (like Courier) for everything.
*   **Why it fails:** While the numbers align, the text becomes harder to read and looks like code or a typewriter [@muth_fonts_2022].

## How to Check <!-- role: check -->

*   **Visual Sign:** In a column of numbers, do the decimal points wobble left and right?
*   **The Test:** Type "111" and "888" on two lines. If "888" is significantly wider, you are using proportional figures.

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Choose a font that defaults to tabular lining figures (e.g., Roboto, Lato, Open Sans).
*   **Best Fix:** Use a "multiplexed" (or uni-width) font where bold and regular weights share the same width, or specific fonts like Recursive, to ensure numbers align perfectly even when highlighted [@muth_fonts_2022].
