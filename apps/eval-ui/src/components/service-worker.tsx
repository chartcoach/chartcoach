import { useEffect } from "react";

export function ServiceWorkerRegistration() {
  useEffect(() => {
    if (!("serviceWorker" in navigator)) {
      console.warn("[eval-ui] Service worker not supported in this browser.");
      return;
    }

    navigator.serviceWorker.register("/sw.js").catch((error) => {
      console.warn(
        "[eval-ui] Service worker registration failed (offline/private mode?)",
        error,
      );
    });
  }, []);

  return null;
}
