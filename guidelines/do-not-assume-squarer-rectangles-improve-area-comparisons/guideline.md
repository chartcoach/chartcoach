---
id: do-not-assume-squarer-rectangles-improve-area-comparisons
title: Do Not Assume Square-Like Rectangles Improve Area Comparison Accuracy
bibliography: references.bib
description: Area comparisons were least accurate when both rectangles were near 1:1
  aspect ratio.
labels:
- chart:treemap
- task:compare
- visual:area
- impact:accuracy
- data:hierarchical
- audience:general
- domain:treemap-layout
---

## The Rule <!-- role: advice -->

Do not treat “make rectangles as square as possible” as a perceptually guaranteed optimization for accurate area comparisons.

## The Logic <!-- role: reason -->

In rectangular area judgment tasks (including treemap-like displays), Heer & Bostock found a significant effect of aspect ratio—and unexpectedly, comparisons where both rectangles had aspect ratio 1 performed worst [@heerCrowdsourcingGraphicalPerception2010a]. They hypothesize viewers may rely on 1D side-length cues as a proxy for area, which can maximize error when comparing squares.

- **The Principle:** Heuristic use of length cues can bias area perception
- **The Evidence:** Significant aspect-ratio effect; 1:1 vs 1:1 worst accuracy in their data [@heerCrowdsourcingGraphicalPerception2010a]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare magnitudes encoded by rectangle areas
- **Data Type:** Treemaps, cartogram-like rectangles, rectangular area encodings
- **Audience:** General readers making quick magnitude judgments

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your optimization goal is not comparison accuracy (e.g., aesthetic regularity, packing constraints).
- **Reason:** The paper’s finding concerns judgment accuracy, not layout aesthetics or space utilization [@heerCrowdsourcingGraphicalPerception2010a].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need to reconsider “squarified” objectives or accept varied aspect ratios.
- **The Risk:** Without further validation, changing layout objectives could have unforeseen effects on other tasks.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming closer-to-square rectangles automatically make treemaps easier to read.
- **Why it fails:** Their experiment found the opposite for the specific comparison setting of square-vs-square [@heerCrowdsourcingGraphicalPerception2010a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users struggle to compare similarly sized square-like nodes and disagree on ordering.
- **The Test:** Sample comparisons where both targets are ~1:1 and measure estimation error; compare against non-square aspect ratio pairings, as in the paper’s factorial design [@heerCrowdsourcingGraphicalPerception2010a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Avoid relying solely on area for precise comparisons; add interaction or alternative encodings in critical comparisons.
- **Best Fix:** Validate your treemap/cartogram layout with an area-judgment experiment that varies aspect ratios, rather than assuming squareness is optimal [@heerCrowdsourcingGraphicalPerception2010a].
