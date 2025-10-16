---
id: short-slug
title: "Imperative, directional instruction"

tags:
  # Impact dimensions (select all that apply)
  - impact:perceptual
  - impact:cognitive
  - impact:accessibility
  - impact:inclusion
  - impact:logos
  - impact:pathos
  - impact:ethos
  - impact:ethical
  - impact:aesthetic
  - impact:performance

  # Chart types (use hierarchy with dots for specificity)
  - chart:bar
  - chart:line
  - chart:scatter
  - chart:pie
  - chart:map
  - chart:map.choropleth
  - chart:map.small-multiples
  - chart:map.glyphs

  # Tasks (what the user is trying to accomplish)
  - task:compare
  - task:rank
  - task:lookup
  - task:trend
  - task:direction
  - task:correlation
  - task:distribution
  - task:composition
  - task:summary-mean
  - task:summary-median

  # Data characteristics
  - data:quantitative
  - data:categorical
  - data:temporal
  - data:spatial
  - data:spatiotemporal
  - data:periodicity.24h
  - data:cardinality.high
  - data:cardinality.low

  # Visual channels
  - visual:color
  - visual:position
  - visual:size
  - visual:shape
  - visual:texture

  # Audience characteristics
  - audience:general
  - audience:expert
  - audience:low-literacy

  # Medium/format
  - medium:static
  - medium:interactive
  - medium:animation
  - medium:print
  - medium:screen

  # Accessibility risks
  - access:color-vision-risk
  - access:screenreader-risk
  - access:motor-control-risk
  - access:cognitive-load-risk

evidence:
  strength: high # Options: high | medium | low
  summary: "Cleveland & McGill (1984, n=55) replicated across 8+ studies through 2019, showing position 20-40% more accurate than angle (p<0.001, d=0.72)"

sources:
  - type: research
    ref: "Cleveland & McGill, 1984"
    url: https://doi.org/10.2307/2288400
    note: "Foundational study (n=55) establishing perceptual ranking with significant accuracy differences (p<0.001)"
    role: primary # Options: primary | supporting | related
  - type: research
    ref: Heer & Bostock, 2010
    url: https://doi.org/10.1145/1753326.1753357
    note: "Crowdsourced replication (n=1,935) confirming original findings across diverse visualizations"
    role: supporting
  - type: standard
    ref: WCAG 2.1
    url: https://www.w3.org/TR/WCAG21/
    role: related
  - type: practitioner
    ref: DataViz Society Best Practices
    url: https://www.datavizsociety.org/best-practices
    role: related

tools:
  - type: implement
    name: Tool Name
    url: https://example.com
    description: Brief description of what it does
  - type: validate
    name: Tool Name
    url: https://example.com
    description: Brief description of what it checks
  - type: learn
    name: Resource Name
    url: https://example.com
    description: Brief description of what it teaches

examples:
  - type: good
    description: Brief description of what makes this a good example
    url: https://example.com/chart-or-image.png # optional
  - type: bad
    description: Brief description of what's wrong and why it's problematic
    url: https://example.com/chart-or-image.png # optional
---

