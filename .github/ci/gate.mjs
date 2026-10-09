const needs = JSON.parse(process.env.NEEDS);

const selection = needs.changes.outputs;

for (const name of ["quality", "javascript", "npm", "python"]) {
  if (!["true", "false"].includes(selection[name])) {
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
