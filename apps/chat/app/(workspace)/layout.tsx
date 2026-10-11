import type { ReactNode } from "react";
import { ChatWorkspace } from "../../components/chat/chat";

export default function Layout({ children }: { children: ReactNode }) {
  return <ChatWorkspace>{children}</ChatWorkspace>;
}