<!--
  FRONTMATTER GUIDE:

  id: Use a short, descriptive slug in lowercase-with-dashes format
      Example: "avoid-pie-charts" or "start-axis-at-zero"

  title: Write as an imperative command or clear instruction
         Examples: "Start bar chart axes at zero"
                  "Use position over color for quantitative comparisons"
                  "Avoid rainbow color schemes for ordered data"

  tags: A namespaced tag grammar for both human authors and AI agents.
        Use colons to create hierarchy, dots for fine-grained specificity.

        PURPOSE:
        Tags serve multiple critical functions:
        1. CONTEXTUALIZE: Describe the scenario, conditions, and constraints where this guideline applies
        2. SEARCH: Enable users to find relevant guidelines by filtering/browsing specific categories
        3. RETRIEVE: Allow systems to fetch guidelines matching a user's current situation
        4. RECOMMEND: Power AI agents to suggest appropriate guidelines based on user context
        5. RELATE: Connect guidelines that share common themes, concerns, or applicability

        FORMAT: {family}:{value}.{subvalue}
        Example: chart:map.choropleth, data:periodicity.24h, task:summary-mean

        EXTENSIBILITY:
        This tag system is FLEXIBLE and EXTENSIBLE. The families listed below are common patterns,
        but you can create new families, values, and subvalues as needed for your specific domain.
        The system will automatically leverage any tags following the {family}:{value}.{subvalue} format.

        Examples of custom tags:
          - domain:healthcare, domain:finance, domain:journalism
          - context:realtime, context:historical, context:predictive
          - scale:global, scale:national, scale:local
          - tone:formal, tone:casual, tone:technical

        AUTHORING FOR DISCOVERABILITY:
        - Tag generously: Include all relevant contexts where this guideline might apply
        - Think like a searcher: What words would someone use to find this guideline?
        - Use multiple specificity levels: Both chart:bar AND chart:bar.stacked if both apply
        - Consider the user's perspective: Tag based on what they see/feel, not just technical details
        - Include edge cases: If it applies to uncommon scenarios, tag those too
        - Mix concrete and abstract: chart:pie (concrete) + task:compare (abstract) = better matching

        ROUTING LOGIC:
        - Tags enable hierarchical matching: chart:map matches chart:map.choropleth
        - Use namespaces to route guidelines to specific contexts
        - The system will group and match tags by family, regardless of whether they're predefined
        - More tag matches = higher relevance score in search and recommendation systems

        COMMON TAG FAMILIES (use these as starting points, but feel free to extend):

        IMPACT DIMENSIONS (prefix: impact:)
        Tag all that apply to describe what aspect of the visualization this guideline affects:
          - impact:perceptual       → How visual information is perceived (accuracy, speed, discriminability)
          - impact:cognitive        → Memory load, attention, mental effort, comprehension complexity
          - impact:accessibility    → Screen readers, colorblindness, motor/cognitive disabilities, assistive tech
          - impact:inclusion        → Cultural sensitivity, diverse audiences, avoiding bias, universal design
          - impact:logos            → Logic, clarity, data integrity, reasoning (rational appeal)
          - impact:pathos           → Emotional impact, engagement, storytelling (emotional appeal)
          - impact:ethos            → Credibility, trust, professionalism, authority (trustworthiness)
          - impact:ethical          → Truthfulness, avoiding deception, transparency, fairness
          - impact:aesthetic        → Visual appeal, style, design quality, brand consistency
          - impact:performance      → Rendering speed, file size, scalability, technical efficiency

        CHART TYPES (prefix: chart:)
        Use hierarchy to route from general to specific:
          - chart:bar, chart:line, chart:scatter, chart:pie, chart:heatmap, chart:treemap
          - chart:map → general map guidance
          - chart:map.choropleth → specific to choropleth maps
          - chart:map.small-multiples → specific to small-multiple map arrangements
          - chart:map.glyphs → specific to maps with overlaid symbols/glyphs
        Example: A guideline tagged chart:map applies to ALL map types; chart:map.choropleth applies only to choropleths.

        TASKS (prefix: task:)
        What the viewer is trying to accomplish:
          - task:compare       → Comparing values across categories or groups
          - task:rank          → Determining order or ranking
          - task:lookup        → Finding specific data values
          - task:trend         → Identifying patterns over time
          - task:direction     → Determining if values are increasing/decreasing
          - task:correlation   → Finding relationships between variables
          - task:distribution  → Understanding spread and frequency
          - task:composition   → Seeing part-to-whole relationships
          - task:summary-mean, task:summary-median → Specific summary statistics

        DATA CHARACTERISTICS (prefix: data:)
        Properties of the underlying data:
          - data:quantitative, data:categorical, data:ordinal
          - data:temporal      → Time-series data
          - data:spatial       → Geographic/spatial data
          - data:spatiotemporal → Both space and time
          - data:periodicity.24h, data:periodicity.yearly → Repeating patterns
          - data:cardinality.high → Many unique values (>20)
          - data:cardinality.low  → Few unique values (<10)

        VISUAL CHANNELS (prefix: visual:)
        The visual encoding being used or discussed:
          - visual:color, visual:position, visual:size, visual:shape, visual:texture, visual:angle

        AUDIENCE (prefix: audience:)
        Who will be viewing/using the visualization:
          - audience:general      → General public, no domain expertise assumed
          - audience:expert       → Domain experts who understand technical details
          - audience:low-literacy → Users with limited reading/technical skills

        MEDIUM/FORMAT (prefix: medium:)
        How the visualization will be presented:
          - medium:static       → Non-interactive (PNG, PDF)
          - medium:interactive  → User can interact (hover, click, zoom)
          - medium:animation    → Animated/transitioning
          - medium:print        → Will be printed on paper
          - medium:screen       → Will be viewed on screen

        ACCESSIBILITY RISKS (prefix: access:)
        Specific accessibility concerns this guideline addresses:
          - access:color-vision-risk     → Colorblindness or color perception issues
          - access:screenreader-risk     → Screen reader compatibility
          - access:motor-control-risk    → Fine motor control challenges
          - access:cognitive-load-risk   → High cognitive demand or complexity

        HOW AN AI AGENT USES THESE TAGS:
        1. User describes their chart: "I have a choropleth map showing election results by county"
        2. Agent extracts context tags: chart:map.choropleth, data:spatial, data:categorical
        3. Agent queries guidelines matching these tags (hierarchically: chart:map OR chart:map.choropleth)
        4. Agent ranks results by relevance (more tag matches = higher priority)
        5. Agent presents most relevant guidelines first
        6. Agent explains why each guideline was recommended (based on matching tags)

        HOW A HUMAN AUTHOR OPTIMIZES TAGS FOR DISCOVERABILITY:

        STEP 1 - Core Context (required):
        Ask: "What type of chart does this apply to?" → Add chart: tags
        Ask: "What task is the viewer doing?" → Add task: tags
        Ask: "What kind of data?" → Add data: tags

        STEP 2 - Impact & Constraints (recommended):
        Ask: "What's the impact?" → Add impact: tags
        Ask: "Any accessibility concerns?" → Add access: tags
        Ask: "What medium or audience?" → Add medium: and audience: tags

        STEP 3 - Discoverability & Edge Cases (optimize for search):
        Ask: "What problem does this solve?" → Tag the symptom (e.g., visual:color + access:color-vision-risk)
        Ask: "When would someone search for this?" → Include those search terms as tags
        Ask: "What related scenarios exist?" → Add tags for adjacent use cases
        Example: A guideline about pie charts should include task:compare (not just chart:pie)
                 because users searching for comparison guidance need to find it

        STEP 4 - Hierarchy & Specificity:
        Use dots for specificity: chart:map.choropleth is more specific than chart:map
        Include BOTH general and specific when appropriate: [chart:map, chart:map.choropleth]
        This ensures the guideline appears in both broad and narrow searches

        STEP 5 - Domain Extensions (as needed):
        CREATE NEW TAG FAMILIES for your specific domain (e.g., domain:healthcare, tone:formal)
        The system will recognize and use any tag following the {family}:{value}.{subvalue} pattern

        GOLDEN RULE: When in doubt, add more tags. Over-tagging beats under-tagging for discoverability.

  evidence: A lightweight object capturing the overall strength and synthesis of supporting evidence.
    Required fields:
    - strength: Overall confidence level based on the quality and replication of sources
    - summary: Brief synthesis of the evidence base (1-2 sentences)

    FIELD: strength
    Options: high | medium | low

    Choose based on the quality and breadth of sources listed below:
    - high: Meta-analyses, systematic reviews, or multiple replicated foundational studies over decades.
            Well-established principles with broad consensus (e.g., "position is more accurate than angle").
            Typically supported by multiple "primary" research sources or authoritative standards.
    - medium: Single high-quality peer-reviewed study, or consistent findings across a few studies.
              Strong evidence but less extensive replication or time-tested validation.
              Typically supported by 1-2 "primary" research sources.
    - low: Preliminary findings, exploratory studies, or practitioner consensus without formal research.
           Valuable insights but not yet robustly validated across contexts.
           May rely primarily on practitioner sources or single preliminary studies.

    FIELD: summary
    A brief, concrete synthesis of how this guideline was established or validated.
    This should tie together the sources listed below, providing a high-level view of the evidence base.

    Be specific and QUANTITATIVE whenever possible:
    - Key findings with numbers (e.g., "Shows 35% faster task completion, p<0.001")
    - Sample sizes and contexts (e.g., "Tested with 120 participants across 3 experiments")
    - Effect sizes and significance (e.g., "Cohen's d=0.8, indicating large effect")
    - Replication history (e.g., "Replicated in 8 independent studies from 1984-2019")
    - Consensus status (e.g., "Consistent recommendation across major newsroom style guides")
    - Standard requirements (e.g., "Required by WCAG 2.1 AA for contrast ratios")

    INCLUDE QUANTITATIVE DETAILS from experiments whenever available:
    - Statistical significance (p-values, confidence intervals)
    - Effect sizes (Cohen's d, eta-squared, etc.)
    - Sample characteristics (n=, demographics, expertise level)
    - Performance metrics (accuracy %, time in seconds, error rates)

    Keep it to 1-2 sentences. This is a synthesis, not a duplication of individual source notes.

    WHY THIS APPROACH:
    - Avoids duplication: The `evidence` object provides a high-level summary; `sources` provide details
    - Natural connection: The `type` and `role` fields in sources indicate their evidential contribution
    - Flexibility: Sources can serve different roles (primary evidence, supporting, or just related context)
    - Clarity: Readers see both the forest (evidence summary) and the trees (individual sources)

    Examples:
      evidence:
        strength: high
        summary: "Cleveland & McGill (1984, n=55) replicated in 8+ studies through 2019, consistently showing position judgments 20-40% more accurate than angle/area (p<0.001, Cohen's d=0.72)"

      evidence:
        strength: medium
        summary: "Single well-controlled 2019 study (n=120, between-subjects design) showing 28% improvement in pattern recognition (p=0.003), but awaiting replication"

      evidence:
        strength: low
        summary: "Emerging consensus from practitioner guides (FT, NYT, Economist) based on newsroom experience, but no formal empirical validation yet"

      evidence:
        strength: high
        summary: "Required by WCAG 2.1 Level AA (4.5:1 minimum contrast) based on extensive accessibility research with low-vision users showing 67% improvement in readability"

  sources: List of references that support this guideline (optional - omit section entirely if none)
    Each source is an object with:
    - type: One of "research" (peer-reviewed), "standard" (WCAG, ISO), "practitioner" (style guides), "personal" (team rules)
    - ref: Short citation (e.g., "Cleveland & McGill, 1984" or "WCAG 2.1")
    - url: Full URL or DOI link (optional but preferred)
    - note: Additional context about what this source specifically supports (optional)
            INCLUDE QUANTITATIVE DETAILS when available: sample sizes, effect sizes, p-values, etc.
    - role: Indicates this source's relationship to the evidence (optional but recommended)
            Options: "primary" (core evidence), "supporting" (reinforces/replicates), "related" (contextual)

    The `role` field helps connect sources to the evidence summary:
    - primary: This is a foundational or key piece of evidence for the guideline
    - supporting: This reinforces, replicates, or extends the primary evidence
    - related: This provides useful context but isn't core to the evidence claim

    Examples:
      - type: research
        ref: "Cleveland & McGill, 1984"
        url: https://doi.org/10.2307/2288400
        note: "Foundational study (n=55) establishing perceptual ranking with significant accuracy differences (p<0.001)"
        role: primary
      - type: standard
        ref: WCAG 2.1 Success Criterion 1.4.3
        url: https://www.w3.org/TR/WCAG21/#contrast-minimum
        note: "Requires 4.5:1 minimum contrast ratio for normal text"
        role: primary
      - type: practitioner
        ref: Financial Times Visual Vocabulary
        url: https://ft.com/vocabulary
        role: related
      - type: personal
        ref: Internal design system v2.1
        note: "Established Q2 2024 based on usability testing (n=8 client teams, 45% reduction in support tickets)"
        role: primary

  tools: List of tools/resources to implement, validate, or learn about this guideline (optional - omit section entirely if none)

    CRITICAL: AVOID DUPLICATION WITH SOURCES
    - If a paper/source is already listed in `sources`, DO NOT repeat it here as a "learn" tool
    - Respect the reader's time and cognitive load—every item should add unique value
    - Sources = evidence backing; Tools = practical implementation/validation/education

    Each tool is an object with:
    - type: One of "implement" (helps apply), "validate" (checks compliance), "learn" (educational)
    - name: Tool or resource name
    - url: Link to the tool/resource
    - description: Brief description of what it does

    WHEN TO USE "learn" TYPE:
    - Tutorials, interactive explainers, or educational resources that TEACH the concept
    - Blog posts or articles that EXPLAIN HOW TO APPLY the guideline in practice
    - NOT for the original research papers (those go in `sources`)
    - NOT for style guides already listed in `sources`

    Think: "Would this help someone DO something?" (implement/validate) or
           "Would this help someone UNDERSTAND how to apply this?" (learn, but not primary research)

    Examples:
      - type: implement
        name: Colorgorical
        url: http://vrl.cs.brown.edu/color
        description: Generate categorical color palettes optimized for perceptual difference
      - type: validate
        name: Viz Palette
        url: https://projects.susielu.com/viz-palette
        description: Simulate how your palette looks to colorblind users
      - type: learn
        name: "Datawrapper: How to Pick Colors"
        url: https://blog.datawrapper.de/colors/
        description: Practical tutorial on applying color theory to real-world charts (NOT the original research)

  examples: List of illustrative examples showing the guideline in action (optional - omit section entirely if none)
    Each example is an object with:
    - type: One of "good" (follows guideline) or "bad" (violates guideline)
    - description: What to notice or what makes this example relevant (required)
    - url: Link to image, interactive example, or article (optional)
    - caption: Short label for the example (optional, for display purposes)

    Note: URLs can point to:
      - Image files (.png, .jpg, .svg, etc.) - either local paths or external URLs
      - Interactive visualizations
      - Articles or blog posts discussing the example
      - Any web resource that illustrates the point

    Each example should have either:
      - Just a description (text-only reference)
      - description + url (with link to resource)
      - description + url + caption (for labeled examples)

    Examples:
      - type: good
        caption: Election forecast using position
        description: FiveThirtyEight's 2020 election forecast uses position to show probabilities, making comparisons clear and accurate
        url: https://projects.fivethirtyeight.com/2020-election-forecast/
      - type: bad
        caption: 12-slice pie chart
        description: Pie chart with 12 slices makes comparison nearly impossible—small differences are imperceptible
        url: /examples/bad-pie-12-slices.png
      - type: good
        description: Chart uses colorblind-safe palette from Okabe-Ito color scheme, ensuring all users can distinguish categories
-->

## Guidance

<!--
  The core actionable rule or recommendation.
  This should be a clear, imperative statement of what to do or avoid.
  Examples: "Use position rather than color for quantitative comparisons"
           "Avoid truncating the y-axis for bar charts showing magnitude"
           "Sort categorical data by value when order is not meaningful"
-->

A rule, preference, or suggestion—describe the recommended action, best practice, or stylistic preference.

## Why

<!--
  The reasoning, evidence, or intent behind the guidance.
  Explain WHY this guidance matters. This can reference:
  - Perceptual principles (how humans perceive visual information)
  - Cognitive limitations (working memory, attention)
  - Task performance (accuracy, speed of interpretation)
  - Accessibility concerns (colorblindness, screen readers)
  - Communication goals (clarity, persuasion)
  Keep it concise but substantive—2-4 sentences typically.
-->

Short explanation of reasoning, evidence, or intent. Can be perceptual, rhetorical, practical, or personal.

### Core Principle

<!--
  OPTIONAL: An explicit statement of the high-level, abstract principle underlying this guidance.
  This elevates the educational value by connecting the specific guidance to broader, generalizable concepts.
  Positioned here as a subheading under ## Why to show it's part of the justification.

  FOR HUMANS: Helps you understand the "why behind the why"—the foundational insight that explains
              this guidance and potentially many others. Makes the guideline more memorable and
              transferable to new situations not explicitly covered.

  FOR AI AGENTS: Provides a higher-level conceptual anchor that can inform recommendations when
                 exact matches aren't available. Enables principled reasoning about edge cases.

  WHEN TO INCLUDE:
  - When the guidance is an application of a well-known perceptual, cognitive, or design principle
  - When understanding the abstract principle helps users apply the guidance more flexibly
  - When the principle connects this guideline to others in a meaningful way

  WHEN TO SKIP:
  - When the guidance IS the principle (no higher abstraction exists)
  - When the main ## Why section already captures the principle clearly
  - When adding this would feel redundant or overly academic

  FORMAT:
  Write 1-2 sentences expressing the abstract principle in plain language.
  Avoid jargon. Aim for something memorable that could apply beyond this specific guidance.

  Examples:
    - "Humans judge quantities more accurately by comparing positions along a common scale than by comparing angles, areas, or colors."
    - "Visual encodings should match the structure of the data and the task—ordered data deserves ordered encodings."
    - "Reduce the cognitive work required to decode your visualization; every unnecessary step is a chance for misinterpretation."
    - "Make the most important comparisons the easiest to see."
-->

[Optional: State the high-level, abstract principle that justifies this guidance. Connect the specific rule to a broader, generalizable insight about perception, cognition, or design.]

## When it applies

<!--
  Contexts, cues, or situations where this guidance is relevant.
  List specific, observable conditions that indicate this guideline applies.
  Be concrete: mention chart types, data characteristics, tasks, or audience needs.

  FOR HUMANS: This helps you quickly determine if this guideline is relevant to your current work.
  FOR AI AGENTS: This provides natural language patterns that can be matched against user descriptions.
                 When a user says "I'm comparing sales across regions," the agent can match this to
                 guidelines that mention "comparing quantitative values across categories."

  Examples:
    - "When comparing quantitative values across categories"
    - "For time series with multiple overlapping lines"
    - "When the audience includes colorblind users"
    - "When you have more than 7 categorical colors"
    - "For small multiples where consistency is critical"
-->

- Observable cues, chart types, data, audience, or context where this is relevant.

## Exceptions

<!--
  Legitimate reasons to bend or ignore the guidance.
  Not every guideline applies universally. List circumstances where:
  - Breaking the rule is acceptable or even preferable
  - Other constraints take priority (branding, space, audience expectations)
  - The context makes the guidance irrelevant

  FOR HUMANS: This acknowledges real-world constraints and builds trust by showing flexibility.
  FOR AI AGENTS: This helps the agent avoid dogmatic recommendations. If the user mentions a constraint
                 listed here (e.g., "but our brand colors are..."), the agent can acknowledge the
                 exception and suggest adaptations instead of insisting on the rule.

  If there are no known exceptions, you can omit this section entirely or state "None known."
-->

- Legitimate reasons to bend or ignore the guidance.

## Trade-offs

<!--
  What you might sacrifice or what conflicts may arise.
  Acknowledge costs or tensions when applying this guidance:
  - Visual properties you give up (e.g., aesthetics for clarity)
  - Other guidelines that might conflict
  - Practical constraints (time, tooling, flexibility)

  FOR HUMANS: This shows empathy for real-world complexity and helps set expectations.
  FOR AI AGENTS: This enables the agent to ask clarifying questions. "This will improve accuracy but
                 may reduce visual appeal—which is more important for your use case?"

  If there are no significant trade-offs, you can omit this section entirely.
-->

- What you might sacrifice or what conflicts may arise.

## Signs of Trouble

<!--
  RENAMED FROM "Evaluate" - More engaging, diagnostic language.

  How to recognize when this guideline is being violated or when problems are present.
  Frame these as "red flags" or symptoms to watch for—things that suggest improvement is needed.

  FOR HUMANS: This is approachable and non-judgmental. It feels like a friendly expert helping you
              spot issues, not a test you might fail. Use plain language and relatable metaphors.

  FOR AI AGENTS: These are matchable patterns. When a user describes their chart ("the colors blend
                 together" or "it's hard to tell the bars apart"), the agent can match these phrases
                 to the symptoms listed here to identify which guidelines are relevant.

  Use bullet points with specific, observable signals. Make checks concrete and actionable.
  Consider including:
  - Visual tests anyone can do ("The Squint Test: If you squint, do categories blend?")
  - Tool-based checks ("Does a colorblindness simulator show lost distinctions?")
  - User feedback patterns ("Do viewers keep asking which line is which?")

  Examples:
    - **The Squint Test:** If you squint at your chart, do different categories blend into one?
    - **Subtle Neighbors:** Does your palette contain two very similar colors (light green and teal)?
    - **Legend Deception:** Were colors chosen using large swatches that look different from tiny chart marks?
    - **Back-and-Forth:** Do viewers have to repeatedly look between legend and chart to decode?
    - **Axis Truncation:** Y-axis starts at a value other than zero for a bar chart showing magnitude
    - **Color Overload:** More than 7 colors used for categorical distinction
-->

- **Signal A:** What to look for—be specific and observable.
- **Signal B:** Another tangible cue or symptom.

## How to Improve

<!--
  RENAMED FROM "Repair" - More positive, growth-oriented language.
  STRUCTURED IN TIERS - Acknowledges real-world time/effort constraints.

  Provide actionable steps to fix or improve when issues are present.
  Structure these by effort and impact to help users make practical decisions.

  FOR HUMANS: This is incredibly practical. It acknowledges you might not have time for a total redesign.
              It provides options for different scenarios, showing empathy for constraints.
              The tiered structure helps you make informed trade-offs between competing priorities.

  FOR AI AGENTS: The agent can parse these tiers to offer appropriate advice based on context.
                 It can ask: "Are you looking for a quick change, or are you open to a more thorough
                 redesign?" and provide the corresponding tier.

  STRUCTURE (choose meaningful tier labels based on the guideline):
  - **Quick/Minimal/Lightweight:** Low effort, immediate impact. Pragmatic workarounds that help now.
  - **Moderate/Balanced/Iterative:** Moderate effort, substantial improvement. More thorough but still practical.
  - **Comprehensive/Thorough/Ideal:** Higher effort, strongest alignment with this guideline's principles.

  IMPORTANT: Avoid absolute language like "best" or "perfect." Every solution involves trade-offs.
             Frame options as different points on the effort/impact spectrum, not as a hierarchy of correctness.
             Acknowledge what each approach prioritizes and what it sacrifices.

  Be specific about HOW to make the change, not just WHAT to change.
  Include tool recommendations if relevant.
  Acknowledge the trade-offs inherent in each approach.

  Examples:
    - **Quick Fix: Add Data Labels.** If you must keep the pie chart, add direct labels (e.g., "42%")
      to each slice. This lets viewers read exact values instead of estimating angles. Trade-off: doesn't
      address the root perceptual limitation, but provides an immediate accuracy escape hatch.

    - **Moderate Redesign: Unstack Your Bars.** Switch from a stacked bar chart to a grouped bar chart.
      This puts every bar on the same baseline, making comparisons substantially easier. Trade-off: uses
      more space and may be less effective for showing totals.

    - **Thorough Redesign: Use Position on a Common Scale.** Switch to a bar chart or dot plot. Position
      along a common scale is demonstrably more accurate for comparing quantitative values (Cleveland &
      McGill, 1984). Trade-off: may feel less familiar to audiences used to pie charts, requires more
      vertical space.
-->

- **Quick approach:** Minimal change with immediate impact. A pragmatic workaround or mitigation.

- **Moderate approach:** More thorough improvement requiring moderate effort. Addresses underlying issues while remaining practical.

- **Comprehensive approach:** Higher effort, stronger alignment with guideline principles. Acknowledge the trade-offs this approach involves.
