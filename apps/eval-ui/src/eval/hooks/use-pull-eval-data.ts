import { queryOptions, useQuery } from "@tanstack/react-query";
import { useEffect, useMemo, useRef } from "react";

import {
  guidelineRatingsCollection,
  mergeGuidelineRatings,
  mergeSetRatings,
  setRatingsCollection,
} from "@chartcoach/eval-ui/db-collections";
import type { EvalDataExportV1 } from "@chartcoach/eval-ui/eval/eval-data";
import type { GuidelineRatingsExportV2 } from "@chartcoach/eval-ui/eval/guideline-ratings";
import {
  SYNC_LAST_SIGNATURE_STORAGE_KEY,
  SYNC_LAST_SUCCESS_AT_STORAGE_KEY,
  SYNC_LAST_SUCCESS_KEY_STORAGE_KEY,
  getLocalStorageItem,
  makeEvalDataSignature,
  setLocalStorageItem,
} from "@chartcoach/eval-ui/eval/eval-data-sync-metadata";
import { downloadLatestEvalDataExport } from "@chartcoach/eval-ui/eval/server/eval-data-sync.server";
import { downloadLatestGuidelineRatingsExport } from "@chartcoach/eval-ui/eval/server/guideline-ratings-sync.server";
import { getDeviceId, useOnlineStatus } from "@chartcoach/eval-ui/lib/eval-utils";

type PullStatus = "idle" | "pulling" | "synced" | "error" | "disabled";

type PullResult =
  | { kind: "none" }
  | { kind: "eval-data"; key: string; export: EvalDataExportV1 }
  | { kind: "legacy-guideline-ratings"; key: string; export: GuidelineRatingsExportV2 };

function latestExportQueryOptions(deviceId: string) {
  return queryOptions({
    queryKey: ["eval", "eval-data", "latest-export", deviceId],
    networkMode: "online",
    queryFn: async (): Promise<PullResult> => {
      const combined = await downloadLatestEvalDataExport({ data: { deviceId } });
      if (combined.found) {
        return { kind: "eval-data", key: combined.key, export: combined.export };
      }

      const legacyGuidelines = await downloadLatestGuidelineRatingsExport({
        data: { deviceId },
      });
      if (legacyGuidelines.found) {
        return {
          kind: "legacy-guideline-ratings",
          key: legacyGuidelines.key,
          export: legacyGuidelines.export,
        };
      }

      return { kind: "none" };
    },
    staleTime: 30_000,
  });
}

export function usePullEvalDataFromS3() {
  const isOnline = useOnlineStatus();
  const deviceId = useMemo(() => getDeviceId(), []);
  const lastImportedKeyRef = useRef<string | null>(null);

  const query = useQuery({
    ...latestExportQueryOptions(deviceId),
    enabled: isOnline,
    retry: 1,
  });

  useEffect(() => {
    if (!query.data) return;
    if (query.data.kind === "none") return;
    if (lastImportedKeyRef.current === query.data.key) return;
    lastImportedKeyRef.current = query.data.key;

    if (query.data.kind === "eval-data") {
      mergeGuidelineRatings(query.data.export.guidelineRatings.ratings);
      mergeSetRatings(query.data.export.setRatings.ratings);
    } else {
      mergeGuidelineRatings(query.data.export.ratings);
    }

    const lastSignature = getLocalStorageItem(SYNC_LAST_SIGNATURE_STORAGE_KEY);
    if (lastSignature) return;

    const remoteGuidelineRatings =
      query.data.kind === "eval-data"
        ? query.data.export.guidelineRatings.ratings
        : query.data.export.ratings;
    const remoteSetRatings = query.data.kind === "eval-data" ? query.data.export.setRatings.ratings : [];

    const remoteSignature = makeEvalDataSignature({
      guidelineRatings: remoteGuidelineRatings,
      setRatings: remoteSetRatings,
    });
    const localSignature = makeEvalDataSignature({
      guidelineRatings: [...guidelineRatingsCollection.state.values()],
      setRatings: [...setRatingsCollection.state.values()],
    });

    if (remoteSignature !== localSignature) return;

    const remoteExportedAt =
      query.data.kind === "eval-data"
        ? query.data.export.exportedAt
        : query.data.export.exportedAt;

    setLocalStorageItem(SYNC_LAST_SIGNATURE_STORAGE_KEY, localSignature);
    setLocalStorageItem(SYNC_LAST_SUCCESS_AT_STORAGE_KEY, remoteExportedAt);
    setLocalStorageItem(SYNC_LAST_SUCCESS_KEY_STORAGE_KEY, query.data.key);
  }, [query.data]);

  const foundExport =
    query.data?.kind === "eval-data"
      ? query.data.export
      : query.data?.kind === "legacy-guideline-ratings"
        ? query.data.export
        : null;

  const status: PullStatus =
    query.isError && query.error instanceof Error
      ? query.error.message.toLowerCase().includes("not configured")
        ? "disabled"
        : "error"
      : query.isFetching
        ? "pulling"
        : foundExport
          ? "synced"
          : "idle";

  return {
    status,
    isOnline,
    exportedAt:
      query.data?.kind === "eval-data"
        ? query.data.export.exportedAt
        : query.data?.kind === "legacy-guideline-ratings"
          ? query.data.export.exportedAt
          : null,
    key: query.data?.kind && query.data.kind !== "none" ? query.data.key : null,
    source:
      query.data?.kind === "eval-data"
        ? ("eval-data" as const)
        : query.data?.kind === "legacy-guideline-ratings"
          ? ("legacy-guideline-ratings" as const)
          : null,
    error: query.isError ? query.error : null,
  };
}

