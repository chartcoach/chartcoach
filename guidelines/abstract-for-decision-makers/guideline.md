---
id: abstract-for-decision-makers
title: Abstract Complex Data for Decision-Makers
bibliography: references.bib
description: When presenting to high-level stakeholders, focus on information design
  that conveys essential issues rather than raw analytical data.
labels:
- task:communicate
- audience:executive
- impact:clarity
- visual:abstraction
- complexity:low
---

## The Rule <!-- role: advice -->
When designing for high-level decision-makers, strictly limit visualization to the essential matters of interest. Do not present the raw aggregates or complex exploration tools used by analysts.

## The Logic <!-- role: reason -->
According to [@kohlhammer_toward_2012], the policy-making chain involves stakeholders with heterogeneous skills. While analysts require tools to aggregate and browse vast amounts of data, the actual decision-making occurs higher up the chain.
*   **The Principle:** Information Design.
*   **The Evidence:** The authors argue that at the decision-making level, "the main target is to convey a matter of interest and present the essential issues" using rules of adequate information presentation and communication, rather than data exploration [@kohlhammer_toward_2012].

## Where to Apply <!-- role: context -->
*   **User Goal:** Communicating a finalized policy recommendation or defining an agenda.
*   **Data Type:** Synthesized outcomes, risk summaries, or high-level trends.
*   **Audience:** Decision-makers (e.g., politicians, executives) who are not domain experts in the underlying data science.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user is a policy *analyst* or researcher.
*   **Reason:** Analysts need "Information Visualization" or "Visual Analytics" tools to "aggregate vast amounts of data, analyze it, and form an overview of it" before they can synthesize it for others [@kohlhammer_toward_2012].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose transparency regarding the raw data and granular nuance.
*   **The Risk:** Oversimplification can hide outliers or edge cases that might be relevant to specific constituents.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Showing the full dashboard used for analysis to the final decision-maker.
*   **Why it fails:** It overwhelms the user with "vast amounts of data" rather than communicating the "knowledge" derived from perception science [@kohlhammer_toward_2012].

## How to Check <!-- role: check -->
*   **Visual Sign:** The display contains complex filtering controls or high-density raw data plots.
*   **The Test:** Can a non-expert identify the "matter of interest" within 5 seconds without interacting with the data?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Remove interactive filtering controls and highlight only the key insight.
*   **Best Fix:** Transition from an exploratory interface to an explanatory infographic or narrative visualization that guides the viewer to the specific policy issue.
