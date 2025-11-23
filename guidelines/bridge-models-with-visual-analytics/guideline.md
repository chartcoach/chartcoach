---
id: bridge-models-with-visual-analytics
title: Use Visualization to Control Computational Models
bibliography: references.bib
description: Use interactive visualization to allow non-experts to steer complex algorithms
  and simulations.
labels:
- task:steer
- task:analyze
- system:visual-analytics
- audience:analyst
- complexity:advanced
---

## The Rule <!-- role: advice -->
Use interactive visual interfaces to let users set parameters for and control automatic analysis algorithms. Do not expect analysts to interact with computational models (like simulations or mining tools) directly via code or raw inputs.

## The Logic <!-- role: reason -->
Political analysts cannot be experts in every computational discipline (KDD, simulation, opinion mining). Visual Analytics (VA) acts as the bridge.
*   **The Principle:** Human-Computer Collaboration.
*   **The Evidence:** VA combines "computers' data-processing capabilities with the strength of humans' visual perception." It allows users to "interactively control computers to get a more precise analysis" without needing deep algorithmic expertise [@kohlhammer_toward_2012].

## Where to Apply <!-- role: context -->
*   **User Goal:** Impact analysis or evaluating policy scenarios.
*   **Data Type:** Output from social simulations, opinion mining algorithms, or complex statistical models.
*   **Audience:** Policy analysts who understand the domain but are not computer scientists.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Simple descriptive statistics.
*   **Reason:** If the data requires only aggregation and no complex algorithmic processing, standard Information Visualization techniques are sufficient [@kohlhammer_toward_2012].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Development complexity increases significantly, as the visualization must be tightly coupled with the backend calculation engine.
*   **The Risk:** The user might misinterpret the model's output if the visual metaphor for the control parameters is ambiguous.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using visualization only for "postprocessing"—showing the results after the calculation is done.
*   **Why it fails:** It prevents the iterative exploration where users "detect interesting patterns... and can control computers to get a more precise analysis" [@kohlhammer_toward_2012].

## How to Check <!-- role: check -->
*   **Visual Sign:** The interface is a static report of a simulation run.
*   **The Test:** Can the user change a variable (e.g., a budget constraint) and immediately see the visual impact on the simulation result?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add basic parameter sliders that trigger a re-calculation of the visualization.
*   **Best Fix:** Implement a full "Visual Analytics" loop where interaction with the data points themselves (e.g., selecting a cluster) feeds back into the model parameters.
