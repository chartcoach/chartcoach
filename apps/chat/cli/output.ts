import { chalkStderr, type ChalkInstance } from "chalk";

const accent = "#e0364b";

export type StartupDetails = {
  url: string;
  catalog: { guidelines: number; digest: string };
  model?: string;
  dataDir: string;
};

export function renderLoading(chalk: ChalkInstance = chalkStderr) {
  return `${chalk.hex(accent)("◌")} ${chalk.dim("Loading catalog…")}\n`;
}

export function renderStopping(chalk: ChalkInstance = chalkStderr) {
  return `\n${chalk.yellow("◌")} Stopping ChartCoach…\n`;
}

export function renderStopped(chalk: ChalkInstance = chalkStderr) {
  return `${chalk.green("✓")} ChartCoach stopped.\n`;
}

export function renderReady(
  { url, catalog, model, dataDir }: StartupDetails,
  chalk: ChalkInstance = chalkStderr,
) {
  const row = (label: string, value: string) => `  ${chalk.dim(label.padEnd(9))}${value}`;

  return [
    "",
    `${chalk.green("✓")} ${chalk.bold("ChartCoach")} ${chalk.green("is ready")}`,
    `  ${chalk.hex(accent)("➜")} ${chalk.cyan.underline(url)}`,
    "",
    row("Catalog", `${chalk.bold(catalog.guidelines)} guidelines`),
    row("Release", chalk.dim(catalog.digest)),
    row("Model", model ?? "Choose a connection in the browser"),
    row("Data", dataDir),
    "",
    `  ${chalk.dim("Press")} ${chalk.bold("Ctrl+C")} ${chalk.dim("to stop.")}`,
    "",
  ].join("\n");
}
