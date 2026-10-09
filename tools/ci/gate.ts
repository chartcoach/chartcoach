const input = process.env.NEEDS;

if (!input) throw new Error("Missing job results");

// SAFETY: the workflow passes GitHub job results and their string-valued outputs.
const needs = JSON.parse(input) as Record<
  string,
  { result?: string; outputs?: Record<string, string> }
>;

const selection = needs.changes?.outputs;

if (!selection) throw new Error("Missing check selection");

for (const name of ["quality", "javascript", "npm", "python"]) {
  if (selection[name] !== "true" && selection[name] !== "false") {
    throw new Error(`Missing or invalid check selection: ${name}`);
  }
}

const required = {
  changes: true,
  quality: selection.quality === "true",
  javascript: selection.javascript === "true",
  "npm-consumers": selection.npm === "true",
  python: selection.python === "true",
  "python-minimum": selection.python === "true",
};

for (const [job, selected] of Object.entries(required)) {
  const result = needs[job]?.result;

  if (result === "success" || (!selected && result === "skipped")) continue;
  throw new Error(`${job}: ${result}, expected ${selected ? "success" : "success or skipped"}`);
}
