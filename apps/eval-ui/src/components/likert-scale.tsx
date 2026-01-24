import type { ChangeEvent } from 'react'

type LikertOption = {
  value: number
  label: string
}

const defaultOptions: LikertOption[] = [
  { value: 1, label: 'Irrelevant' },
  { value: 2, label: 'Somewhat relevant' },
  { value: 3, label: 'Relevant' },
  { value: 4, label: 'Very relevant' },
  { value: 5, label: 'Critical' },
]

export function LikertScale({
  name,
  value,
  onChange,
  options = defaultOptions,
  ariaLabel = 'Relevance (1–5)',
}: {
  name: string
  value: number | undefined
  onChange: (next: number) => void
  options?: LikertOption[]
  ariaLabel?: string
}) {
  const selectedLabel = options.find((o) => o.value === value)?.label

  function handleChange(event: ChangeEvent<HTMLInputElement>) {
    const next = Number(event.currentTarget.value)
    if (!Number.isFinite(next)) return
    onChange(next)
  }

  return (
    <fieldset className="min-w-0" aria-label={ariaLabel}>
      <div className="flex flex-col gap-1.5">
        <div className="inline-flex overflow-hidden rounded-md border bg-background">
          {options.map((opt) => (
            <label
              key={opt.value}
              className="cursor-pointer"
              title={`${opt.value} — ${opt.label}`}
            >
              <input
                type="radio"
                name={name}
                value={opt.value}
                checked={opt.value === value}
                onChange={handleChange}
                className="peer sr-only"
              />
              <span className="grid h-11 w-11 select-none place-items-center text-xs peer-checked:bg-foreground peer-checked:text-background peer-focus-visible:outline peer-focus-visible:outline-2 peer-focus-visible:outline-offset-1 peer-focus-visible:outline-ring/60">
                <span className="tabular-nums">{opt.value}</span>
              </span>
            </label>
          ))}
        </div>
        <div className="min-h-4 min-w-0 text-center text-xs text-muted-foreground">
          <span className="block truncate">{selectedLabel ?? 'Not rated'}</span>
        </div>
      </div>
    </fieldset>
  )
}
