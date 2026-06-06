# ChartCoach Guideline Catalog

## Section Roles

### advice

The design action a reader or agent can apply. Use this section when the task needs the concrete chart change first.

### reason

The rationale or source-backed mechanism behind the design action. Use this section when the task needs to justify why the advice works.

### context

The design context where the guideline applies, including audience, task, medium, data setting, or chart conditions.

### exceptions

Conditions where the design action should not be applied, or where another guideline should be checked first.

### costs

Tradeoffs introduced by the design action, including space, complexity, precision, effort, accessibility, or interpretation costs.

### mistakes

Common failure modes that occur when the design action is ignored or applied carelessly.

### check

Review steps for deciding whether a chart satisfies the guideline in a concrete design context.

### fix

Repair steps for changing an existing chart when the check section identifies a problem.

## Label Families

### access

Accessibility affordances or constraints that affect whether a design can be perceived, operated, or understood. Examples include `access:noncolor:use`, `access:keyboard:use`, and `access:screen-reader:use`.

### aesthetic

Visual-style concerns that affect composition, color, and presentation polish. Examples include `aesthetic:style:use`, `aesthetic:composition:use`, and `aesthetic:color:avoid`.

### audience

Audience groups or reader roles that change which guidance applies. Examples include `audience:general-public`, `audience:analyst`, and `audience:decision-maker`.

### basis

The broad source basis for the guideline claim. Examples include `basis:empirical`, `basis:heuristic`, and `basis:accessibility`.

### channel

Visual encoding channels affected by the guideline. Examples include `channel:position:use`, `channel:color-hue:avoid`, and `channel:length:avoid`.

### chart

Chart families, chart forms, or chart-form recommendations. Examples include `chart:bar`, `chart:scatter`, and `chart:text:avoid`.

### communication

Communication goals around framing, workflow, credibility, resonance, or explanatory context. Examples include `communication:framing`, `communication:credibility`, and `communication:context`.

### component

Chart parts that can be added, changed, removed, or reviewed. Examples include `component:axis:use`, `component:legend:avoid`, and `component:annotation:use`.

### data

Data types or data structures that shape chart choice and interpretation. Examples include `data:categorical`, `data:temporal`, and `data:geospatial`.

### density

Visual or informational density conditions. Examples include `density:dense`, `density:dense:avoid`, and `density:sparse`.

### group-cardinality

The number of groups or categories a chart needs to compare. Examples include `group-cardinality:many`, `group-cardinality:binary`, and `group-cardinality:few`.

### knowledge

Reader domain knowledge or prior familiarity. Examples include `knowledge:low`, `knowledge:mixed`, and `knowledge:high`.

### lever

The design lever a guideline changes. Examples include `lever:encoding`, `lever:layout-structure`, and `lever:chart-family`.

### literacy

Reader visualization literacy. Examples include `literacy:novice` and `literacy:expert`.

### measure

Measure-count conditions. Examples include `measure:single` and `measure:multi`.

### needs

Reader needs that affect accessibility, language, interaction, or domain understanding. Examples include `needs:color-vision-deficiency`, `needs:low-vision`, and `needs:screen-reader`.

### operator

Analytical operators or comparison tasks supported by a guideline. Examples include `operator:part-whole`, `operator:rank`, and `operator:lookup`.

### polish

Presentation refinements that improve inspection or review. Examples include `polish:annotation`, `polish:declutter`, and `polish:consistency`.

### purpose

Whether the guideline helps select a chart family or refine an already chosen design. Examples include `purpose:select` and `purpose:refine`.

### quality

Design qualities affected by the guideline. Examples include `quality:readability`, `quality:accessibility:use`, and `quality:trust`.

### reading-mode

How readers are expected to inspect the chart. Examples include `reading-mode:exact`, `reading-mode:overview`, and `reading-mode:lookup`.

### scope

The result scope or display scope affected by the guideline. Examples include `scope:single-result`, `scope:record-list`, and `scope:grouped-result`.

### shape

Data-shape conditions that affect chart interpretation. Examples include `shape:outlier-rich` and `shape:skewed`.

### structure

View and layout structures used to organize a chart or set of charts. Examples include `structure:single-view`, `structure:multi-view:use`, and `structure:dashboard:avoid`.

### task

Reader or analysis tasks. Examples include `task:compare`, `task:trend`, and `task:retrieve`.

### temporal-pattern

Temporal dynamics that affect design choice. An example is `temporal-pattern:dynamic`.

### time

Time-related data conditions. Examples include `time:ordered-time`, `time:time-interval`, and `time:non-temporal`.
