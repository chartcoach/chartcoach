import { resolve } from "node:path";
import { readFile } from "node:fs/promises";
import { defineEval } from "eve/evals";
import { satisfies } from "eve/evals/expect";
import { assertGrounding } from "./assert-grounding";

export default defineEval({
  async test(t) {
    const image = resolve("evals/fixtures/chart.png");
    const data = (await readFile(image)).toString("base64");

    const turn = await t.send([
      {
        type: "text",
        text: "Review this chart using applicable guidelines. Anchor the observations in the visible title and the largest category's name and value.",
      },
      {
        type: "file",
        data: `data:image/png;base64,${data}`,
        mediaType: "image/png",
        filename: "chart.png",
      },
    ]);

    const answer = assertGrounding(
      t,
      turn,
      "The user supplied a chart image and asked for applicable guideline feedback. Image observations have separate fixture checks. Judge whether each stated context and action meet the cited guideline's conditions, taking the context as given for this grounding check.",
    );

    const observations = answer.points.map((item) => item.context).join(" ");
    t.check(
      observations,
      satisfies<string>((text) => /Orchard harvest/i.test(text), "observes the chart title"),
    );
    t.check(
      observations,
      satisfies<string>(
        (text) => /Pears[\s\S]{0,60}26/i.test(text),
        "observes the largest category and value",
      ),
    );
  },
});
