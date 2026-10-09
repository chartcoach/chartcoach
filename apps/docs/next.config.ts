import type { NextConfig } from "next";

import { createMDX } from "fumadocs-mdx/next";

const withMDX = createMDX();

const config: NextConfig = {
  allowedDevOrigins: process.env.PORTLESS_URL ? [new URL(process.env.PORTLESS_URL).hostname] : [],
  output: "export",
  reactStrictMode: true,
};

export default withMDX(config);
