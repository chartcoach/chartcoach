export const starters = [
  {
    title: "Review a comparison",
    description: "Check what the bars communicate",
    image: "/examples/bicycle-trips.png",
    prompt:
      "Review this chart. Readers need to compare the total number of bicycle trips across the three cities. What should I keep or improve?",
  },
  {
    title: "Explore a tradeoff",
    description: "Labels, legends, and reading effort",
    image: "/examples/support-requests.png",
    prompt:
      "For this chart, when would direct labels work better than a legend, and when would you keep the legend? Compare the tradeoffs using the guidelines.",
  },
  {
    title: "Choose a chart",
    description: "Turn a data brief into a design",
    image: "/examples/visits-brief.png",
    prompt:
      "I’m designing a static chart for a monthly report. The image contains six months of website visits by acquisition channel. Readers should compare trends and see which channel leads each month. Recommend a chart and the key encoding choices using the guidelines.",
  },
] as const;
