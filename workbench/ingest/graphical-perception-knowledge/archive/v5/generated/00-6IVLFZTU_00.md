---
id: use-small-multiples-for-propagation-analysis
title: "Use small-multiple maps for the best overall performance in spatiotemporal propagation analysis"

tags:
  - impact:performance
  - impact:cognitive
  - chart:map
  - chart:map.small-multiples
  - data:spatiotemporal
  - task:compare
  - task:trend
  - task:rank
  - medium:interactive
  - medium:static

evidence:
  strength: medium
  summary: "A 2020 study comparing animated maps, small-multiple maps, and glyph maps for analyzing geographical propagation found that small-multiples had the fastest overall completion time and high accuracy across a range of five analytical tasks."

sources:
  - type: research
    ref: "Peña-Araya, Bezerianos, & Pietriga, 2020"
    url: https://doi.org/10.1145/3313831.3376350
    note: "Primary study that compared three visualization strategies (animation, small-multiples, glyphs) for five propagation analysis tasks. Small-multiples performed best overall."
    role: primary

---

## Guidance

For the most efficient overall analysis of geographical propagation patterns (like the spread of a disease or a meme), use a small-multiple layout where each point in time is shown as a separate, small map.

## Why

Small-multiple maps provide a complete, static overview of the entire phenomenon at a glance. This layout allows viewers to make comparisons between any two points in time, not just consecutive ones, without having to rely on working memory. This "overview first" approach reduces cognitive load and leads to faster and more accurate performance across a variety of analytical tasks, such as finding peaks and comparing scope.

### Core Principle

Reduce cognitive load by making comparisons explicit in space rather than implicit in time. By juxtaposing all time steps, the visualization offloads the work of remembering previous states from the user's brain to the screen.

## When it applies

- When analyzing spatiotemporal data, particularly phenomena that spread or propagate geographically.
- When the analysis involves multiple types of tasks, such as finding peaks, comparing the scope of spread, and looking for temporal patterns.
- When screen real estate is sufficient to display all time steps without making individual maps illegibly small.

## Exceptions

For highly specific, singular tasks, other visualizations may be faster. The same study found:
- **Animation** is faster for the single task of judging the *direction* of spread.
- **Maps with temporal glyphs** are faster for looking up the *arrival time* at a single, specific location.
If your analysis is exclusively focused on one of these narrow tasks, consider the specialized alternative.

## Trade-offs

- **Loss of Detail:** To fit on one screen, individual maps in a small-multiple display are smaller than a single animated map, which can obscure fine-grained spatial detail.
- **Lower Engagement:** Viewers, particularly non-experts, often find animations more engaging and report higher confidence, even if their performance is worse. Small-multiples may be perceived as more clinical or complex.
- **Space:** This technique requires significant screen real estate, and its effectiveness diminishes as the number of time steps increases, forcing maps to become smaller.

## Signs of Trouble

- **Scrubbing Fatigue:** With an animated view, you find yourself constantly scrubbing a timeline back and forth to compare two moments.
- **Memory Errors:** You can't remember what the map looked like 10 seconds ago in an animation to compare it with what you're seeing now.
- **"Where's Waldo" for Time:** You are hunting across a series of separate, disconnected views to find a specific pattern, instead of seeing it all in one place.

## How to Improve

- **Quick approach: Switch to Small-Multiples.** If you are using animation, convert the frames into a static grid of small maps. This immediately provides an overview and aids comparison.
- **Moderate approach: Implement Brushing and Linking.** In your small-multiple view, add interactivity so that hovering over a region in one map highlights the same region in all other maps. This helps track a single location through time.
- **Comprehensive approach: Provide Multiple Coordinated Views.** Offer both an animated view for its narrative power and a small-multiple view for analytical rigor. Link them so that playing the animation highlights the corresponding frame in the static grid. This gives the user the benefits of both approaches.