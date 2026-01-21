---
id: use-familiar-chart-types
title: Use Familiar, Straightforward Chart Types
bibliography: references.bib
description: Prefer familiar chart types (like bars and lines) so audiences can recognize
  the form quickly and interpret the data accurately.
labels:
- chart:bar
- chart:line
- task:compare
- visual:position
- impact:clarity
- data:quantitative
- audience:novice
- complexity:simple
---

## The Rule <!-- role: advice -->

Choose a familiar, straightforward chart type (e.g., bar or line) before considering more complex, multi-dimensional alternatives.

## The Logic <!-- role: reason -->

Familiar chart types reduce the mental effort needed to decode how values are encoded, letting viewers spend attention on the message rather than the method.

- **The Principle:** Recognition reduces interpretation load
- **The Evidence:** Viewers understand charts more easily when they can recognize the type, and they may prefer several simple charts over one complex visualization [@knoll_gulf_2025]. For one-dimensional comparisons, bar charts are perceived as easier to interpret than bubble charts [@prantl_studying_forthcoming]. Practitioners report that familiar chart types are most commonly understood, while more artful designs can reduce comprehension and trigger requests for simpler depictions [@schuster_who_2023].

## Where to Apply <!-- role: context -->

Use this rule when comprehension and trust matter more than novelty.

- **User Goal:** Quickly understand or compare values without training
- **Data Type:** One-dimensional quantitative comparisons, simple categories, basic trends over time
- **Audience:** General public, mixed-literacy stakeholders, time-constrained decision-makers

## When to Break It <!-- role: exceptions -->

Ignore this rule when a familiar chart type cannot express the key structure without distortion or omission.

- **Scenario:** You must show high-dimensional relationships (e.g., multivariate tradeoffs, distributions, uncertainty) that a bar/line chart would hide.
- **Reason:** A simple chart may force misleading aggregation or conceal critical patterns; a more specialized chart can be clearer if the audience is prepared and the encoding is explained.

## The Price <!-- role: costs -->

Using only familiar chart types can limit what you can say.

- **The Sacrifice:** Less expressive power for complex, multi-variable stories
- **The Risk:** Oversimplification (important nuance gets flattened into averages or categories)

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Replacing a clear bar/line chart with a bubble/3D/novel hybrid to look “more insightful.”
- **Why it fails:** Extra encodings add decoding steps and can make simple comparisons feel harder than necessary [@prantl_studying_forthcoming].
- **The Wrong Fix:** Packing many variables into one “do-everything” visualization instead of splitting into small multiples.
- **Why it fails:** Viewers may prefer multiple simple charts because each one is recognizable and easier to interpret [@knoll_gulf_2025].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers have to ask “What am I looking at?” or “How do I read this?” before they can discuss the data.
- **The Test:** Show the chart to someone representative of your audience for 10 seconds; ask them to name the chart type and describe what is being compared. If they can’t, the form is likely too unfamiliar.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch to a bar chart for categorical comparisons or a line chart for trends; remove extra encodings (size, 3D, decorative shapes).
- **Best Fix:** Decompose the complex view into several simple, familiar charts (small multiples) aligned to the main questions, so each chart has one primary job [@knoll_gulf_2025].
