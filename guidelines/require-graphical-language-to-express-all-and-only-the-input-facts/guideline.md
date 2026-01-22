---
id: require-graphical-language-to-express-all-and-only-the-input-facts
title: Require each graphic to encode all and only the intended facts
bibliography: references.bib
description: Treat a chart as valid only if it encodes every required fact and does
  not imply additional facts not present in the data.
labels:
- chart:general
- task:encode
- visual:semantics
- impact:accuracy
- data:relational
- audience:expert
- concept:expressiveness
---

## Expressiveness as “all and only” facts <!-- role: advice -->

Require that the chosen chart type can encode every intended fact and does not encode any additional facts beyond the input.

## Expressiveness prevents missing facts and unintended claims <!-- role: reason -->

A chart is a sentence in a graphical language; its syntax and semantic conventions determine exactly which facts are conveyed. Expressiveness must therefore include both completeness (all input facts are encoded) and exactness (no extra facts are encoded), because encoding extra structure can communicate false information.

**Mechanism:** Enforcing “all and only” facts prevents both under-specification (facts the chart cannot represent) and over-specification (facts the chart inadvertently suggests via its visual conventions).

**Evidence:** Expressiveness is defined as the existence of a graphical sentence that encodes all input facts and only those facts, because extra encoded facts can be incorrect [@mackinlayAutomatingDesignGraphical1986b]. Examples show both failure to encode required detail (scatter plot without labels when item identity matters) and accidental encoding of nonexistent ordering (bar lengths suggesting order for nominal categories) [@mackinlayAutomatingDesignGraphical1986b].

**Notes:** This rule applies before optimizing aesthetics or layout; a visually appealing chart that encodes extra facts is still wrong.

## When “all and only” expressiveness is the gate <!-- role: context -->

- **User Goal:** Communicate relational information without misstatement.
- **Task:** Choose a chart type that faithfully represents the relation structure.
- **Data:** Relations with domain types (nominal/ordinal/quantitative) and structural properties (functional dependencies, shared domain sets).
- **Chart Setting:** Static 2D graphics where meaning is carried by conventional encodings.
- **Audience:** Readers relying on visual conventions to infer meaning.
- **Success Criterion:** The chart implies no false facts and omits no required facts.

## When not to enforce “only the facts” literally <!-- role: exceptions -->

**Break it when:** You intentionally want the graphic to suggest additional interpretive structure not present in the data (for example, a deliberate rhetorical emphasis). **Why:** The goal is no longer strict factual expressiveness but persuasion or commentary, which this criterion is designed to avoid [@mackinlayAutomatingDesignGraphical1986b].

## Tradeoffs of strict expressiveness gating <!-- role: costs -->

**Sacrifice:** Some visually compact designs will be rejected because they omit detail or imply extra structure. **Risk:** You may end up with less visually “integrated” graphics (for example, aligned views) to preserve exactness. **Mitigation:** Treat expressiveness as a hard constraint, then optimize effectiveness within the expressive set.

## Common expressiveness failures <!-- role: mistakes -->

- **Mistake:** Using a chart that cannot represent the relation’s multiplicity (for example, one mark forced to represent multiple values). **Why it fails:** The graphic cannot encode all tuples without contradiction, so facts are lost [@mackinlayAutomatingDesignGraphical1986b].
- **Mistake:** Using a chart whose geometry implies structure your data does not have (for example, bar lengths for nominal categories). **Why it fails:** It encodes additional facts (like ordering) that are not true [@mackinlayAutomatingDesignGraphical1986b].

## Quick expressiveness tests <!-- role: check -->

**Failure Sign:** Viewers could infer a relationship (order, magnitude, continuity, uniqueness) that the dataset does not define. **Quick Check:** List the facts the chart makes visually comparable and confirm each is present in the data schema (domain type and dependencies). **Stronger Test:** Enumerate which visual encodings are active (position/length/area/color/etc.) and state the implied facts; confirm they match exactly the intended relation facts.

## What to do instead when expressiveness fails <!-- role: fix -->

- Choose a chart type whose semantic conventions match the relation structure (for example, avoid bar-length encodings for nominal values).
- Add or change encodings (such as labels or a different mark/axis scheme) so omitted required facts become representable.
- Split the information into multiple coordinated views when a single view would imply extra structure.
- Change the encoding technique (for example, swap an ordering-implying encoding for one that does not imply order).
