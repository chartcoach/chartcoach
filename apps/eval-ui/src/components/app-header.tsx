import { Link } from "@tanstack/react-router";
import { useLiveQuery } from "@tanstack/react-db";
import { useIsFetching } from "@tanstack/react-query";
import { Download, RefreshCw, Trash2, Upload } from "lucide-react";
import { useLayoutEffect, useRef } from "react";

import {
  clearGuidelineRatings,
  guidelineRatingsCollection,
  mergeGuidelineRatings,
  clearSetRatings,
  mergeSetRatings,
  setRatingsCollection,
} from "@chartcoach/eval-ui/db-collections";
import type { GuidelineRating } from "@chartcoach/eval-ui/db-collections";
import type { ScenarioSetRating } from "@chartcoach/eval-ui/db-collections";
import { useAutoUploadGuidelineRatings } from "@chartcoach/eval-ui/eval/hooks/use-auto-upload-guideline-ratings";
import { usePullGuidelineRatingsFromS3 } from "@chartcoach/eval-ui/eval/hooks/use-pull-guideline-ratings";
import { GuidelineRatingsExportV2Schema } from "@chartcoach/eval-ui/eval/guideline-ratings";
import { SetRatingsExportV1Schema } from "@chartcoach/eval-ui/eval/set-ratings";
import { ThemeSelector } from "@chartcoach/eval-ui/components/theme-selector";
import { downloadGuidelineRatingsExport } from "@chartcoach/eval-ui/lib/export-guideline-ratings";
import { downloadSetRatingsExport } from "@chartcoach/eval-ui/lib/export-set-ratings";
import { useOnlineStatus } from "@chartcoach/eval-ui/lib/eval-utils";

