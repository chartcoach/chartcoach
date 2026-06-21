import type { BaseLayoutProps } from "fumadocs-ui/layouts/shared";
import { brandAssets } from "@chartcoach/brand";

import { appName } from "@/lib/shared";

function BrandTitle() {
  return (
    <span className="inline-flex min-w-0 items-center gap-2">
      <span className="chartcoach-brand-logo h-7 w-[6.97rem]" aria-hidden="true">
        <img
          src={brandAssets.logo}
          alt=""
          className="chartcoach-brand-logo__image chartcoach-brand-logo__image--light"
        />
        <img
          src={brandAssets.logoWhite}
          alt=""
          className="chartcoach-brand-logo__image chartcoach-brand-logo__image--dark"
        />
      </span>
      <span className="sr-only">{appName}</span>
      <span className="rounded-full border border-accent/25 px-1.5 py-1 text-[0.625rem] font-semibold leading-none tracking-[0.08em] text-accent uppercase dark:border-accent/35">
        Docs
      </span>
    </span>
  );
}

export function baseOptions(): BaseLayoutProps {
  return {
    nav: {
      title: <BrandTitle />,
    },
  };
}
