import { brandAssets } from "@chartcoach/brand";
import Image from "next/image";

import { appName } from "@/lib/shared";

export function BrandTitle() {
  return (
    <span className="inline-flex min-w-0 items-center">
      <span className="chartcoach-brand-logo h-7 w-[6.97rem]" aria-hidden="true">
        <Image
          src={brandAssets.logo}
          alt=""
          width={112}
          height={28}
          className="chartcoach-brand-logo__image chartcoach-brand-logo__image--light"
          unoptimized
        />
        <Image
          src={brandAssets.logoWhite}
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
