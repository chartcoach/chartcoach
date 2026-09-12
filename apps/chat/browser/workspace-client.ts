import { z } from "zod";
import {
  connectionSchema,
  modelSchema,
  preferencesSchema,
  threadDetailSchema,
  threadSchema,
  type ConnectionInput,
  type ThreadDetail,
} from "../shared/preferences";
import type { ChartAttachment } from "../chat/attachment";

async function request<T, B>(path: string, schema: z.ZodType<T>, body?: B, signal?: AbortSignal) {
  const options: RequestInit = { signal, cache: "no-store" };

  if (body !== undefined) {
    options.method = "POST";
    options.headers = { "content-type": "application/json" };
    options.body = JSON.stringify(body);
  }

  const response = await fetch(`/eve/v1/${path}`, options);
  const data: unknown = await response.json();

  if (!response.ok)
    throw new Error(
      z.object({ error: z.string() }).safeParse(data).data?.error ??
        "The request failed. Try again.",
    );

  return schema.parse(data);
}

const ok = z.object({ ok: z.literal(true) });

export const loadPreferences = (signal?: AbortSignal) =>
  request("preferences", preferencesSchema, undefined, signal);

export const saveConnection = (value: ConnectionInput, signal?: AbortSignal) =>
  request("connections", connectionSchema, value, signal);

export const removeConnection = (id: string, signal?: AbortSignal) =>
  request(`connections/${encodeURIComponent(id)}/remove`, ok, {}, signal);

export const loadModels = (value: ConnectionInput, signal?: AbortSignal) =>
  request("connections/models", z.array(modelSchema), value, signal);

export const loadThreads = (signal?: AbortSignal) =>
  request("threads", z.array(threadSchema), undefined, signal);

export const loadThread = (id: string, signal?: AbortSignal) =>
  request(`threads/${encodeURIComponent(id)}`, threadDetailSchema, undefined, signal);

export const createThread = (
  value: { title: string; connectionId: string; knowledge: ThreadDetail["knowledge"] },
  signal?: AbortSignal,
) => request("threads", threadDetailSchema, value, signal);

export const updateThread = (id: string, value: { title?: string; archived?: boolean }) =>
  request(`threads/${encodeURIComponent(id)}`, ok, value);

export const saveChartImage = (id: string, value: ChartAttachment, signal?: AbortSignal) =>
  request(`threads/${encodeURIComponent(id)}/images`, ok, value, signal);

export const chartImageURL = (id: string, filename: string) =>
  `/eve/v1/threads/${encodeURIComponent(id)}/images/${encodeURIComponent(filename)}`;

export async function loadChartImage(id: string, filename: string) {
  const response = await fetch(chartImageURL(id, filename), {
    signal: AbortSignal.timeout(15_000),
  });

  if (!response.ok)
    throw new Error(
      "Could not restore your chart. Try again before changing the guideline selection.",
    );
  const blob = await response.blob();

  return new File([blob], filename, { type: blob.type });
}
