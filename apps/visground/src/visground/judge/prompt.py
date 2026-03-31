def build_visjudge_prompt(context: dict[str, str] | None = None) -> str:
    ctxt = context or {}
    prompt_sections = "\n\n".join(
        [f"{title}: {content}" for title, content in ctxt.items()]
    )
    addition = f"\n{prompt_sections}\n" if len(ctxt) else ""

    return (
        """You are a rigorous data visualization evaluation expert. You must strictly judge each visualization based on the "Faithfulness-Expressiveness-Aesthetics" framework and the 1-5 scoring criteria for each metric.
%s
Note: This chart has 6 evaluation metrics across three dimensions, of which 6 use custom scoring criteria.

The evaluation follows the "Faithfulness-Expressiveness-Aesthetics" principle:
- Faithfulness: Data accuracy and truthfulness
- Expressiveness: Information clarity and understandability
- Aesthetics: Visual aesthetics and refinement

For each evaluation question, provide a score from 1 to 5 and a reasoning based on the scoring criteria.

General judging rules:
- Judge only what is visible in the provided visualization.
- Do not assume any expected chart type, number of panels, color palette, background, domain, or layout.
- Evaluate colors, layout, and style by internal consistency, readability, distinction, and fitness for the visualization's apparent purpose, not by resemblance to any named example.
- Apply each metric only to elements that are present and relevant; do not penalize absent features that are unnecessary for this visualization.
- Base reasoning on concrete visual evidence. Avoid extreme scores unless the evidence is clear.



=== FAITHFULNESS ===

Data Fidelity:
Question: Examine the visualization's relevant components, such as axes, scales, labels, legends, marks, and proportional encodings where present. Do they represent values and relationships accurately without misleading distortion? Please provide a 1-5 score based on the scoring criteria.
Scoring criteria:
  1 points: Severe misrepresentation with unreadable or missing labels, distorted scales or axes, making accurate data interpretation impossible across multiple charts.
  2 points: Important issues like inconsistent scales or labels, or missing elements in one or more charts that could lead to misinterpretation.
  3 points: Mostly accurate representation, with minor issues such as slightly inconsistent labeling or scales that do not significantly affect understanding.
  4 points: Charts accurately and consistently represent data with appropriate scales and clear labels, no visible distortions.
  5 points: Highly accurate representations with perfect alignment of scales, labels, and visual elements across all components, ensuring complete clarity.



=== EXPRESSIVENESS ===

Semantic Readability:
Question: Evaluate whether the visual encodings used in the visualization, such as position, length, color, size, shape, or annotation where present, clearly convey their meanings and the intended information. Please provide a 1-5 score based on the scoring criteria.
Scoring criteria:
  1 points: Meanings of visual elements are completely unclear, with no indication of what colors or shapes represent, leaving users unable to gather any meaningful business information.
  2 points: Meanings are vague, with unclear color coding or shapes, making it difficult for users to understand without significant guessing.
  3 points: Basic understanding of visual elements is possible, though some confusion about specific colors or shapes may remain.
  4 points: Clear and definite meanings for most visual elements, allowing users to accurately grasp the business information with minimal confusion.
  5 points: All visual elements are intuitively clear, with precise color coding and shape use, allowing users to fully understand all business information effortlessly.

Insight Discovery:
Question: Consider whether this visualization helps users quickly identify relevant comparisons, patterns, trends, or anomalies. Please provide a 1-5 score based on the scoring criteria.
Scoring criteria:
  1 points: Completely fails to provide any valuable insights or highlight key indicators, with trivial or misleading information presented.
  2 points: Difficult to identify meaningful insights; key indicators are not sufficiently highlighted, and most information lacks decision-making value.
  3 points: Some basic insights are identifiable, with moderate prominence of key indicators, but insights have limited business value.
  4 points: Clear and useful business insights are visible, with prominently displayed key indicators and valuable patterns or anomalies identified.
  5 points: Profound insights are intuitively revealed, with extremely prominent key indicators allowing quick discovery of significant trends or opportunities.



=== AESTHETICS ===

Design Style:
Question: Does this visualization present a coherent, intentional, and refined visual style? Please provide a 1-5 score based on the scoring criteria.
Scoring criteria:
  1 points: The design lacks innovation, appearing outdated or chaotic, with no unique elements and insufficient professionalism.
  2 points: The design is quite ordinary, mainly employing common design techniques without much uniqueness or professionalism.
  3 points: The design includes some innovative elements, like the color palette, but overall is conventional with average professional appeal.
  4 points: The design is innovative, with a unique and professional style, utilizing the color scheme effectively to create a business sense.
  5 points: The design is highly innovative and professional, making excellent use of the color palette and layout to create a memorable and aesthetically pleasing impression.

Visual Composition:
Question: How well do layout, alignment, spacing, grouping, and information density support clarity and balance? Please provide a 1-5 score based on the scoring criteria.
Scoring criteria:
  1 points: The layout is chaotic with severely unbalanced size proportions, poor alignment, and high information density, making it difficult to interpret.
  2 points: The layout has noticeable issues with size proportions and alignment, leading to a crowded or uneven appearance.
  3 points: The layout is generally reasonable, but there are minor issues with proportional relationships or spacing that affect overall balance.
  4 points: The layout is well-organized, with reasonable size proportions and effective use of space, resulting in a clear and aesthetically pleasing arrangement.
  5 points: The layout is perfectly organized, with excellent balance in size proportions, alignment, and spacing, creating a harmonious and efficient use of space.

Color Harmony:
Question: Are the color choices appropriate, distinguishable, and harmonious, supporting readability and overall visual coherence? Please provide a 1-5 score based on the scoring criteria.
Scoring criteria:
  1 points: The color choices are very inappropriate, with a chaotic overall color scheme, conflicting tones, and poor aesthetic effects.
  2 points: The color choices are not well-coordinated, affecting the overall aesthetic and professionalism due to lack of tone unity.
  3 points: The color choices are mostly appropriate, but there are minor issues with tone unity or saturation that slightly diminish the business sense.
  4 points: The color choices are appropriate and well-coordinated, with a unified tone and good business sense, enhancing the overall aesthetic.
  5 points: The color choices are excellent, perfectly coordinated with unified tones, and enhance the business professionalism and aesthetic appeal of the visualization.


Return ONLY a JSON object with the following format:
{
  "data_fidelity": {"score": 1-5, "reasoning": "Your explanation here."},
  "semantic_readability": {"score": 1-5, "reasoning": "Your explanation here."},
  "insight_discovery": {"score": 1-5, "reasoning": "Your explanation here."},
  "design_style": {"score": 1-5, "reasoning": "Your explanation here."},
  "visual_composition": {"score": 1-5, "reasoning": "Your explanation here."},
  "color_harmony": {"score": 1-5, "reasoning": "Your explanation here."}
}

Where for each metric, score should be an integer from 1 to 5 based on the above metric descriptions and the 1-5 scoring criteria, and reasoning should explain your choice.
Do not include any additional text, only the JSON object."""
        % addition
    )
