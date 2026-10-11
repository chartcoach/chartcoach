import type { BaseLayoutProps } from "fumadocs-ui/layouts/shared";

import { gitConfig, siteOrigin } from "@/lib/shared";

export function baseOptions(): BaseLayoutProps {
  return {
    githubUrl: `https://github.com/${gitConfig.user}/${gitConfig.repo}`,
    nav: {
      url: siteOrigin,
    },
  };
}
