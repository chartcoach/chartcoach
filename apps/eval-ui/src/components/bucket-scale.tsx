import type { ChangeEvent } from "react";

import type { GuidelineRatingBucket } from "@chartcoach/eval-ui/eval/guideline-ratings";
import { cn } from "@chartcoach/eval-ui/lib/utils";

type BucketOption = {
  value: GuidelineRatingBucket;
  label: string;
  shortLabel: string;
};

const defaultOptions: BucketOption[] = [
  { value: "hard_constraint", label: "Hard constraint", shortLabel: "Hard" },
  { value: "soft_constraint", label: "Soft constraint", shortLabel: "Soft" },
  { value: "not_useful", label: "Not useful", shortLabel: "Not useful" },
  { value: "not_applicable", label: "Not applicable", shortLabel: "N/A" },
];

export function BucketScale({
  name,
  value,
  onChange,
  options = defaultOptions,
  ariaLabel = "Bucket",
  disabled = false,
}: {
  name: string;
  value: GuidelineRatingBucket | undefined;
  onChange: (next: GuidelineRatingBucket | undefined) => void;
  options?: BucketOption[];
  ariaLabel?: string;
  disabled?: boolean;
}) {
  const selectedLabel = options.find((o) => o.value === value)?.label;

  function handleChange(event: ChangeEvent<HTMLInputElement>) {
    const next = event.currentTarget.value as GuidelineRatingBucket;
    onChange(next);
  }

  return (
    <fieldset className="flex w-full flex-col gap-1.5" aria-label={ariaLabel}>
      <div className={cn("grid gap-2", "grid-cols-2 sm:grid-cols-4")}>
        {options.map((opt) => (
          <label
            key={opt.value}
            className={cn(disabled ? "cursor-not-allowed opacity-60" : "cursor-pointer")}
            title={opt.label}
          >
            <input
              type="radio"
              name={name}
              value={opt.value}
              checked={opt.value === value}
              disabled={disabled}
              aria-label={opt.label}
              onChange={handleChange}
              onClick={() => {
                if (disabled) return;
                if (opt.value === value) onChange(undefined);
              }}
              className="peer sr-only"
            />
            <span
              className={cn(
                "grid h-10 w-full select-none place-items-center rounded-md border bg-background px-2 text-xs font-medium",
                "peer-checked:border-transparent peer-checked:bg-foreground peer-checked:text-background",
                "peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-ring/60",
              )}
            >
              <span className="truncate">{opt.shortLabel}</span>
            </span>
          </label>
        ))}
      </div>

      <div className="min-h-4 w-full min-w-0 text-center text-xs text-muted-foreground">
        <span className="block truncate">{selectedLabel ?? "Not rated"}</span>
      </div>
    </fieldset>
  );
}

