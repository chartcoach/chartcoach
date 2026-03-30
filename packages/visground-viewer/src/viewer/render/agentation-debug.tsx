import { useEffect, useState, type ComponentType } from "react";

type AgentationComponent = ComponentType<Record<string, never>>;
let agentationModulePromise: Promise<AgentationComponent> | null = null;

function loadAgentation(): Promise<AgentationComponent> {
  if (agentationModulePromise === null) {
    agentationModulePromise = import("agentation").then(
      (module) => module.Agentation as AgentationComponent,
    );
  }
  return agentationModulePromise;
}

export function AgentationDebug({ enabled }: { enabled: boolean }) {
  const [Agentation, setAgentation] = useState<AgentationComponent | null>(null);
  const [loadError, setLoadError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;

    if (!enabled) {
      return () => {
        cancelled = true;
      };
    }

    if (Agentation !== null || loadError !== null) {
      return () => {
        cancelled = true;
      };
    }

    void loadAgentation()
      .then((component) => {
        if (cancelled) {
          return;
        }
        setAgentation(() => component);
      })
      .catch((error) => {
        const message = error instanceof Error ? error.message : String(error || "Unknown error");
        console.error("[visground-viewer] failed to load Agentation", error);
        if (!cancelled) {
          setLoadError(message);
        }
      });

    return () => {
      cancelled = true;
    };
  }, [enabled, Agentation, loadError]);

  if (!enabled || Agentation === null || loadError !== null) {
    return null;
  }

  return <Agentation />;
}
