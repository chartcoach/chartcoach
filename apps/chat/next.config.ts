import type { NextConfig } from "next";
import { withEve } from "eve/next";

const config: NextConfig = {
  agentRules: false,
  devIndicators: false,
  images: {
    qualities: [90],
    remotePatterns: [
      {
        protocol: "https",
        hostname: "chartcoach.dev",
        pathname: "/guidelines/*/og.png",
        search: "",
      },
    ],
  },
};

export default withEve(config);
