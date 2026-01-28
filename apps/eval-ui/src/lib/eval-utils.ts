import { useSyncExternalStore } from "react";

import { env } from "@chartcoach/eval-ui/env";

const DEVICE_ID_STORAGE_KEY = "chartcoach/eval-ui/device-id/v1";
let didWarnDeviceIdLocalStorage = false;

export function getDeviceId() {
  if (typeof window === "undefined") return "server";

  try {
    const existing = window.localStorage.getItem(DEVICE_ID_STORAGE_KEY);
    if (existing) return existing;

    const next =
      typeof crypto !== "undefined" && "randomUUID" in crypto
        ? crypto.randomUUID()
        : `${Date.now()}-${Math.random().toString(16).slice(2)}`;

    window.localStorage.setItem(DEVICE_ID_STORAGE_KEY, next);
    return next;
  } catch (error) {
    if (!didWarnDeviceIdLocalStorage) {
      didWarnDeviceIdLocalStorage = true;
      console.warn(
        "[eval-ui] Failed to read/write device id in localStorage; using 'unknown'.",
        error,
      );
    }
    return "unknown";
  }
}

const DEV_FALLBACK_TEMPLATE = "http://localhost:4321/guidelines/{id}/";

export function getGuidelineDetailHref(guidelineId: string) {
  const template =
    env.VITE_GUIDELINE_DETAIL_URL_TEMPLATE ??
    (import.meta.env.DEV ? DEV_FALLBACK_TEMPLATE : undefined);

  if (!template) return;

  return template.replaceAll("{id}", encodeURIComponent(guidelineId));
}

function subscribeOnlineStatus(callback: () => void) {
  if (typeof window === "undefined") return () => {};

  window.addEventListener("online", callback);
  window.addEventListener("offline", callback);

  return () => {
    window.removeEventListener("online", callback);
    window.removeEventListener("offline", callback);
  };
}

function getOnlineSnapshot() {
  if (typeof navigator === "undefined") return true;
  return navigator.onLine;
}

export function useOnlineStatus() {
  return useSyncExternalStore(subscribeOnlineStatus, getOnlineSnapshot, () => true);
}
