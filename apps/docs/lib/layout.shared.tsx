import type { BaseLayoutProps } from "fumadocs-ui/layouts/shared";

import { siteOrigin } from "@/lib/shared";

export function baseOptions(): BaseLayoutProps {
  return {
    nav: {
      url: siteOrigin,
    },
  };
}
