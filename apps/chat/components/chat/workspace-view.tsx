import { ViewTransition, type ReactNode } from "react";

export function WorkspaceView({ children }: { children: ReactNode }) {
  return (
    <ViewTransition
      default="none"
      name="workspace-content"
      share="content-crossfade"
      enter="content-crossfade"
      exit="content-crossfade"
    >
      {children}
    </ViewTransition>
  );
}
