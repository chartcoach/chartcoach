import { useEffect, useState } from "react";
import { loadGuidelinePage } from "../browser/workspace-client";

export function useGuidelinePage(id: string) {
  const [guideline, setGuideline] = useState<Awaited<ReturnType<typeof loadGuidelinePage>>>();
  const [error, setError] = useState<string>();
  useEffect(() => {
    const controller = new AbortController();
    setGuideline(undefined);
    setError(undefined);

    void loadGuidelinePage(id, controller.signal)
      .then((value) => {
        if (!controller.signal.aborted) setGuideline(value);
      })
      .catch((cause) => {
        if (!controller.signal.aborted)
          setError(cause instanceof Error ? cause.message : "Could not read this guideline.");
      });

    return () => controller.abort();
  }, [id]);

  return { guideline, error };
}
