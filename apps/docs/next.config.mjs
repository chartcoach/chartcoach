import { createMDX } from "fumadocs-mdx/next";

const withMDX = createMDX();

/** @type {import("next").NextConfig} */
const config = {
  allowedDevOrigins: process.env.PORTLESS_URL ? [new URL(process.env.PORTLESS_URL).hostname] : [],
  output: "export",
  reactStrictMode: true,
};

export default withMDX(config);
