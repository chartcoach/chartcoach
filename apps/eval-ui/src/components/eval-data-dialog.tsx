import { Download, HardDriveDownload, Trash2, Upload, X } from "lucide-react";
import { useEffect, useMemo, useRef, useState } from "react";

import {
  clearGuidelineRatings,
  clearSetRatings,
  mergeGuidelineRatings,
  mergeSetRatings,
} from "@chartcoach/eval-ui/db-collections";
import type { GuidelineRating, ScenarioSetRating } from "@chartcoach/eval-ui/db-collections";
import { EvalDataExportV1Schema } from "@chartcoach/eval-ui/eval/eval-data";
import {
  SYNC_LAST_SIGNATURE_STORAGE_KEY,
  SYNC_LAST_SUCCESS_AT_STORAGE_KEY,
  SYNC_LAST_SUCCESS_KEY_STORAGE_KEY,
  removeLocalStorageItem,
} from "@chartcoach/eval-ui/eval/eval-data-sync-metadata";
import { GuidelineRatingsExportV2Schema } from "@chartcoach/eval-ui/eval/guideline-ratings";
import { SetRatingsExportV1Schema } from "@chartcoach/eval-ui/eval/set-ratings";
import { downloadEvalDataExport } from "@chartcoach/eval-ui/lib/export-eval-data";
import { getDeviceId } from "@chartcoach/eval-ui/lib/eval-utils";

type SyncState = {
  status: "idle" | "queued" | "syncing" | "synced" | "error" | "disabled";
  lastSuccessAt: string | null;
  lastSuccessKey: string | null;
};

type PullState = {
  status: "idle" | "pulling" | "synced" | "error" | "disabled";
  exportedAt: string | null;
  key: string | null;
  source: "eval-data" | "legacy-guideline-ratings" | null;
};

function canonicalErrorMessage(error: unknown) {
  if (error instanceof Error) return error.message;
  return "Something went wrong.";
}

