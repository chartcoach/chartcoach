import { useEffect, useEffectEvent, useState } from "react";
import {
  catalogFiltersSchema,
  type CatalogFilters,
  type CatalogMetadata,
} from "../shared/catalog-filters";
import { useCatalogExplorer } from "./use-catalog-explorer";
import type { CatalogFilterSelection } from "./use-catalog-filters";

export function useFilterDraft({
  value,
  metadata,
  open,
  matchedGuidelines,
  disabled,
  onApply,
  onReload,
  onClose,
}: {
  value: CatalogFilters;
  metadata: CatalogMetadata;
  open: boolean;
  matchedGuidelines: number;
  disabled: boolean;
  onApply: (selection: CatalogFilterSelection) => Promise<void>;
  onReload: () => Promise<void>;
  onClose: () => void;
}) {
  const [draft, setDraft] = useState(value);
  const [applying, setApplying] = useState(false);
  const [applyError, setApplyError] = useState("");

  const begin = useEffectEvent(() => {
    setDraft(value);
    setApplyError("");
  });

  useEffect(() => {
    if (open) begin();
  }, [open]);
  const parsed = catalogFiltersSchema.safeParse(draft);
  const explorer = useCatalogExplorer(metadata, parsed.success ? parsed.data : undefined, open);
  const key = parsed.success ? JSON.stringify(parsed.data) : "";
  const appliedKey = JSON.stringify(catalogFiltersSchema.parse(value));
  const changed = key !== appliedKey;
  const current = explorer.data?.key === key ? explorer.data : undefined;
  const count = explorer.data?.matchedGuidelines ?? matchedGuidelines;
  const error = !parsed.success ? parsed.error.issues[0]?.message : explorer.error;

  async function apply() {
    if (!parsed.success || !current || error || disabled || applying) return;
    setApplying(true);
    setApplyError("");

    try {
      await onApply({
        filters: parsed.data,
        selection: current.selection,
        matchedGuidelines: current.matchedGuidelines,
      });
      onClose();
    } catch {
      setApplyError("Could not apply this selection. Your current review is unchanged.");
    } finally {
      setApplying(false);
    }
  }

  async function reload() {
    if (disabled || applying) return;
    setApplying(true);
    setApplyError("");

    try {
      await onReload();
      onClose();
    } catch {
      setApplyError("Could not reload the catalog. Try again.");
    } finally {
      setApplying(false);
    }
  }

  return {
    draft,
    setDraft,
    count,
    ready: Boolean(current),
    error,
    valid: parsed.success,
    changed,
    applying,
    applyError,
    apply,
    reload,
    retry: explorer.retry,
    explorer,
  };
}
