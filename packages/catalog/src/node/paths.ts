import { homedir } from "node:os";
import { join, win32 } from "node:path";

/** Per-user roots matching Python PlatformDirs("chartcoach", appauthor=False). */
export function platformDirectories() {
  const home = homedir();

  if (process.platform === "darwin") {
    const data = join(home, "Library", "Application Support", "chartcoach");

    return { data, config: data, cache: join(home, "Library", "Caches", "chartcoach") };
  }

  if (process.platform === "win32") {
    const data = win32.join(
      process.env.LOCALAPPDATA || win32.join(home, "AppData", "Local"),
      "chartcoach",
    );

    return { data, config: data, cache: win32.join(data, "Cache") };
  }

  return {
    data: join(process.env.XDG_DATA_HOME || join(home, ".local", "share"), "chartcoach"),
    config: join(process.env.XDG_CONFIG_HOME || join(home, ".config"), "chartcoach"),
    cache: join(process.env.XDG_CACHE_HOME || join(home, ".cache"), "chartcoach"),
  };
}
