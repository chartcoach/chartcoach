# @chartcoach/brand

`@chartcoach/brand` is the private workspace package for the chartcoach site
and docs. It owns the Poppins font imports, shared CSS variables, light and dark
logo styles, and logo and icon files.

## Load the shared styles

Load Poppins once from the app layout:

```ts
import "@chartcoach/brand/fonts.css";
```

Import the theme variables and logo classes from the global stylesheet:

```css
@import "@chartcoach/brand/tokens.css";
@import "@chartcoach/brand/logo.css";
```

`fonts.css` loads Poppins weights 400, 500, and 600. `tokens.css` defines the
shared colors, fonts, and content widths. `logo.css` switches paired light and
dark images when the document has the `.dark` class.

## Import an image

[`assets/brand`](assets/brand/) contains horizontal and vertical lockups, a
square logo, favicons, and the app icon. The transparent vertical lockups in
the root README use `chartcoach-vertical.svg` on light backgrounds and
`chartcoach-vertical-white.svg` on dark backgrounds.

In Astro, read the imported asset URL from `logo.src`:

```astro
---
import logo from "@chartcoach/brand/assets/brand/chartcoach-horizontal.svg";
---

<img src={logo.src} alt="chartcoach" />
```

In Next.js, pass the imported asset to `next/image`:

```tsx
import logo from "@chartcoach/brand/assets/brand/chartcoach-horizontal.svg";
import Image from "next/image";

export function Logo() {
  return <Image src={logo} alt="chartcoach" />;
}
```

Change the fonts, CSS, or files under `assets/brand/` in this package. The site
and docs consume them through `@chartcoach/brand` imports.
