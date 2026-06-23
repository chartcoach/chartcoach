"use client";

import { DocsLayout as FumadocsDocsLayout } from "fumadocs-ui/layouts/docs";
import type { DocsLayoutProps } from "fumadocs-ui/layouts/docs";

import { BrandTitleLink } from "@/components/brand-title";

export function DocsLayout({ slots, ...props }: DocsLayoutProps) {
  return (
    <FumadocsDocsLayout
      {...props}
      slots={{
        ...slots,
        navTitle: BrandTitleLink,
      }}
    />
  );
}