export function AppHeader() {
  const headerRef = useRef<HTMLElement | null>(null);
  const importInputRef = useRef<HTMLInputElement | null>(null);
  const setImportInputRef = useRef<HTMLInputElement | null>(null);

  useLayoutEffect(() => {
    const el = headerRef.current;
    if (!el) return;

    const root = document.documentElement;
    const update = () => {
      root.style.setProperty("--app-header-height", `${el.offsetHeight}px`);
    };

    update();

    if (typeof ResizeObserver === "undefined") return;
    const observer = new ResizeObserver(update);
    observer.observe(el);
    return () => observer.disconnect();
  }, []);

  const isOnline = useOnlineStatus();
  const isFetchingCount = useIsFetching();

  const { data } = useLiveQuery(
    (q) =>
      q.from({ rating: guidelineRatingsCollection }).select(({ rating }) => ({
        ...rating,
      })),
    [],
  );

  const ratings = (data ?? []) as GuidelineRating[];
  const ratingCount = ratings.length;

  const { data: setData } = useLiveQuery(
    (q) =>
      q.from({ rating: setRatingsCollection }).select(({ rating }) => ({
        ...rating,
      })),
    [],
  );

  const setRatings = (setData ?? []) as ScenarioSetRating[];

  const sync = useAutoUploadGuidelineRatings(ratings);
  const pull = usePullGuidelineRatingsFromS3();

  type PullStatus = (typeof pull)["status"];
  type SyncStatus = (typeof sync)["status"];

  const pullStatusLabel: Partial<Record<PullStatus, string>> = {
    pulling: "Fetching remote",
    error: "Remote fetch failed",
    disabled: "Remote fetch disabled",
  };

  const syncStatusLabel: Partial<Record<SyncStatus, string>> = {
    syncing: "Uploading",
    queued: "Upload queued",
    error: "Upload failed",
    disabled: "Upload disabled",
    synced: "Upload synced",
  };

  const isPresent = <T,>(value: T | null | undefined | false): value is T => Boolean(value);
  const syncLabel = [
    pullStatusLabel[pull.status] ?? null,
    syncStatusLabel[sync.status] ?? null,
    ratingCount === 0 ? "No ratings yet" : null,
  ]
    .filter(isPresent)
    .join(" · ");

  const hasError = sync.status === "error" || pull.status === "error";
  const isBusy =
    sync.status === "syncing" ||
    sync.status === "queued" ||
    pull.status === "pulling" ||
    isFetchingCount > 0;

  let syncDotClass = "bg-muted-foreground/40";
  if (sync.status === "synced" || pull.status === "synced") syncDotClass = "bg-emerald-500";
  if (isBusy) syncDotClass = "bg-amber-500";
  if (hasError) syncDotClass = "bg-red-500";

  const lastAt = sync.lastSuccessAt ?? pull.exportedAt;
  const lastKey = sync.lastSuccessKey ?? pull.key;

  const syncTitleParts = [
    syncLabel,
    !isOnline ? "Offline" : null,
    lastAt ? `Last: ${lastAt}` : null,
    lastKey ? `Key: ${lastKey}` : null,
  ].filter(Boolean);
  const syncTitle = syncTitleParts.join(" · ");

  async function handleImportFromFile(file: File) {
    const raw = await file.text();
    const parsed = GuidelineRatingsExportV2Schema.parse(JSON.parse(raw));
    mergeGuidelineRatings(parsed.ratings);
    console.info(`[eval-ui] Imported ${parsed.ratings.length} guideline ratings.`);
  }

  async function handleImportSetRatingsFromFile(file: File) {
    const raw = await file.text();
    const parsed = SetRatingsExportV1Schema.parse(JSON.parse(raw));
    mergeSetRatings(parsed.ratings);
    console.info(`[eval-ui] Imported ${parsed.ratings.length} set ratings.`);
  }

  return (
    <header ref={headerRef} className="sticky top-0 z-50 border-b bg-background">
      <div className="mx-auto flex w-full items-center justify-between gap-3 px-4 py-3 lg:px-6">
        <div className="flex min-w-0 items-center gap-2">
          <div className="truncate text-sm font-semibold">
            <Link
              to="/"
              className="underline-offset-4 hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
            >
              ChartCoach
            </Link>{" "}
            <span className="text-muted-foreground">· Guideline Eval</span>
          </div>

          <div
            className="inline-flex items-center gap-2 rounded-full border px-2 py-1"
            title={syncTitle}
            aria-label={syncTitle}
          >
            <RefreshCw
              className={
                sync.status === "syncing"
                  ? "size-3.5 animate-spin text-muted-foreground"
                  : "size-3.5 text-muted-foreground"
              }
              aria-hidden="true"
            />
            <span
              className={`inline-block size-2 rounded-full ${syncDotClass}`}
              aria-hidden="true"
            />
            <span className="sr-only">{syncLabel}</span>
          </div>

          {!isOnline ? (
            <div className="rounded-full border px-2 py-1 text-xs text-muted-foreground">
              Offline
            </div>
          ) : null}
        </div>

        <div className="flex shrink-0 items-center gap-2">
          <input
            ref={importInputRef}
            type="file"
            accept="application/json"
            className="sr-only"
            onChange={(event) => {
              const file = event.currentTarget.files?.[0];
              if (!file) return;
              event.currentTarget.value = "";
              void handleImportFromFile(file).catch((error) => {
                console.warn("[eval-ui] Failed to import guideline ratings.", error);
              });
            }}
          />

          <input
            ref={setImportInputRef}
            type="file"
            accept="application/json"
            className="sr-only"
            onChange={(event) => {
              const file = event.currentTarget.files?.[0];
              if (!file) return;
              event.currentTarget.value = "";
              void handleImportSetRatingsFromFile(file).catch((error) => {
                console.warn("[eval-ui] Failed to import set ratings.", error);
              });
            }}
          />

          <button
            type="button"
            onClick={() => downloadGuidelineRatingsExport(ratings)}
            className="inline-flex items-center gap-2 rounded-md border px-2 py-1 text-xs text-muted-foreground hover:bg-muted focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
            title="Download ratings as JSON"
            aria-label="Download ratings as JSON"
          >
            <Download className="size-3.5" aria-hidden="true" />
            <span className="hidden sm:inline">Export</span>
          </button>

          <button
            type="button"
            onClick={() => importInputRef.current?.click()}
            className="inline-flex items-center gap-2 rounded-md border px-2 py-1 text-xs text-muted-foreground hover:bg-muted focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
            title="Import ratings from JSON"
            aria-label="Import ratings from JSON"
          >
            <Upload className="size-3.5" aria-hidden="true" />
            <span className="hidden sm:inline">Import</span>
          </button>

          <button
            type="button"
            onClick={() => {
              if (typeof window === "undefined") return;
              const ok = window.confirm("Clear all local guideline ratings on this device?");
              if (!ok) return;
              clearGuidelineRatings();
            }}
            className="inline-flex items-center gap-2 rounded-md border px-2 py-1 text-xs text-muted-foreground hover:bg-muted focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
            title="Clear all local ratings"
            aria-label="Clear all local ratings"
          >
            <Trash2 className="size-3.5" aria-hidden="true" />
            <span className="hidden sm:inline">Clear</span>
          </button>

          <button
            type="button"
            onClick={() => downloadSetRatingsExport(setRatings)}
            className="inline-flex items-center gap-2 rounded-md border px-2 py-1 text-xs text-muted-foreground hover:bg-muted focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
            title="Download set ratings as JSON"
            aria-label="Download set ratings as JSON"
          >
            <Download className="size-3.5" aria-hidden="true" />
            <span className="hidden sm:inline">Export sets</span>
          </button>

          <button
            type="button"
            onClick={() => setImportInputRef.current?.click()}
            className="inline-flex items-center gap-2 rounded-md border px-2 py-1 text-xs text-muted-foreground hover:bg-muted focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
            title="Import set ratings from JSON"
            aria-label="Import set ratings from JSON"
          >
            <Upload className="size-3.5" aria-hidden="true" />
            <span className="hidden sm:inline">Import sets</span>
          </button>

          <button
            type="button"
            onClick={() => {
              if (typeof window === "undefined") return;
              const ok = window.confirm("Clear all local set ratings on this device?");
              if (!ok) return;
              clearSetRatings();
            }}
            className="inline-flex items-center gap-2 rounded-md border px-2 py-1 text-xs text-muted-foreground hover:bg-muted focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
            title="Clear all local set ratings"
            aria-label="Clear all local set ratings"
          >
            <Trash2 className="size-3.5" aria-hidden="true" />
            <span className="hidden sm:inline">Clear sets</span>
          </button>

          <ThemeSelector />
        </div>
      </div>
    </header>
  );
}
