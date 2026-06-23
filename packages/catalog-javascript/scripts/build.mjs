import { rmSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const scriptDir = dirname(fileURLToPath(import.meta.url));
const packageRoot = resolve(scriptDir, "..");

rmSync(resolve(packageRoot, "dist"), { recursive: true, force: true });

run("tsc", ["-b", "tsconfig.build.json", "--force"]);
run("tsc-alias", [
  "-p",
  "tsconfig.build.json",
  "--resolve-full-paths",
  "--resolve-full-extension",
  ".js",
]);

function run(command, args) {
  const result = spawnSync(command, args, {
    cwd: packageRoot,
    stdio: "inherit",
    shell: process.platform === "win32",
  });

  if (result.status !== 0) {
    process.exit(result.status ?? 1);
  }
}
