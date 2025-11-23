---
id: conform-to-accessibility-standards
title: Conform to Established Accessibility Standards
bibliography: references.bib
description: Ensure data visualizations meet baseline regulatory and technical accessibility
  standards like WCAG or Section 508.
labels:
- impact:accessibility
- impact:compliance
- source:chartability
- visual:code
- tool:assistive-technology
---

## The Rule <!-- role: advice -->
Ensure your visualization strictly conforms to appropriate compliance standards, such as WCAG 2.1, Section 508, or equivalent regional requirements. Treat non-compliance with these standards as an automatic failure of the visualization's accessibility audit.

## The Logic <!-- role: reason -->
This guideline falls under the **Robust** principle of the Chartability framework, ensuring the design works with the user’s compliant, assistive technologies of choice [@elavsky_how_2022].
*   **The Principle:** Compatible Parsing.
*   **The Evidence:** To ensure content can be interpreted consistently by assistive technologies, markup must be used in a way that can be unambiguously parsed. Elements must be properly nested and possess unique start and end tags [@w3c_understanding_ensure]. Without this technical foundation, higher-level accessibility strategies will fail to function.

## Where to Apply <!-- role: context -->
*   **User Goal:** Accessing data using assistive technologies (e.g., screen readers, braille displays) or requiring specific browser accommodations.
*   **Data Type:** All web-based or digital data visualizations and interfaces.
*   **Audience:** Any user base that includes people with disabilities protected by legal standards (e.g., 55% of the world's population is influenced by WCAG policy [@elavsky_how_2022]).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Non-Digital or Physical Media.
*   **Reason:** While digital standards are robust, they have limited transferability to physical contexts. For example, tactile graphics guidelines require different considerations for information prioritization and layout than digital DOM structures [@elavsky_how_2022].
*   **Scenario:** "Information-Rich" Gaps.
*   **Reason:** You should not *break* the standard, but you must recognize that standards often fall short for information-rich systems like data visualizations. General standards may only account for up to half of the needs of people with disabilities, necessitating additional heuristics beyond basic compliance [@elavsky_how_2022].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Testing for compliance is labor-intensive. Auditing complex data systems is a "daunting and often expensive task," and novices often struggle to organize knowledge across non-specific standards bodies [@elavsky_how_2022].
*   **The Risk:** "Access is an experience, not just compliance." Strictly following standards without user testing may result in a technically compliant but unusable experience. Experts note that general standards bodies like WCAG can neglect the diverse accessibility needs specific to data visualization, such as cognitive or vestibular considerations [@elavsky_how_2022].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Relying solely on automated compliance checkers.
*   **Why it fails:** State-of-the-art automated checkers only find approximately 57% of accessibility errors. Accessible experiences must still be manually designed and checked for quality [@elavsky_how_2022].
*   **The Wrong Fix:** Ignoring standards because visualization is "custom."
*   **Why it fails:** Chartability is not intended to replace existing standards but to work alongside them. Ignoring the baseline WCAG criteria renders the visualization robustly inaccessible regardless of other design efforts [@elavsky_how_2022].

## How to Check <!-- role: check -->
*   **Visual Sign:** Broken layout in high-contrast modes or unreadable code structures.
*   **The Test:** Perform a baseline audit against WCAG 2.1 or Section 508 criteria. If the visualization fails these general standards, it is considered a failure in Chartability until remediated. Use tools like Axe-core or similar automation as a first pass, followed by manual verification [@elavsky_how_2022].

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Utilize semantic HTML and standard ARIA patterns ensuring all elements are properly nested and parsed.
*   **Best Fix:** Integrate compliance testing into the development lifecycle (e.g., automated unit tests) and supplement with the Chartability heuristics (POUR + Compromising, Assistive, Flexible) to address the gaps where general standards fall short [@elavsky_how_2022].
