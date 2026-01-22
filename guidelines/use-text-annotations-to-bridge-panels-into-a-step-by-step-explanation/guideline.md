---
id: use-text-annotations-to-bridge-panels-into-a-step-by-step-explanation
title: Add text annotations that connect panels into a step-by-step narrative
bibliography: references.bib
description: Use brief annotation text to explicitly state the takeaway of each panel
  and the transition to the next, turning trends into a coherent story.
labels:
- chart:line
- task:explain
- visual:annotation
- impact:storytelling
- data:temporal
- audience:general
- technique:small-multiples
---

## Write the story on the chart with short, panel-bridging annotations <!-- role: advice -->

Add short text annotations that state each panel’s key takeaway and explicitly connect it to the next panel in the sequence. Make the annotations do narrative work (e.g., “but…”, “and…”, “the result…”) rather than restating axis labels.

## Why annotations make “bonkersness” and connections visible <!-- role: reason -->

A set of time series can be accurate yet emotionally flat or conceptually disconnected. Annotations provide the missing narrative glue: they tell readers what to notice, how one trend relates to the next, and what conclusion to draw from the set.

**Mechanism:** Explicit statements reduce the chance that readers form their own (possibly unintended) interpretation and increase the salience of the intended connections across panels.

**Evidence:** Filling a sequential small-multiple chart with narrative annotations transforms separate demographic lines into an unfolding explanation that highlights how changes relate and culminate in a combined outcome. [@mintzer_sequential_storytelling_2024]

**Notes:** Annotations can be short; the value is in the transitions and the explicit takeaway, not in long prose.

## When panel-bridging annotations are especially useful <!-- role: context -->

- **User Goal:** Feel the magnitude of change and understand how multiple trends connect.
- **Task:** Extract the intended takeaway from each panel and integrate them into one conclusion.
- **Data:** Multi-indicator time series where the combined interpretation matters more than any single series.
- **Chart Setting:** Editorial/story context where guiding attention is appropriate.
- **Audience:** Readers who may not be comfortable inferring relationships from trend lines alone.
- **Success Criterion:** Readers can explain the narrative chain and the final implication after skimming.

## When to avoid heavy annotation <!-- role: exceptions -->

**Break it when:** The chart must serve as a neutral reference graphic with minimal framing. **Why:** Narrative annotations can be perceived as editorializing and may reduce perceived objectivity.

## Tradeoffs of adding narrative text <!-- role: costs -->

**Sacrifice:** More space and design time, and less room for the data itself. **Risk:** Poorly worded annotations can overstate causality or distract from the quantitative message. **Mitigation:** Keep text tightly tied to what the chart shows and focus on relationships and takeaways.

## Common annotation pitfalls <!-- role: mistakes -->

- **Mistake:** Using only a strong title and no in-chart explanation. **Why it fails:** Readers may not connect the indicators or notice the intended “result” of the sequence.
- **Mistake:** Writing annotations that merely repeat what the axis already says. **Why it fails:** It adds clutter without providing narrative linkage or meaning.

## Quick checks for annotation quality <!-- role: check -->

**Failure Sign:** Readers can describe each panel but cannot explain how they connect or what the combined conclusion is. **Quick Check:** Remove the title and ask whether the annotations alone still communicate the intended storyline. **Stronger Test:** Ask a reader to paraphrase the story using the annotation connectors (“but”, “and”, “result”); missing connectors indicate weak narrative bridging.

## If annotations aren’t enough, adjust the structure <!-- role: fix -->

- Rewrite annotations to emphasize transitions between panels rather than isolated facts.
- Move the “result” statement (the combined takeaway) onto the figure so it’s not only in surrounding article text.
- Simplify the number of annotated points so each annotation is a clear, high-signal sentence.
- If the narrative is complex, split into two sequential charts so each has a simpler annotated storyline.
