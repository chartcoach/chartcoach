# @chartcoach/ui

Shared React UI primitives, design tokens, and ChartCoach brand assets.

The package exports base components, ChartCoach brand marks, and shared style utilities for the site.

```tsx
import { Button, ChartCoachMarimekkoMark } from "@chartcoach/ui";

export function CatalogButton() {
  return (
    <Button type="button">
      <ChartCoachMarimekkoMark style={{ width: 18 }} />
      Browse catalog
    </Button>
  );
}
```

Build it with `pnpm --dir packages/ui build`.

## License

MIT. See [LICENSE](../../LICENSE).
