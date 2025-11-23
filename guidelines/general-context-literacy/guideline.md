---
id: general-context-literacy
title: Use General Contexts for Literacy-Agnostic Design
bibliography: references.bib
description: When designing for broad audiences, use data contexts familiar to the
  general public to ensure visualization literacy is tested, not domain knowledge.
labels:
- impact:accessibility
- impact:clarity
- audience:general
- audience:novice
- data:context
---

## The Rule <!-- role: advice -->
When designing visualizations for a general audience (or assessing their ability to read charts), use datasets with general, widely understood contexts (e.g., "height vs. weight") rather than specialized domain topics.

## The Logic <!-- role: reason -->
A user's inability to read a chart often stems from unfamiliarity with the subject matter, not the chart itself.
*   **The Principle:** **Contextual Familiarity.** Unfamiliar contexts introduce "bias" and cognitive load. To accurately measure or facilitate visualization literacy, the content itself must not require specific expertise.
*   **The Evidence:** In Section 3.1.3, [@lee_vlat_2017] states: "We avoided the potential bias of the familiarity of the contexts... Eventually, we decided on 12 datasets with general contexts that did not require specific expertise (e.g., monthly oil price, height vs. weight, popular girls' names)."

## Where to Apply <!-- role: context -->
*   **User Goal:** Ensuring the visualization is understood by a non-expert user base.
*   **Data Type:** Any dataset used for public communication, news, or general assessments.
*   **Audience:** Non-expert users (defined in the paper as users over 18 who are not domain experts).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Specialized Professional Dashboards.
*   **Reason:** If the tool is for petroleum engineers, using "oil well displacement" terminology is efficient and necessary, even if a layperson doesn't understand it.
*   **Scenario:** Educational Material.
*   **Reason:** If the specific goal is to *teach* the domain concept using the chart.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Nuance and specificity. General contexts are often simplified.
*   **The Risk:** The data might feel "generic" or less exciting to niche audiences.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using familiar nouns but unfamiliar attributes.
*   **Why it fails:** [@lee_vlat_2017] notes that one might be familiar with the context of a "car" but not the specific attribute of "displacement." Both the entity and the metric must be familiar.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there acronyms or technical units in the axis labels (e.g., "μmol/L")?
*   **The Test:** Show the chart title and axis labels to a person outside the field. If they ask "What does this word mean?", the context is too specific.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Rename axes using plain language descriptions (e.g., change "Displacement" to "Engine Size").
*   **Best Fix:** Swap the dataset for a universally understood analogy if the goal is purely to demonstrate a chart type or finding.
