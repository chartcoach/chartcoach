import { useId } from "react";
import { Input } from "@chartcoach/ui/components/input";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@chartcoach/ui/components/select";
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

  return (
    <div className="grid min-w-0 gap-1.5">
      <span
        className="font-mono text-[0.72rem] font-bold lowercase tracking-[0.02em] text-muted-foreground"
        id={labelId}
      >
        {label}
      </span>
      <Select onValueChange={onValueChange} value={value}>
        <SelectTrigger
          aria-labelledby={labelId}
          className="w-full justify-between bg-background text-foreground"
        >
          <SelectValue />
        </SelectTrigger>
        <SelectContent align="start" className="min-w-48" portal={false} position="popper">
          <SelectGroup>
            {options.map((option) => {
              const optionValue = toOptionValue(option.value);
              return (
                <SelectItem key={optionValue} value={optionValue}>
                  {option.label}
                </SelectItem>
              );
            })}
          </SelectGroup>
        </SelectContent>
      </Select>
    </div>
  );
}
