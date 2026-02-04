import { useEffect, useMemo, useRef, useState } from "react";

import type { GuidelineRating, ScenarioSetRating } from "@chartcoach/eval-ui/db-collections";
import {
  SYNC_LAST_SIGNATURE_STORAGE_KEY,
  SYNC_LAST_SUCCESS_AT_STORAGE_KEY,
  SYNC_LAST_SUCCESS_KEY_STORAGE_KEY,
  getLocalStorageItem,
  makeEvalDataSignature,
  setLocalStorageItem,
} from "@chartcoach/eval-ui/eval/eval-data-sync-metadata";
import { uploadEvalDataExport } from "@chartcoach/eval-ui/eval/server/eval-data-sync.server";
import { createEvalDataExport } from "@chartcoach/eval-ui/lib/export-eval-data";
import { getDeviceId, useOnlineStatus } from "@chartcoach/eval-ui/lib/eval-utils";

type SyncStatus = "idle" | "queued" | "syncing" | "synced" | "error" | "disabled";

function signatureDigest(signature: string) {
  const parts = signature.split(":");
  if (parts.length < 3) return undefined;
  return parts[1];
}

export function useAutoUploadEvalData({
  guidelineRatings,
  setRatings,
}: {
  guidelineRatings: GuidelineRating[];
  setRatings: ScenarioSetRating[];
}) {
  const isOnline = useOnlineStatus();

  const signature = useMemo(
    () => makeEvalDataSignature({ guidelineRatings, setRatings }),
    [guidelineRatings, setRatings],
  );

  const dataRef = useRef({ guidelineRatings, setRatings, signature });
  useEffect(() => {
    dataRef.current = { guidelineRatings, setRatings, signature };
  }, [guidelineRatings, setRatings, signature]);

  const [status, setStatus] = useState<SyncStatus>("idle");
  const [message, setMessage] = useState<string | null>(null);
  const [lastSuccessAt, setLastSuccessAt] = useState<string | null>(() =>
    getLocalStorageItem(SYNC_LAST_SUCCESS_AT_STORAGE_KEY),
  );
  const [lastSuccessKey, setLastSuccessKey] = useState<string | null>(() =>
    getLocalStorageItem(SYNC_LAST_SUCCESS_KEY_STORAGE_KEY),
  );

  const uploadTimerIdRef = useRef<number | null>(null);
  const messageTimerIdRef = useRef<number | null>(null);
  const inFlightRef = useRef(false);
  const lastFailureAtRef = useRef<number | null>(null);

  function clearUploadTimer() {
    if (uploadTimerIdRef.current === null) return;
    window.clearTimeout(uploadTimerIdRef.current);
    uploadTimerIdRef.current = null;
  }

  function clearMessageTimer() {
    if (messageTimerIdRef.current === null) return;
    window.clearTimeout(messageTimerIdRef.current);
    messageTimerIdRef.current = null;
  }

  function notify(nextMessage: string) {
    setMessage(nextMessage);
    clearMessageTimer();
    messageTimerIdRef.current = window.setTimeout(() => {
      setMessage(null);
      messageTimerIdRef.current = null;
    }, 5000);
  }

  async function uploadNow() {
    if (typeof window === "undefined") return;
    if (!isOnline) return;
    if (inFlightRef.current) return;

    const lastSignature = getLocalStorageItem(SYNC_LAST_SIGNATURE_STORAGE_KEY);
    const { signature: currentSignature, guidelineRatings, setRatings } = dataRef.current;

    if (guidelineRatings.length === 0 && setRatings.length === 0) return;
    if (lastSignature === currentSignature) return;

    const lastFailureAt = lastFailureAtRef.current;
    if (lastFailureAt && Date.now() - lastFailureAt < 30_000) {
      return;
    }

    inFlightRef.current = true;
    setStatus("syncing");

    try {
      const exportPayload = createEvalDataExport(guidelineRatings, setRatings);
      const digest = signatureDigest(currentSignature);
      const result = await uploadEvalDataExport({
        data: {
          deviceId: getDeviceId(),
          export: exportPayload,
          ...(digest ? { digest } : {}),
        },
      });

      setLocalStorageItem(SYNC_LAST_SIGNATURE_STORAGE_KEY, currentSignature);
      setLocalStorageItem(SYNC_LAST_SUCCESS_AT_STORAGE_KEY, new Date().toISOString());
      setLocalStorageItem(SYNC_LAST_SUCCESS_KEY_STORAGE_KEY, result.key);

      setLastSuccessAt(getLocalStorageItem(SYNC_LAST_SUCCESS_AT_STORAGE_KEY));
      setLastSuccessKey(result.key);
      lastFailureAtRef.current = null;

      setStatus("synced");
      notify("Synced");
    } catch (error) {
      console.warn("[eval-ui] Auto-upload eval data failed.", error);
      lastFailureAtRef.current = Date.now();

      const message = error instanceof Error ? error.message : "Failed to sync ratings.";

      if (message.toLowerCase().includes("not configured")) {
        setStatus("disabled");
        notify("Sync disabled");
        return;
      }

      setStatus("error");
      notify("Sync failed");
    } finally {
      inFlightRef.current = false;
    }
  }

  useEffect(() => {
    if (typeof window === "undefined") return;
    return () => {
      clearUploadTimer();
      clearMessageTimer();
    };
  }, []);

  useEffect(() => {
    if (typeof window === "undefined") return;
    if (status === "disabled") return;

    clearUploadTimer();

    const hasAny = guidelineRatings.length > 0 || setRatings.length > 0;
    if (!hasAny) {
      setStatus("idle");
      return;
    }

    const lastSignature = getLocalStorageItem(SYNC_LAST_SIGNATURE_STORAGE_KEY);
    const needsSync = lastSignature !== signature;

    if (!needsSync) {
      if (lastSignature) setStatus("synced");
      return;
    }

    if (!isOnline) {
      setStatus("queued");
      return;
    }

    setStatus("queued");
    uploadTimerIdRef.current = window.setTimeout(() => {
      void uploadNow();
    }, 2500);
  }, [signature, guidelineRatings.length, setRatings.length, isOnline, status]);

  return {
    status,
    message,
    lastSuccessAt,
    lastSuccessKey,
  };
}

