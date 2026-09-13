import type { MetadataRoute } from "next";

import { isPreviewDeployment } from "@/lib/shared";

export const dynamic = "force-static";

export const revalidate = false;

export default function robots(): MetadataRoute.Robots {
  if (isPreviewDeployment()) {
    return {
      rules: {
        userAgent: "*",
        disallow: "/",
      },
    };
  }

  return {
    rules: {
      userAgent: "*",
      allow: "/",
    },
  };
}