export function EvalDataDialog({
  guidelineRatings,
  setRatings,
  sync,
  pull,
}: {
  guidelineRatings: GuidelineRating[];
  setRatings: ScenarioSetRating[];
  sync: SyncState;
  pull: PullState;
}) {
  const deviceId = useMemo(() => getDeviceId(), []);
  const [open, setOpen] = useState(false);
  const closeButtonRef = useRef<HTMLButtonElement | null>(null);
  const importInputRef = useRef<HTMLInputElement | null>(null);

  const [importNotice, setImportNotice] = useState<string | null>(null);
  const [importError, setImportError] = useState<string | null>(null);

  const [clearGuidelines, setClearGuidelines] = useState(true);
  const [clearSets, setClearSets] = useState(true);
  const [clearConfirm, setClearConfirm] = useState("");

  useEffect(() => {
    if (!open) return;
    setImportNotice(null);
    setImportError(null);
    setClearConfirm("");
    setClearGuidelines(true);
    setClearSets(true);
    closeButtonRef.current?.focus();
  }, [open]);

  useEffect(() => {
    if (!open) return;
    const onKeyDown = (event: KeyboardEvent) => {
      if (event.key !== "Escape") return;
      event.preventDefault();
      setOpen(false);
    };
    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [open]);

  async function handleImportFromFile(file: File) {
    setImportNotice(null);
    setImportError(null);

    try {
      const raw = await file.text();
      const doc = JSON.parse(raw) as unknown;

      const combined = EvalDataExportV1Schema.safeParse(doc);
      if (combined.success) {
        const gCount = combined.data.guidelineRatings.ratings.length;
        const sCount = combined.data.setRatings.ratings.length;
        mergeGuidelineRatings(combined.data.guidelineRatings.ratings);
        mergeSetRatings(combined.data.setRatings.ratings);
        setImportNotice(`Imported ${gCount} guideline ratings and ${sCount} set ratings.`);
        return;
      }

      const guidelinesOnly = GuidelineRatingsExportV2Schema.safeParse(doc);
      if (guidelinesOnly.success) {
        mergeGuidelineRatings(guidelinesOnly.data.ratings);
        setImportNotice(`Imported ${guidelinesOnly.data.ratings.length} guideline ratings.`);
        return;
      }

      const setsOnly = SetRatingsExportV1Schema.safeParse(doc);
      if (setsOnly.success) {
        mergeSetRatings(setsOnly.data.ratings);
        setImportNotice(`Imported ${setsOnly.data.ratings.length} set ratings.`);
        return;
      }

      setImportError("Unrecognized file format.");
    } catch (error) {
      setImportError(canonicalErrorMessage(error));
    }
  }

  function clearSyncMetadata() {
    // Clears the local "already synced" marker so the next upload is unambiguous.
    removeLocalStorageItem(SYNC_LAST_SIGNATURE_STORAGE_KEY);
    removeLocalStorageItem(SYNC_LAST_SUCCESS_AT_STORAGE_KEY);
    removeLocalStorageItem(SYNC_LAST_SUCCESS_KEY_STORAGE_KEY);
  }

  const guidelineCount = guidelineRatings.length;
  const setCount = setRatings.length;

  const hasAny = guidelineCount > 0 || setCount > 0;
  const canClear = (clearGuidelines || clearSets) && clearConfirm === "CLEAR";

  return (
    <>
      <button
        type="button"
        onClick={() => setOpen(true)}
        className="inline-flex h-8 items-center gap-2 rounded-md border bg-background px-3 text-xs text-foreground shadow-sm hover:bg-muted focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
        aria-haspopup="dialog"
        aria-expanded={open}
      >
        <HardDriveDownload className="size-4 text-muted-foreground" aria-hidden="true" />
        <span>Data</span>
      </button>

      {open ? (
        <div
          className="fixed inset-0 z-[60] flex items-start justify-center bg-background/75 px-4 py-10 backdrop-blur-sm"
          onMouseDown={(event) => {
            if (event.target !== event.currentTarget) return;
            setOpen(false);
          }}
          role="presentation"
        >
          <section
            role="dialog"
            aria-modal="true"
            aria-labelledby="eval-data-dialog-title"
            className="w-full max-w-xl rounded-xl border bg-card shadow-xl"
          >
            <header className="flex items-start justify-between gap-3 border-b px-5 py-4">
              <div className="min-w-0">
                <h2 id="eval-data-dialog-title" className="text-base font-semibold">
                  Data & sync
                </h2>
                <p className="mt-1 text-sm text-muted-foreground">
                  Ratings are stored locally and synced to the study bucket when online.
                </p>
              </div>

              <button
                ref={closeButtonRef}
                type="button"
                onClick={() => setOpen(false)}
                className="inline-flex h-8 items-center justify-center rounded-md border bg-background px-2 text-xs text-muted-foreground hover:bg-muted focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
                aria-label="Close"
              >
                <X className="size-4" aria-hidden="true" />
              </button>
            </header>

            <div className="space-y-6 px-5 py-5">
              <section className="space-y-2">
                <div className="flex flex-wrap items-center justify-between gap-2">
                  <div className="text-sm font-semibold">Status</div>
                  <div className="text-xs text-muted-foreground">
                    Device:{" "}
                    <button
                      type="button"
                      className="rounded-sm underline-offset-2 hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
                      onClick={() => {
                        const promise = navigator.clipboard?.writeText(deviceId);
                        if (!promise) {
                          setImportError("Clipboard API not available.");
                          return;
                        }
                        void promise.then(
                          () => setImportNotice("Copied device id."),
                          () => setImportError("Failed to copy device id."),
                        );
                      }}
                      title="Copy device id"
                    >
                      {deviceId}
                    </button>
                  </div>
                </div>

                <div className="grid gap-3 rounded-lg border bg-background p-3 sm:grid-cols-2">
                  <div>
                    <div className="text-xs font-semibold text-muted-foreground">Local</div>
                    <div className="mt-1 text-sm tabular-nums">
                      {guidelineCount} guideline · {setCount} set
                    </div>
                  </div>
                  <div>
                    <div className="text-xs font-semibold text-muted-foreground">Cloud sync</div>
                    <div className="mt-1 text-sm">
                      <span className="font-medium">
                        {pull.status === "disabled" || sync.status === "disabled"
                          ? "Disabled"
                          : pull.status === "error" || sync.status === "error"
                            ? "Error"
                            : pull.status === "pulling"
                              ? "Fetching"
                              : sync.status === "syncing"
                                ? "Uploading"
                                : sync.status === "queued"
                                  ? "Queued"
                                  : "OK"}
                      </span>
                      <span className="ml-2 text-xs text-muted-foreground">
                        {sync.lastSuccessAt
                          ? `Last upload: ${sync.lastSuccessAt}`
                          : pull.exportedAt
                            ? `Last remote: ${pull.exportedAt}`
                            : null}
                      </span>
                    </div>
                    {sync.lastSuccessKey || pull.key ? (
                      <div className="mt-1 truncate text-xs text-muted-foreground">
                        Key: {sync.lastSuccessKey ?? pull.key}
                        {pull.source === "legacy-guideline-ratings" ? " (legacy)" : null}
                      </div>
                    ) : null}
                  </div>
                </div>
              </section>

              <section className="space-y-2">
                <div className="text-sm font-semibold">Export / import</div>
                <div className="rounded-lg border bg-background p-3">
                  <div className="flex flex-wrap items-center gap-2">
                    <button
                      type="button"
                      onClick={() => downloadEvalDataExport(guidelineRatings, setRatings)}
                      className="inline-flex h-8 items-center gap-2 rounded-md border bg-background px-3 text-xs text-foreground shadow-sm hover:bg-muted focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
                      title="Download all ratings as JSON"
                    >
                      <Download className="size-4 text-muted-foreground" aria-hidden="true" />
                      <span>Download JSON</span>
                    </button>

                    <input
                      ref={importInputRef}
                      type="file"
                      accept="application/json"
                      className="sr-only"
                      onChange={(event) => {
                        const file = event.currentTarget.files?.[0];
                        if (!file) return;
                        event.currentTarget.value = "";
                        void handleImportFromFile(file);
                      }}
                    />

                    <button
                      type="button"
                      onClick={() => importInputRef.current?.click()}
                      className="inline-flex h-8 items-center gap-2 rounded-md border bg-background px-3 text-xs text-foreground shadow-sm hover:bg-muted focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
                      title="Import ratings from JSON (combined or legacy exports)"
                    >
                      <Upload className="size-4 text-muted-foreground" aria-hidden="true" />
                      <span>Import JSON…</span>
                    </button>
                  </div>

                  {importNotice ? (
                    <div className="mt-2 text-xs text-emerald-600">{importNotice}</div>
                  ) : null}
                  {importError ? (
                    <div className="mt-2 text-xs text-red-600">{importError}</div>
                  ) : null}
                </div>
              </section>

              <section className="space-y-2">
                <div className="text-sm font-semibold text-red-600">Danger zone</div>
                <div className="rounded-lg border border-red-200 bg-background p-3 dark:border-red-900/60">
                  <div className="text-sm font-medium">Clear local data (this device)</div>
                  <p className="mt-1 text-xs text-muted-foreground">
                    This only deletes local browser data. If cloud sync is enabled, ratings may
                    re-appear after refresh when restored from the bucket.
                  </p>

                  <div className="mt-3 grid gap-2 sm:grid-cols-2">
                    <label className="flex items-center gap-2 text-xs">
                      <input
                        type="checkbox"
                        className="size-4 accent-foreground"
                        checked={clearGuidelines}
                        onChange={(e) => setClearGuidelines(e.currentTarget.checked)}
                        disabled={!hasAny}
                      />
                      <span>Guideline ratings ({guidelineCount})</span>
                    </label>
                    <label className="flex items-center gap-2 text-xs">
                      <input
                        type="checkbox"
                        className="size-4 accent-foreground"
                        checked={clearSets}
                        onChange={(e) => setClearSets(e.currentTarget.checked)}
                        disabled={!hasAny}
                      />
                      <span>Set ratings ({setCount})</span>
                    </label>
                  </div>

                  <div className="mt-3 grid gap-2 sm:grid-cols-[1fr_auto] sm:items-end">
                    <label className="block text-xs text-muted-foreground">
                      Type <span className="font-semibold text-foreground">CLEAR</span> to confirm
                      <input
                        value={clearConfirm}
                        onChange={(e) => setClearConfirm(e.currentTarget.value)}
                        placeholder="CLEAR"
                        className="mt-1 h-8 w-full rounded-md border bg-background px-2 text-xs text-foreground placeholder:text-muted-foreground/70"
                        aria-label="Type CLEAR to confirm"
                        disabled={!hasAny}
                      />
                    </label>

                    <button
                      type="button"
                      onClick={() => {
                        if (!canClear) return;
                        if (clearGuidelines) clearGuidelineRatings();
                        if (clearSets) clearSetRatings();
                        clearSyncMetadata();
                        setOpen(false);
                      }}
                      className="inline-flex h-8 items-center gap-2 rounded-md border border-red-300 bg-red-50 px-3 text-xs font-medium text-red-700 shadow-sm hover:bg-red-100 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60 disabled:cursor-not-allowed disabled:opacity-60 dark:border-red-900/60 dark:bg-red-950/40 dark:text-red-200 dark:hover:bg-red-950/60"
                      disabled={!canClear}
                    >
                      <Trash2 className="size-4" aria-hidden="true" />
                      <span>Clear</span>
                    </button>
                  </div>
                </div>
              </section>
            </div>
          </section>
        </div>
      ) : null}
    </>
  );
}
