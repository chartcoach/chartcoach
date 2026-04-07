import { useId, type MouseEvent, type PointerEvent } from "react";
import { Input } from "@chartcoach/ui/components/input";
import type { ViewerOption } from "../contract/types";
import { toOptionValue } from "./utils";

export function ViewerSearchField({
  label,
  onChange,
  placeholder,
  value,
}: {
  label: string;
  onChange: (value: string) => void;
  placeholder: string;
  value: string;
}) {
  const inputId = useId();

  return (
    <label className="grid min-w-0 gap-1.5" htmlFor={inputId}>
      <span className="font-mono text-[0.72rem] font-bold lowercase tracking-[0.02em] text-muted-foreground">
        {label}
      </span>
      <Input
        className="w-full bg-background text-foreground"
        id={inputId}
        onChange={(event) => onChange(event.target.value)}
        placeholder={placeholder}
        type="search"
        value={value}
      />
    </label>
  );
}

export function ViewerSelectField({
  label,
  onValueChange,
  options,
  value,
}: {
  label: string;
  onValueChange: (value: string) => void;
  options: ViewerOption[];
  value: string;
}) {
  const labelId = useId();
  const stopPropagation = (
    event:
      | MouseEvent<HTMLButtonElement | HTMLDivElement | HTMLSelectElement>
      | PointerEvent<HTMLButtonElement | HTMLDivElement | HTMLSelectElement>,
  ) => {
    event.stopPropagation();
  };

  return (
    <div className="grid min-w-0 gap-1.5">
      <span
        className="font-mono text-[0.72rem] font-bold lowercase tracking-[0.02em] text-muted-foreground"
        id={labelId}
      >
        {label}
      </span>
      <select
        aria-labelledby={labelId}
        className="h-8 w-full rounded-[4px] border border-input bg-background px-2.5 text-sm text-foreground outline-none transition-colors focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50"
        onChange={(event) => onValueChange(event.target.value)}
        onClick={stopPropagation}
        onMouseDown={stopPropagation}
        onPointerDown={stopPropagation}
        value={value}
      >
        {options.map((option) => {
          const optionValue = toOptionValue(option.value);
          return (
            <option key={optionValue} value={optionValue}>
              {option.label}
            </option>
          );
        })}
      </select>
    </div>
  );
}
