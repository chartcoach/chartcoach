import { useEffect } from "react";
import { useAui } from "@assistant-ui/react";

export function useModelContext(modelName: string | undefined) {
  const aui = useAui();
  useEffect(
    () => aui.modelContext.register({ getModelContext: () => ({ config: { modelName } }) }),
    [aui, modelName],
  );
}
