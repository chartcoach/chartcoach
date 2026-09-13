import type { NextConfig } from "next";
import { withEve } from "eve/next";
import { PHASE_DEVELOPMENT_SERVER } from "next/constants";

const config: NextConfig = {
  agentRules: false,
  devIndicators: false,
  images: { unoptimized: true },
};

export default function nextConfig(phase: string) {
  return phase === PHASE_DEVELOPMENT_SERVER
    ? withEve(config)
    : { ...config, output: "export" as const };
}
