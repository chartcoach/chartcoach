import { useEffect, useState } from "react";
import { loadGuidelinePage } from "../browser/workspace-client";

export function useGuidelinePage() {
  const [guideline, setGuideline] = useState<Awaited<ReturnType<typeof loadGuidelinePage>>>();
  const [error, setError] = useState<string>();
  useEffect(() => {
    const id = new URL(location.href).searchParams.get("id");
    const controller = new AbortController();

    if (!id) {
      setError("Choose a guideline from your conversation.");

      return;
    }

    void loadGuidelinePage(id, controller.signal)
      .then(setGuideline)
      .catch((cause) => {
        if (!controller.signal.aborted)
          setError(cause instanceof Error ? cause.message : "Could not read this guideline.");
      });

    return () => controller.abort();
  }, []);

  return { guideline, error };
}
