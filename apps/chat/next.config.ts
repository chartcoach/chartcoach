import type { NextConfig } from "next";
import { withEve } from "eve/next";
import { PHASE_DEVELOPMENT_SERVER } from "next/constants.js";

const config: NextConfig = {
  agentRules: false,
  devIndicators: false,
  images: { unoptimized: true },
  poweredByHeader: false,
};

export default function nextConfig(phase: string) {
  return phase === PHASE_DEVELOPMENT_SERVER ? withEve(config) : config;
}
