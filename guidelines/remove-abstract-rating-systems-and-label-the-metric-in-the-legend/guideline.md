---
id: remove-abstract-rating-systems-and-label-the-metric-in-the-legend
title: Remove abstract rating systems and label the metric directly in the legend
bibliography: references.bib
description: Avoid star ratings or other proxy scales in map legends; state the mapped
  variable and thresholds plainly.
labels:
- chart:map
- task:interpret
- visual:text
- impact:clarity
- data:quantitative
- audience:novice
- complexity:basic
---

## Replace proxy scales (like star ratings) with the real mapped measure in the legend <!-- role: advice -->

State the mapped variable directly in the legend (including what it counts and when it applies) instead of using a proxy like “1–5 stars.”

## Why direct metric labels improve comprehension <!-- role: reason -->

Proxy scales force readers to do an unnecessary conversion (“What does 4 stars mean?”) before they can interpret the map, which slows understanding and increases the chance of misreading. Naming the metric aligns the color scale with the data and makes the map self-explanatory.

**Mechanism:** Removing an intermediate encoding step reduces cognitive work and ambiguity, because the legend immediately answers the key decoding question: “What quantity do colors represent?”

**Evidence:** A map redesign recommendation explicitly removes a star rating system and replaces it with a direct explanation of the measure in the color key to eliminate an “extra layer of abstraction” for readers [@mintzer_fix_my_chart_text_elements_2024].

**Notes:** This is most important when the audience is broad or the map supports a practical decision.

## When proxy scales are tempting but harmful <!-- role: context -->

- **User Goal:** Read values/ranges from colors with minimal effort.
- **Task:** Decode the legend and interpret regional differences.
- **Data:** A quantitative measure that can be binned into ranges (e.g., counts of hot days).
- **Chart Setting:** Choropleth map with a categorical-looking legend that could imply rankings or quality judgments.
- **Audience:** Mixed literacy readers who may interpret “stars” as subjective ratings.
- **Success Criterion:** Readers can correctly describe what higher/lower colors mean without asking what the rating represents.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The star/proxy scale is itself the measured outcome (e.g., the dataset literally contains standardized ratings). **Why:** In that case, stars are not an abstraction layered on top; they are the data.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose a bit of “friendly” framing that feels simpler than numbers. **Risk:** Direct metric labels can look technical if you include too many qualifiers. **Mitigation:** Keep the legend phrasing short and put only one key qualifier (like the year) in the legend text.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Keeping stars in the legend and explaining their meaning in a long footnote. **Why it fails:** Readers still have to jump away from the legend to decode the map, so the abstraction and friction remain.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers describe places as “better” or “worse” based on stars but can’t say what’s being measured. **Quick Check:** Ask someone to define what one legend step means; if they answer with “stars” rather than the metric, the legend is too abstract. **Stronger Test:** Remove the title and see if the legend alone communicates the variable, unit, and time frame.

## What to do instead <!-- role: fix -->

- Rename legend classes to include the metric and threshold (e.g., “Under 30 days over 90°F in summer 2050”).
- Put the time horizon (e.g., 2050) and season (e.g., summer) in the legend label if that’s what the colors represent.
- If you need an evaluative framing (“comfortable”), express it in the title, not as a proxy scale in the legend.
- Add a short annotation that connects the metric to the reader’s decision (“lower is cooler”) if needed.
