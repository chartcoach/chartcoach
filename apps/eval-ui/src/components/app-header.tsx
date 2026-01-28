import { Link } from "@tanstack/react-router";
import { useLiveQuery } from "@tanstack/react-db";
import { useIsFetching } from "@tanstack/react-query";
import { RefreshCw } from "lucide-react";
import { useLayoutEffect, useRef } from "react";

import { relevanceRatingsCollection } from "@chartcoach/eval-ui/db-collections";
import type { RelevanceRating } from "@chartcoach/eval-ui/db-collections";
import { useAutoUploadRelevanceRatings } from "@chartcoach/eval-ui/eval/hooks/use-auto-upload-relevance-ratings";
import { usePullRelevanceRatingsFromS3 } from "@chartcoach/eval-ui/eval/hooks/use-pull-relevance-ratings";
import { ThemeSelector } from "@chartcoach/eval-ui/components/theme-selector";
import { useOnlineStatus } from "@chartcoach/eval-ui/lib/eval-utils";

export function AppHeader() {
  const headerRef = useRef<HTMLElement | null>(null);

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
      q.from({ rating: relevanceRatingsCollection }).select(({ rating }) => ({
        ...rating,
      })),
    [],
  );

  const ratings = (data ?? []) as RelevanceRating[];
  const ratingCount = ratings.length;

  const sync = useAutoUploadRelevanceRatings(ratings);
  const pull = usePullRelevanceRatingsFromS3();

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

  return (
    <header ref={headerRef} className="sticky top-0 z-50 border-b bg-background">
      <div className="mx-auto flex w-full items-center justify-between gap-3 px-4 py-3 lg:px-6">
        <div className="flex min-w-0 items-center gap-2">
          <div className="truncate text-sm font-semibold">
            <Link
              to="/"
              className="underline-offset-4 hover:underline focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
            >
              ChartCoach
            </Link>{" "}
            <span className="text-muted-foreground">· Guideline Relevance Eval</span>
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
          <ThemeSelector />
        </div>
      </div>
    </header>
  );
}
