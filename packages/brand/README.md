# @chartcoach/brand

`@chartcoach/brand` provides the logo files, Poppins imports, CSS color tokens,
and shared logo styles used by the chartcoach web apps.

Import the font faces from the app layout:

```ts
import "@chartcoach/brand/fonts.css";
```

Import the tokens and logo styles from the app stylesheet:

```css
@import "@chartcoach/brand/tokens.css";
@import "@chartcoach/brand/logo.css";
```

Astro reads the emitted asset URL from `src`:

```astro
---
import logo from "@chartcoach/brand/assets/brand/chartcoach-horizontal.svg";
---

<img src={logo.src} alt="chartcoach" />
```

Next passes the same static import to `next/image`:

```tsx
import logo from "@chartcoach/brand/assets/brand/chartcoach-horizontal.svg";
import Image from "next/image";

export function Logo() {
  return <Image src={logo} alt="chartcoach" />;
}
```

Edit the reviewed SVG, PNG, and CSS sources in this package. The site and docs
builds emit the files they import.
