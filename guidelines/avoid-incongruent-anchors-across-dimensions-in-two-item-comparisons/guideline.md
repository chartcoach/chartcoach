---
id: avoid-incongruent-anchors-across-dimensions-in-two-item-comparisons
title: Avoid placing task-relevant and task-irrelevant anchor features on different
  items when speed matters
bibliography: references.bib
description: Prevent interference by not splitting salient anchor features across
  different objects in a two-item comparison.
labels:
- chart:bar
- task:compare
- visual:color
- impact:speed
- data:categorical
- audience:novice
- concept:congruency
---

## Keep anchor features congruent across dimensions in two-item displays <!-- role: advice -->

When a two-item display uses multiple dimensions, design it so the most anchor-like features across dimensions do not land on different items when the user must respond quickly. If one dimension is irrelevant to the task, avoid letting it create a strong competing anchor on the opposite item.

## Competing anchors increase interference even when viewers try to ignore them <!-- role: reason -->

Even when viewers’ eye movements are primarily guided by the task-relevant anchor point, features in a task-irrelevant dimension can still compete for attention and slow down responses. When preferred anchor points for different dimensions are split across different objects (“incongruent”), it creates attentional competition and increases response time.

**Mechanism:** Incongruent anchor placement increases conflict during the early stages of selecting an object for the comparison, requiring more top-down control to suppress the irrelevant relation and complete the relevant one.

**Evidence:** Response times were faster when a participant’s preferred size-anchor and contrast-anchor features appeared on the same bar (congruent) than when they appeared on different bars (incongruent) during orthogonal tasks where only one dimension was relevant [@michalVisualRoutinesAre2017]. This interference occurred despite first saccades largely following the task-relevant dimension’s anchor point [@michalVisualRoutinesAre2017].

**Notes:** The study cannot fully separate interference from top-down competition versus low-level salience, but both interpretations imply that splitting salient anchors across objects increases competition [@michalVisualRoutinesAre2017].

## When congruency problems arise <!-- role: context -->

- **User Goal:** Make a rapid correct judgment about a relation along one specified dimension.
- **Task:** Decide between two configurations (e.g., which side has the larger value) under time pressure.
- **Data:** Two values with an intended comparison dimension; an additional visual dimension varies but is not meant to be used.
- **Chart Setting:** Two-bar displays or other two-object layouts with multi-attribute encoding (e.g., size plus color/contrast).
- **Audience:** Any audience, especially where attentional control may be limited (learning settings, scanning tasks).
- **Success Criterion:** Faster responses without increasing errors when irrelevant features vary.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The task explicitly requires noticing a mismatch between dimensions (e.g., detecting inconsistency between size and color). **Why:** The “incongruent” arrangement is the signal, so removing it would remove the phenomenon to be detected [@michalVisualRoutinesAre2017].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Constraining congruency can reduce freedom to encode multiple variables on the same marks. **Risk:** Forcing congruency may hide meaningful variation in the secondary dimension. **Mitigation:** If both dimensions matter, treat both as task-relevant and give them separate structure (e.g., separate comparisons).

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using color/contrast to encode an irrelevant attribute while also making it the most visually anchor-like feature, and letting it oppose the task-relevant anchor on the other item. **Why it fails:** It increases competition and slows the intended relation judgment, even when viewers attempt to focus on the relevant dimension [@michalVisualRoutinesAre2017].

## Quick tests <!-- role: check -->

**Failure Sign:** Users are noticeably slower on cases where the “largest” value is not also the “most salient” by another dimension. **Quick Check:** Enumerate the four combinations of two binary dimensions (e.g., tall/short × dark/light) and flag the cases where the task-relevant anchor (e.g., tall) and the irrelevant anchor (e.g., dark) are on opposite items. **Stronger Test:** Time a small within-subject test comparing congruent vs incongruent variants while keeping the required judgment constant.

## What to do instead <!-- role: fix -->

- Remove variation in the irrelevant dimension for tasks that require a single relation judgment.
- Encode the irrelevant variable in a way that is less anchor-like for the intended task (so it does not create a competing “first pick”).
- Provide separate marks or separate panels for the second dimension so it does not compete within the same two-item comparison.
- Add explicit instruction near the chart indicating which dimension defines the required comparison.
