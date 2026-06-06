# @chartcoach/ui

Shared React UI primitives, design tokens, and style utilities.

The package exports base components and shared style utilities from the package root.

```tsx
import { Button } from "@chartcoach/ui";

export function CatalogButton() {
  return <Button type="button">Browse catalog</Button>;
}
```

Import CSS through `@chartcoach/ui/styles/globals.css`. Do not import component or library internals through package subpaths.

Build it with `pnpm --dir packages/ui build`.

## License

MIT. See [LICENSE](../../LICENSE).
