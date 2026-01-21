---
id: avoid-3d-when-comprehension-depends-on-navigation-in-static-contexts
title: Avoid 3D When Navigation Is Required but Interaction Is Not Guaranteed
bibliography: references.bib
description: Do not rely on 3D views that require navigation to be understood when
  the chart may be used as a static image or in constrained interaction settings.
labels:
- chart:scatter
- task:present
- impact:clarity
- data:any
- audience:general
- complexity:basic
---

## The Rule <!-- role: advice -->

Do not use a 3D view that requires navigation to understand the data if the visualization may be consumed as a static image or with limited shared control.

## The Logic <!-- role: reason -->

3D navigation is a critical failure point when the scene is incomprehensible from a single viewpoint; in real usage, charts often end up as static snapshots (reports, slides) or in collaborative settings where only one person can interact, making navigation dependence a liability [@brath3DInfoVisHere2014].

- **The Principle:** Don’t make comprehension conditional on interaction that may not be available.
- **The Evidence:** [@brath3DInfoVisHere2014]

## Where to Apply <!-- role: context -->

- **User Goal:** Communicate findings reliably in documents, presentations, or group reviews.
- **Data Type:** Any 3D layout that needs rotation/zoom to resolve ambiguity (commonly free-form 3D point clouds).
- **Audience:** Mixed audiences and stakeholders in non-interactive settings [@brath3DInfoVisHere2014].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The 3D configuration is readable without navigation because the data/structure provides sufficient cues.
- **Reason:** Some 3D scenes remain comprehensible from a stable view if the structure is inherently readable [@brath3DInfoVisHere2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may give up 3D-specific benefits (spatial separation, certain mental models).
- **The Risk:** Choosing 2D may require alternative encodings that reduce dynamic range or introduce overplotting [@brath3DInfoVisHere2014].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming “users can just rotate it” as the primary readability strategy.
- **Why it fails:** Interaction is frequently unavailable or constrained in real communication workflows [@brath3DInfoVisHere2014].

## How to Check <!-- role: check -->

- **Visual Sign:** A single screenshot looks ambiguous (depth ordering unclear; key structure hidden).
- **The Test:** Export one static frame—if a viewer cannot answer the main question from that frame, the design depends on navigation [@brath3DInfoVisHere2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Choose a default camera/view that makes the main structure legible without interaction.
- **Best Fix:** Replace the 3D view with a representation that communicates the same insight in a static-friendly way, or add coordinated 2D views to carry the message [@brath3DInfoVisHere2014].
