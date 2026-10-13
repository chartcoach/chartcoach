import type { ReactNode } from "react";
import { redirect } from "next/navigation";
import { threadIdSchema } from "../../../../shared/threads";

export default async function Layout({
  children,
  params,
}: {
  children: ReactNode;
  params: Promise<{ threadId: string }>;
}) {
  if (!threadIdSchema.safeParse((await params).threadId).success) redirect("/");

  return children;
}
