import { afterEach, expect, it, vi } from "vite-plus/test";
import { platformDirectories } from "../src/node/paths";
import { homedir } from "node:os";

const home = homedir();

afterEach(() => vi.unstubAllGlobals());

it.each([
  {
    platform: "darwin",
    env: {},
    expected: {
      data: `${home}/Library/Application Support/chartcoach`,
      config: `${home}/Library/Application Support/chartcoach`,
      cache: `${home}/Library/Caches/chartcoach`,
    },
  },
  {
    platform: "linux",
    env: {},
    expected: {
      data: `${home}/.local/share/chartcoach`,
      config: `${home}/.config/chartcoach`,
      cache: `${home}/.cache/chartcoach`,
    },
  },
  {
    platform: "linux",
    env: { XDG_DATA_HOME: "/data", XDG_CONFIG_HOME: "/config", XDG_CACHE_HOME: "/cache" },
    expected: {
      data: "/data/chartcoach",
      config: "/config/chartcoach",
      cache: "/cache/chartcoach",
    },
  },
  {
    platform: "win32",
    env: { LOCALAPPDATA: "C:\\Users\\test\\AppData\\Local" },
    expected: {
      data: "C:\\Users\\test\\AppData\\Local\\chartcoach",
      config: "C:\\Users\\test\\AppData\\Local\\chartcoach",
      cache: "C:\\Users\\test\\AppData\\Local\\chartcoach\\Cache",
    },
  },
])("uses native $platform application roots", ({ platform, env, expected }) => {
  vi.stubGlobal("process", { ...process, platform, env });
  expect(platformDirectories()).toEqual(expected);
});
