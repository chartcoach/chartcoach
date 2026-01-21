---
id: require-graphical-designs-to-express-all-and-only-the-input-facts
title: Ensure the Graphic Encodes All and Only the Input Facts
bibliography: references.bib
description: "Only use a design whose encoding conventions represent exactly the intended\
  \ facts\u2014no omissions and no extra implied facts."
labels:
- chart:any
- task:communicate
- visual:encoding
- impact:correctness
- data:relational
- audience:any
- principle:expressiveness
- source:mackinlay-1986
---

## The Rule <!-- role: advice -->

Choose (or generate) a chart design only if it can encode **all** intended facts and encode **only** those facts.

## The Logic <!-- role: reason -->

A graphical presentation is a “sentence” in a graphical language with conventions that determine what facts it encodes; a design is acceptable only if the language can express the input **exactly** (no missing facts and no additional incorrect facts implied by geometry).

- **The Principle:** Expressiveness = “all facts” + “only facts”
- **The Evidence:** [@mackinlayAutomatingDesignGraphical1986b]

## Where to Apply <!-- role: context -->

- **User Goal:** Accurate communication of relational facts without introducing false implications
- **Data Type:** Relational data (functions, relations, shared domain sets)
- **Audience:** Any audience where correctness matters (analysis, reporting, decision-making)

## When to Break It <!-- role: exceptions -->

- **Scenario:** The chart is explicitly exploratory/illustrative and the audience is warned that the graphic may imply structure not present in the data.
- **Reason:** The paper’s criterion is for safe, correct presentation; relaxing it risks communicating false facts [@mackinlayAutomatingDesignGraphical1986b].

## The Price <!-- role: costs -->

- **The Sacrifice:** Fewer available chart types; you may have to use less familiar or more complex designs.
- **The Risk:** If you ignore the rule, viewers may infer incorrect relationships from the graphic’s implied semantics [@mackinlayAutomatingDesignGraphical1986b].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** “Any chart that shows the values is fine.”
- **Why it fails:** Many chart forms carry implicit semantics (e.g., ordering, continuity) that can add facts not in the dataset [@mackinlayAutomatingDesignGraphical1986b].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers can reasonably read additional structure (ordering, magnitude, continuity, dependency) that you did not intend.
- **The Test:** List the facts your chart’s encodings imply (e.g., ordering by length, functional dependency by unique positions) and verify the set matches the input facts exactly [@mackinlayAutomatingDesignGraphical1986b].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove or change the encoding channel that introduces unintended facts (e.g., replace bar length with point position).
- **Best Fix:** Switch to a graphical language whose conventions match the relation’s structure (nominal vs ordinal vs quantitative; functional vs nonfunctional) [@mackinlayAutomatingDesignGraphical1986b].
