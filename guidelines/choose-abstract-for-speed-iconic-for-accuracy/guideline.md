---
id: choose-abstract-for-speed-iconic-for-accuracy
title: Use Abstract Symbols for Speed, Iconic for Accuracy
bibliography: references.bib
description: Choose abstract symbols for faster processing, but iconic metaphors for
  higher accuracy in aggregate uncertainty tasks.
labels:
- visual:iconography
- visual:shape
- task:search
- task:aggregate
- impact:efficiency
- data:uncertainty
---

## The Rule <!-- role: advice -->
Decide between abstract and iconic symbols based on the primary task:
*   Use **Abstract symbols** (geometric shapes varying in size, value, etc.) when the user needs to make **fast** judgments.
*   Use **Iconic symbols** (pictorial metaphors like stoplights or blurry targets) when the user needs to accurately assess **aggregate** uncertainty across a region.

## The Logic <!-- role: reason -->
There is a fundamental trade-off between processing speed and semantic accuracy.
*   **The Evidence:** In Experiment 2, participants generally took longer (mean RT = 3800ms) to process iconic symbols compared to abstract symbols (mean RT = 3147ms) because icons require cognitive processing to decode the metaphor. However, iconic symbols often led to higher accuracy in map reading tasks, likely because the metaphor (e.g., a "bullseye" for precision) helps the user conceptulize the data more effectively [@maceachren_visual_2012].
*   **The Principle:** Abstract symbols benefit from pre-attentive processing (visual variables), while iconic symbols benefit from semiotic association (metaphor).

## Where to Apply <!-- role: context -->
*   **User Goal:**
    *   *Abstract:* Time-critical monitoring or "glanceability."
    *   *Iconic:* Analytical tasks requiring high confidence in the interpretation of the data quality (e.g., distinguishing trustworthiness from precision).
*   **Data Type:** Spatially distributed data points where users must aggregate information (e.g., "Which region is least certain overall?").

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The iconic metaphor is weak or cultural.
*   **Reason:** If the user does not immediately understand the metaphor (e.g., a "sun dial" for temporal trustworthiness), the accuracy benefit is lost, and the cognitive load remains high [@maceachren_visual_2012].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Iconic symbols are often visually complex and harder to reduce in size for mobile devices or dense displays.
*   **The Risk:** Iconic symbols (like a "stoplight") may introduce colors (Red/Green) that conflict with other color encodings on the map.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Designing complex icons for simple "high/low" uncertainty tasks that require rapid scanning.
*   **Why it fails:** The user is forced to cognitively decode each symbol, slowing down the visual search significantly.
*   **The Wrong Fix:** Using abstract symbols for multiple *types* of uncertainty on the same map.
*   **Why it fails:** Users may confuse which geometric variable (e.g., size vs. value) maps to which uncertainty type (e.g., accuracy vs. currency) without the semantic aid of an icon.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the symbol look like the concept (e.g., a clock for time)? If yes, it is Iconic. Is it a simple circle changing shade? It is Abstract.
*   **The Test:** Measure how long it takes a user to find the "most uncertain" point. If it feels sluggish, your icons may be too complex.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** If users are too slow, simplify icons into abstract geometric forms (e.g., turn a "target" icon into a simple circle size encoding).
*   **Best Fix:** For specific uncertainty types, use the "winning" combinations found in the study: Graded point size for Spatial Accuracy; Scale bars for Temporal Accuracy; "Stop lights" for Attribute Trustworthiness [@maceachren_visual_2012].
