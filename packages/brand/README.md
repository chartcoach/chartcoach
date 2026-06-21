# @chartcoach/brand

`@chartcoach/brand` owns the shared chartcoach web identity. It provides the
logo asset paths, public brand files, font imports, CSS tokens, and asset drift
checks used by `apps/site` and `apps/docs`.

Import the shared font face and app tokens from the app entry CSS or layout:

```ts
import "@chartcoach/brand/fonts.css";
import "@chartcoach/brand/tokens.css";
```

Use `brandAssets` for public `/brand/...` paths:

```ts
import { brandAssets } from "@chartcoach/brand";

brandAssets.favicon;
brandAssets.logo;
```

The canonical files live in `assets/brand`. `render:svg` generates square
lockup SVGs from the shared wordmark geometry. `render:png` renders one PNG for
every SVG in `assets/brand`. The web apps still serve copied files from their
own `public/brand` directories so Astro, Next static export, favicons, and
apple touch icons keep predictable public URLs.

Regenerate SVGs, render PNGs, and sync public copies after changing canonical
assets:

```bash
pnpm --dir packages/brand sync:assets
```

Check for stale generated SVGs, stale PNGs, and public-copy drift:

```bash
pnpm --dir packages/brand check:assets
```
