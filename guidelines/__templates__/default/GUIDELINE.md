---
# PERMANENT ID: URL-friendly kebab-case.
id: "unique-guideline-slug"

# TITLE: A strong, imperative command (The "Do This").
title: "Strong Action Verb Object"

# METADATA:
bibliography: references.bib
description: "A single-sentence summary for search results."

# LABELS: DISCOVERY & FILTERING
# Use the standard categories below to ensure your guideline is found in common searches.
# You are also free to add CUSTOM tags for your specific domain (e.g., tool:tableau, industry:finance).
labels:
  - "chart:[type]" # e.g., chart:bar, chart:scatter
  - "task:[action]" # e.g., task:compare, task:rank
  - "visual:[channel]" # e.g., visual:color, visual:position
  - "impact:[goal]" # e.g., impact:clarity, impact:accessibility
  - "data:[type]" # e.g., data:temporal, data:categorical
  - "audience:[group]" # e.g., audience:novice, audience:expert
  - "[custom]:[value]" # e.g., complexity:advanced, source:internal-policy
---

<!--
  AUTHORING TIP: STAY IN YOUR LANE
  To make this useful for AI, keep each section pure.
  - Don't put "Why" in the "Advice" section.
  - Don't put "Exceptions" in the "Context" section.
  - Trust the structure.
-->

## The Rule <!-- role: advice -->

<!-- Write this as a direct command. No fluff. Imagine you only have 10 seconds to tell a designer what to do. -->

State the rule clearly and immediately. (e.g., "Directly label your lines. Do not use a legend.")

## The Logic <!-- role: reason -->

<!-- Why does this work? Don't just say "it's better." Explain the mechanism. Is it about how the eye moves? How the brain counts? Cite your sources. -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** [Concept Name]
- **The Evidence:** [@citationKey]

## Where to Apply <!-- role: context -->

<!-- Describe the specific situation where this rule applies. Be specific about the data, the user, or the goal. -->

This advice is designed for specific moments.

- **User Goal:** What is the user trying to see? (e.g., "Comparing values precisely")
- **Data Type:** What does the data look like? (e.g., "High-density time series")
- **Audience:** Who is this for? (e.g., "General public")

## When to Break It <!-- role: exceptions -->

<!-- No rule is absolute. When is this advice actually WRONG? -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** [Describe the situation]
- **Reason:** Why the rule fails here.

## The Price <!-- role: costs -->

<!-- Every design choice has a cost. If I follow this rule, what do I lose? (e.g. "It takes up more space" or "It takes longer to read"). -->

Be honest about the downsides.

- **The Sacrifice:** What are you giving up?
- **The Risk:** What might go wrong?

## Common Mistakes <!-- role: mistakes -->

<!-- How do people usually screw this up? What are the bad "fixes" people try? -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** [Common bad practice]
- **Why it fails:** [Brief explanation]

## How to Check <!-- role: check -->

<!-- How can I tell if I've broken this rule? Give me a test. -->

- **Visual Sign:** What does the error look like?
- **The Test:** (e.g., "Squint your eyes," "Convert to grayscale")

## How to Fix <!-- role: fix -->

<!-- I've broken the rule. How do I solve it? Give me options. -->

- **Quick Fix:** The minimal effort change.
- **Best Fix:** The ideal solution (even if it requires changing the chart type).
