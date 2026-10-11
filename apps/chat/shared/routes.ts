export const chatPath = (threadId: string) => `/chat/${encodeURIComponent(threadId)}`;

export const guidelinesPath = (threadId?: string) =>
  threadId ? `${chatPath(threadId)}/guidelines` : "/guidelines";
