---
id: blend-visual-patterns-systematically
title: Blend Abstract Visual Patterns
bibliography: references.bib
description: Create novel visualizations by systematically combining abstract patterns
  like Token, Group, and Coordinate.
labels:
- chart:custom
- task:design
- visual:structure
- impact:creativity
- data:complex
- audience:designer
---

## The Rule <!-- role: advice -->
Construct complex visualizations by selecting and "blending" abstract structural patterns (such as Token, Hierarchy, Cell, or Coordinate) rather than selecting off-the-shelf chart types.

## The Logic <!-- role: reason -->
Big data tasks often require novel visualizations that do not fit into standard taxonomies (like "bar chart" or "scatter plot"). By treating visualization design as a blending of abstract patterns, designers can create sophisticated structures tailored to the specific data complexity. For example, blending `[Token•Group]` conveys uniqueness and classification simultaneously. This grammatical approach allows for "systematic, yet creative and flexible" design that captures the intricacies of big data [@ola_beyond_2016].

## Where to Apply <!-- role: context -->
*   **User Goal:** Designing a tool for a domain where standard charts fail to capture the depth of the data (e.g., global burden of disease analysis).
*   **Data Type:** Multifaceted data requiring the representation of hierarchy, relationships, and specific values simultaneously.
*   **Audience:** Visualization designers and developers building custom analytics tools.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Rapid prototyping for standard business reporting.
*   **Reason:** If a standard library chart (e.g., a basic line chart) answers the user's question, the overhead of designing a custom pattern blend is unnecessary.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Speed of implementation. Designing from first principles (patterns) takes longer than instantiating a library chart.
*   **The Risk:** Ad-hoc complexity. Without disciplined adherence to the framework, the blending can become messy.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Ad-hoc design.
*   **Why it fails:** Creating complex visuals without a framework (vocabulary and syntax) leads to inconsistent designs that are hard to evaluate or iterate upon [@ola_beyond_2016].

## How to Check <!-- role: check -->
*   **Visual Sign:** Can you describe your visualization using a structural formula (e.g., `V ∈ [Stack•Group•Token]`)?
*   **The Test:** Identify the "organizational affordances" of your visual. If you can't name the underlying patterns (e.g., "This organizes by stacking," "This organizes by linking"), the design may lack structure.

## How to Fix <!-- role: fix -->
*   **Best Fix:** Deconstruct the data requirements into organizational needs (e.g., "I need to show hierarchy" -> Hierarchy pattern; "I need to show membership" -> Group pattern). Blend these patterns to derive the final visual form [@ola_beyond_2016].
