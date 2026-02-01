import { queryOptions, useQuery } from "@tanstack/react-query";
import { useEffect, useMemo, useRef } from "react";

import {
  guidelineRatingsCollection,
  mergeGuidelineRatings,
} from "@chartcoach/eval-ui/db-collections";
import type { GuidelineRatingsExportV2 } from "@chartcoach/eval-ui/eval/guideline-ratings";
import {
  SYNC_LAST_SIGNATURE_STORAGE_KEY,
  SYNC_LAST_SUCCESS_AT_STORAGE_KEY,
  SYNC_LAST_SUCCESS_KEY_STORAGE_KEY,
  getLocalStorageItem,
  makeRatingsSignature,
  setLocalStorageItem,
} from "@chartcoach/eval-ui/eval/guideline-ratings-sync-metadata";
import { downloadLatestGuidelineRatingsExport } from "@chartcoach/eval-ui/eval/server/guideline-ratings-sync.server";
import { getDeviceId, useOnlineStatus } from "@chartcoach/eval-ui/lib/eval-utils";

type PullStatus = "idle" | "pulling" | "synced" | "error" | "disabled";

function latestRatingsExportQueryOptions(deviceId: string) {
  return queryOptions({
    queryKey: ["eval", "guideline-ratings", "latest-export", deviceId],
    networkMode: "online",
    queryFn: async () =>
      await downloadLatestGuidelineRatingsExport({
        data: { deviceId },
      }),
    staleTime: 30_000,
  });
}

export function usePullGuidelineRatingsFromS3() {
  const isOnline = useOnlineStatus();
  const deviceId = useMemo(() => getDeviceId(), []);
  const lastImportedKeyRef = useRef<string | null>(null);

  const query = useQuery({
    ...latestRatingsExportQueryOptions(deviceId),
    enabled: isOnline,
    retry: 1,
  });

  useEffect(() => {
    if (!query.data?.found) return;
    if (lastImportedKeyRef.current === query.data.key) return;
    lastImportedKeyRef.current = query.data.key;

    mergeGuidelineRatings(query.data.export.ratings);

    const lastSignature = getLocalStorageItem(SYNC_LAST_SIGNATURE_STORAGE_KEY);
    if (lastSignature) return;

    const remoteSignature = makeRatingsSignature(query.data.export.ratings);
    const localSignature = makeRatingsSignature([...guidelineRatingsCollection.state.values()]);

    if (remoteSignature !== localSignature) return;

    setLocalStorageItem(SYNC_LAST_SIGNATURE_STORAGE_KEY, localSignature);
    setLocalStorageItem(SYNC_LAST_SUCCESS_AT_STORAGE_KEY, query.data.export.exportedAt);
    setLocalStorageItem(SYNC_LAST_SUCCESS_KEY_STORAGE_KEY, query.data.key);
  }, [query.data]);

  const pulledExport: GuidelineRatingsExportV2 | null = query.data?.found ? query.data.export : null;

  const status: PullStatus =
    query.isError && query.error instanceof Error
      ? query.error.message.toLowerCase().includes("not configured")
        ? "disabled"
        : "error"
      : query.isFetching
        ? "pulling"
        : pulledExport
          ? "synced"
          : "idle";

  return {
    status,
    isOnline,
    exportedAt: pulledExport?.exportedAt ?? null,
    key: query.data?.found ? query.data.key : null,
    error: query.isError ? query.error : null,
  };
}

