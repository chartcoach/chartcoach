import type { BaseLayoutProps } from "fumadocs-ui/layouts/shared";

import { BrandTitle } from "@/components/brand-title";
import { siteOrigin } from "@/lib/shared";

export function baseOptions(): BaseLayoutProps {
  return {
    nav: {
      title: <BrandTitle />,
      url: siteOrigin,
    },
  };
}
