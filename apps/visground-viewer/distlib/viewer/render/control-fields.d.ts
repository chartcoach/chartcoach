import type { ViewerOption } from "../contract/types";
export declare function ViewerSearchField({
  label,
  onChange,
  placeholder,
  value,
}: {
  label: string;
  onChange: (value: string) => void;
  placeholder: string;
  value: string;
}): import("react/jsx-runtime").JSX.Element;
export declare function ViewerSelectField({
  label,
  onValueChange,
  options,
  value,
}: {
  label: string;
  onValueChange: (value: string) => void;
  options: ViewerOption[];
  value: string;
}): import("react/jsx-runtime").JSX.Element;
//# sourceMappingURL=control-fields.d.ts.map
