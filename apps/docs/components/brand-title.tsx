import logo from "@chartcoach/brand/assets/brand/chartcoach-horizontal.svg";
import logoWhite from "@chartcoach/brand/assets/brand/chartcoach-horizontal-white.svg";
import Image from "next/image";
import type { ComponentProps } from "react";

import { appName, siteOrigin } from "@/lib/shared";

export function BrandTitle() {
  return (
    <span className="inline-flex min-w-0 items-center">
      <span className="chartcoach-brand-logo h-7 w-[6.97rem]" aria-hidden="true">
        <Image
          src={logo}
          alt=""
          width={112}
          height={28}
          className="chartcoach-brand-logo__image chartcoach-brand-logo__image--light"
          unoptimized
        />
        <Image
          src={logoWhite}
          alt=""
          width={112}
          height={28}
          className="chartcoach-brand-logo__image chartcoach-brand-logo__image--dark"
          unoptimized
        />
      </span>
      <span className="sr-only">{appName}</span>
    </span>
  );
}

export function BrandTitleLink({
  href: _href,
  rel: _rel,
  target: _target,
  ...props
}: ComponentProps<"a">) {
  return (
    <a href={siteOrigin} {...props}>
      <BrandTitle />
    </a>
  );
}
