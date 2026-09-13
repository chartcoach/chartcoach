import { ViewTransition, type ReactNode } from "react";

export function WorkspaceView({ children }: { children: ReactNode }) {
  return (
    <ViewTransition
      default="none"
      update={{ "workspace-navigation": "content-crossfade", default: "none" }}
    >
      {children}
    </ViewTransition>
  );
}
