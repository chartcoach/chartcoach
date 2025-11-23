---
id: map-causal-relationships
title: Map Causal Variables to Reveal Intervention Points
bibliography: references.bib
description: Use influence diagrams to visualize causal links and variables, helping
  users create new options rather than just choosing among fixed ones.
labels:
- chart:network-diagram
- chart:flow-chart
- task:planning
- impact:exploration
- data:causal
---

## The Rule <!-- role: advice -->
When the goal is to help users create new solutions (rather than choose from a fixed list), visualize the system using influence diagrams. Display variables as nodes and causal relationships as links, explicitly including factors that might be uncertain or social in nature.

## The Logic <!-- role: reason -->
*   **The Principle:** Mental Models and Influence Diagrams.
*   **The Evidence:** [@fischhoff_communicating_2014] argues that to create options (e.g., how to ensure water safety), people need to understand how the world works. Influence diagrams allow users to simulate outcomes mentally and identify specific nodes where they can intervene to reduce uncertainty or improve results.

## Where to Apply <!-- role: context -->
*   **User Goal:** "Creating options" or complex problem solving (e.g., disaster response, policy making, engineering design).
*   **Data Type:** System models involving multiple interacting variables and probabilities.
*   **Audience:** Planners, engineers, or policymakers who need to identify leverage points in a system.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user is choosing among fixed, pre-determined options (e.g., which medical treatment is best).
*   **Reason:** In fixed-choice scenarios, the causal mechanism is less important than the comparative probability of outcomes. A box plot or probability distribution is more effective here [@fischhoff_communicating_2014].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Visual simplicity. Influence diagrams can become cluttered "spaghetti charts" if too many variables are included.
*   **The Risk:** Omitted variable bias. If the model neglects social factors (e.g., public opposition to technology), the visualization may give a false sense of completeness.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Listing facts or bullet points without showing connections.
*   **Why it fails:** It relies on the user's internal intuition to connect the dots, which is often flawed regarding dynamic or nonlinear processes.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there arrows connecting concepts?
*   **The Test:** Can the user trace a path from an intervention (e.g., "Boil water") to an outcome (e.g., "Health effects") through intermediate steps?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Draw a simple flow chart of the process.
*   **Best Fix:** Create a formal influence diagram (like Fig. 3 in the paper) where nodes represent variables and arrows represent probabilistic dependencies.
