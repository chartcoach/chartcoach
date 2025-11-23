---
id: provide-bias-correction-instructions
title: Instruct Users on Specific Visual Biases
bibliography: references.bib
description: Accompany uncertainty visualizations with instructions that explicitly
  warn against specific errors, like the collocation effect.
labels:
- chart:ensemble-plot
- task:education
- impact:decision-making
- audience:novice
- visual:annotation
---

## The Rule <!-- role: advice -->
When presenting complex uncertainty visualizations, provide task-specific instructions that explicitly explain the potential visual bias (e.g., "Don't focus on line overlap") rather than just explaining how the visualization was generated.

## The Logic <!-- role: reason -->
Visual marks (bottom-up processing) have a powerful influence that can override general knowledge. Merely explaining how a chart is made is often insufficient to correct decision-making errors.
*   **The Principle:** Knowledge-Driven Processing. To override the strong perceptual influence of visual marks (like a line hitting a dot), users need "top-down" strategies to consciously correct their intuition.
*   **The Evidence:** [@padilla_powerful_2020] found that "task-specific" instructions—which warned users about the collocation effect and gave practice overcoming it—reduced bias significantly more than "visualization-instructions" that only explained the modeling technique.

## Where to Apply <!-- role: context -->
*   **User Goal:** Making high-stakes decisions based on probabilistic visualizations (e.g., evacuation decisions).
*   **Data Type:** Visualizations known to elicit specific heuristics, such as spaghetti plots (collocation effect) or summary cones (containment bias).
*   **Audience:** Non-experts who lack the statistical training to naturally inhibit perceptual biases.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Time-critical emergency alerts (e.g., a 5-second TV spot).
*   **Reason:** Lengthy instructions may distract from the immediate warning. However, the visualization *design* itself must then be robust enough to minimize bias without instruction.

## The Price <!-- role: costs -->
*   **The Sacrifice:** User time and attention. Instructions add friction before the user engages with the data.
*   **The Risk:** Users may skip the instructions entirely. Note that even with good instructions, [@padilla_powerful_2020] found the bias was reduced but never completely eliminated.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Providing a technical legend or "About" section that only details the simulation parameters or algorithm.
*   **Why it fails:** Users understand *what* the data is but not *how* their brain will trick them when looking at it.
*   **The Wrong Fix:** Assuming that "better data" needs no explanation.
*   **Why it fails:** Even statistically accurate ensemble displays trigger the collocation effect without guidance.

## How to Check <!-- role: check -->
*   **Visual Sign:** Read your help text or intro video. Does it say "This chart was made using Monte Carlo simulations..."? Or does it say "Be careful not to assume..."?
*   **The Test:** If the text describes the *creator's* workflow, it is insufficient. It must describe the *viewer's* strategy.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a warning label: "Note: The storm may travel between the plotted lines."
*   **Best Fix:** Include a brief tutorial or video that demonstrates the error (e.g., "You might think Location A is safer because a line doesn't touch it, but that is incorrect") and provides the correct reading strategy.
