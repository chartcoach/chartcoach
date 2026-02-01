import type { ChangeEvent } from "react";

type LikertOption = {
  value: number;
  label: string;
};

export function LikertScale({
  name,
  value,
  onChange,
  options,
  ariaLabel,
  disabled = false,
}: {
  name: string;
  value: number | undefined;
  onChange: (next: number | undefined) => void;
  options: LikertOption[];
  ariaLabel: string;
  disabled?: boolean;
}) {
  const selectedLabel = options.find((o) => o.value === value)?.label;
  const minOption = options[0];
  const maxOption = options[options.length - 1];

  function handleChange(event: ChangeEvent<HTMLInputElement>) {
    const next = Number(event.currentTarget.value);
    if (!Number.isFinite(next)) return;
    onChange(next);
  }

  return (
    <fieldset
      className="inline-flex w-60 max-w-full min-w-0 flex-col gap-1.5"
      aria-label={ariaLabel}
    >
      <div
        className="grid w-full overflow-hidden rounded-md border bg-background"
        style={{
          gridTemplateColumns: `repeat(${options.length}, minmax(0, 1fr))`,
        }}
      >
        {options.map((opt) => (
          <label
            key={opt.value}
            className={disabled ? "cursor-not-allowed opacity-60" : "cursor-pointer"}
            title={`${opt.value} — ${opt.label}`}
          >
            <input
              type="radio"
              name={name}
              value={opt.value}
              checked={opt.value === value}
              aria-label={`${opt.value} — ${opt.label}`}
              onChange={handleChange}
              onClick={() => {
                if (disabled) return;
                if (opt.value === value) onChange(undefined);
              }}
              disabled={disabled}
              className="peer sr-only"
            />
            <span className="grid h-10 w-full select-none place-items-center text-xs peer-checked:bg-foreground peer-checked:text-background peer-focus-visible:outline-2 peer-focus-visible:outline-offset-1 peer-focus-visible:outline-ring/60">
              <span className="tabular-nums">{opt.value}</span>
            </span>
          </label>
        ))}
      </div>
      {minOption && maxOption ? (
        <div className="flex w-full min-w-0 justify-between gap-2 text-[11px] text-muted-foreground">
          <span className="truncate">
            <span className="tabular-nums">{minOption.value}</span> = {minOption.label}
          </span>
          <span className="truncate text-right">
            <span className="tabular-nums">{maxOption.value}</span> = {maxOption.label}
          </span>
        </div>
      ) : null}
      <div className="min-h-4 w-full min-w-0 text-center text-xs text-muted-foreground">
        <span className="block truncate">{selectedLabel ?? "Not rated"}</span>
      </div>
    </fieldset>
  );
}
