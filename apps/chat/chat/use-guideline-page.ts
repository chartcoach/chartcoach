import { useEffect, useState } from "react";
import { loadGuidelinePage, WorkspaceRequestError } from "../browser/workspace-client";

export function useGuidelinePage(id: string) {
  const [guideline, setGuideline] = useState<Awaited<ReturnType<typeof loadGuidelinePage>>>();
  const [error, setError] = useState<string>();
  const [notFound, setNotFound] = useState(false);
  useEffect(() => {
    const controller = new AbortController();
    setGuideline(undefined);
    setError(undefined);
    setNotFound(false);

    void loadGuidelinePage(id, controller.signal)
      .then((value) => {
        if (!controller.signal.aborted) setGuideline(value);
      })
      .catch((cause) => {
        if (controller.signal.aborted) return;

        if (cause instanceof WorkspaceRequestError && cause.status === 404) setNotFound(true);
        else setError(cause instanceof Error ? cause.message : "Could not read this guideline.");
      });

    return () => controller.abort();
  }, [id]);

  return { guideline, error, notFound };
}
