import path from "node:path";

export function outputPathForPathname(distDir: string, pathname: string): string {
  return path.join(distDir, pathname.replace(/^\/+/, ""));
}
