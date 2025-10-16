---
id: avoid-clock-metaphor-for-daily-data
title: "Do not assume the clock metaphor improves interpretation of daily data"

tags:
  - impact:cognitive
  - impact:perceptual
  - chart:radial
  - chart:rose-chart
  - data:temporal
  - data:periodicity.24h
  - audience:general
  - access:cognitive-load-risk

sources:
  - type: research
    ref: Waldner et al., 2020
    url: https://doi.org/10.1109/TVCG.2019.2934784
    note: "The study's main hypothesis—that a familiar 12-hour clock layout would make radial charts more intuitive—was not supported. In fact, 12-hour radial charts were the worst-performing and least-preferred design, causing significant user confusion."

examples:
  - type: bad
    caption: A 12-hour rose chart evoking a clock face
    description: Despite its apparent intuitiveness, this design was found to be confusing and inefficient. Users did not successfully transfer their clock-reading skills to interpret the data values encoded as bar lengths.
    url: /images/waldner-2020-fig1a.png
---

## Guidance

Avoid using a 12-hour radial layout (rose chart) with the assumption that its resemblance to an analog clock will make it more intuitive for visualizing daily patterns.

## Why

The cognitive skill of reading a clock (interpreting the angle of hands) does not translate to the perceptual task of interpreting a data chart (judging the length or area of segments along a radial axis). The Waldner et al. (2020) study explicitly tested this and found the clock metaphor failed. Instead of providing clarity, it created confusion and was the least effective and least liked of all designs tested. Users reported finding it "hard to look at until you realize that it is showing like a clock. But the data is still difficult to decipher."

## When it applies

- **Design Choice:** When considering using a radial chart for 24-hour time-series data because of the "intuitive" clock metaphor.
- **Audience:** Particularly for a general audience, where assumptions about visual literacy should be minimal.

## Exceptions

- The study found no exceptions where the clock metaphor was beneficial for analytical tasks. The evidence strongly suggests it should be avoided when clarity and accuracy are the goals.

## Trade-offs

- You sacrifice a design that may seem conceptually clever or aesthetically novel for one that is demonstrably more understandable and less prone to error. The presumed benefit of the metaphor is an illusion that actively harms comprehension.

## Signs of Trouble

- **Explicit Confusion:** Users directly comment on the ambiguity of the clock layout. One user noted: "I found it very hard to read initially as I was trying to figure out if the 12pm on the left was for PM or AM... This is very confusing."
- **A.M./P.M. Swaps:** Users frequently make errors by swapping morning and afternoon values. The 12-hour radial chart had the highest rate of these errors.
- **Poor Subjective Ratings:** Users rate the visualization poorly, giving it the lowest scores for suitability. The 12-hour radial chart received an average rating of 2.95 out of 5, significantly lower than the 4.3 rating for the 24-hour linear chart.

## How to Improve

- **Comprehensive Redesign: Abandon the Metaphor.** Do not use a 12-hour radial chart for daily data. The most effective and user-preferred alternative found in the study is a simple 24-hour linear bar chart. It is unambiguous, requires no special knowledge to interpret, and leverages the most accurate perceptual channels for data analysis.