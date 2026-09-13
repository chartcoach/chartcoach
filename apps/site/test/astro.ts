import type { AstroIntegration, AstroIntegrationLogger } from "astro";
import { vi } from "vite-plus/test";

export function createTestLogger() {
  const info = vi.fn<(message: string) => void>();
  const warn = vi.fn<(message: string) => void>();
  const error = vi.fn<(message: string) => void>();
  const debug = vi.fn<(message: string) => void>();
  const flush = vi.fn<() => void>();
  const close = vi.fn<() => void>();

  const options = {
    destination: { write: vi.fn() },
    level: "info",
  } as const;

  function create(label: string): AstroIntegrationLogger {
    return {
      options,
      label,
      fork: create,
      info,
      warn,
      error,
      debug,
      flush,
      close,
    };
  }

  return { close, debug, error, flush, info, logger: create("test"), warn };
}

export function requireIntegrationHook<Hook extends keyof AstroIntegration["hooks"]>(
  integration: AstroIntegration,
  name: Hook,
): NonNullable<AstroIntegration["hooks"][Hook]> {
  const hook = integration.hooks[name];

  if (!hook) throw new Error(`Missing ${name} hook.`);

  return hook;
}
