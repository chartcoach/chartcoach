import { afterEach, expect, it, vi } from "vite-plus/test";
import { generateText, tool } from "ai";
import { z } from "zod";
import { Effect, Redacted } from "effect";
import { FetchHttpClient } from "@effect/platform";
import { languageModel, listProviderModels, providerEndpoint } from "../lib/app/providers";
import type { ConnectionInput, Provider } from "../shared/preferences";
import agent from "../agent/agent";

afterEach(() => vi.unstubAllGlobals());

it("rejects an invalid saved connection instead of using the server's key", async () => {
  const resolve = agent.model.events["step.started"]!;
  await expect(
    resolve(
      {},
      {
        session: {
          id: "session",
          auth: {
            initiator: null,
            current: {
              principalType: "local-dev",
              authenticator: "local-dev",
              principalId: "alice",
              attributes: {
                "chartcoach.owner": "a".repeat(64),
                "chartcoach.thread": "11111111-1111-4111-8111-111111111111",
                "chartcoach.connection": "",
              },
            },
          },
        },
        channel: {},
        messages: [],
      },
    ),
  ).rejects.toThrow("Choose an available model connection");
});

const settings = (provider: Provider): ConnectionInput => ({
  provider,
  name: "Test",
  model: "vision-model",
  contextWindow: 32_000,
  baseURL: provider === "compatible" ? "https://compatible.example/v1" : undefined,
});

const responses = {
  anthropic: {
    id: "msg_1",
    type: "message",
    role: "assistant",
    model: "vision-model",
    content: [{ type: "text", text: "Read the guidance." }],
    stop_reason: "end_turn",
    stop_sequence: null,
    usage: { input_tokens: 10, output_tokens: 4 },
  },
  openai: {
    id: "resp_1",
    created_at: 1,
    model: "vision-model",
    status: "completed",
    output: [
      {
        id: "msg_1",
        type: "message",
        role: "assistant",
        content: [{ type: "output_text", text: "Read the guidance.", annotations: [] }],
      },
    ],
    usage: { input_tokens: 10, output_tokens: 4, total_tokens: 14 },
  },
  google: {
    candidates: [
      { content: { role: "model", parts: [{ text: "Read the guidance." }] }, finishReason: "STOP" },
    ],
    usageMetadata: { promptTokenCount: 10, candidatesTokenCount: 4, totalTokenCount: 14 },
  },
  compatible: {
    id: "chat_1",
    created: 1,
    model: "vision-model",
    choices: [
      {
        index: 0,
        message: { role: "assistant", content: "Read the guidance." },
        finish_reason: "stop",
      },
    ],
    usage: { prompt_tokens: 10, completion_tokens: 4, total_tokens: 14 },
  },
};

it.each([
  [
    "anthropic",
    "https://api.anthropic.com/v1/messages",
    "x-api-key",
    {
      messages: [
        {
          role: "user",
          content: [
            { type: "text", text: "Review this chart." },
            {
              type: "image",
              source: { type: "base64", media_type: "image/png", data: "iVBORw==" },
            },
          ],
        },
      ],
      tools: [{ name: "search_guidelines" }],
    },
  ],
  [
    "openai",
    "https://api.openai.com/v1/responses",
    "authorization",
    {
      input: [
        {
          role: "user",
          content: [
            { type: "input_text", text: "Review this chart." },
            { type: "input_image", image_url: "data:image/png;base64,iVBORw==" },
          ],
        },
      ],
      tools: [{ type: "function", name: "search_guidelines" }],
    },
  ],
  [
    "google",
    "https://generativelanguage.googleapis.com/v1beta/models/vision-model:generateContent",
    "x-goog-api-key",
    {
      contents: [
        {
          role: "user",
          parts: [
            { text: "Review this chart." },
            { inlineData: { mimeType: "image/png", data: "iVBORw==" } },
          ],
        },
      ],
      tools: [{ functionDeclarations: [{ name: "search_guidelines" }] }],
    },
  ],
  [
    "compatible",
    "https://compatible.example/v1/chat/completions",
    "authorization",
    {
      messages: [
        {
          role: "user",
          content: [
            { type: "text", text: "Review this chart." },
            { type: "image_url", image_url: { url: "data:image/png;base64,iVBORw==" } },
          ],
        },
      ],
      tools: [{ type: "function", function: { name: "search_guidelines" } }],
    },
  ],
] as const)(
  "uses the native %s adapter for images and tools",
  async (provider, endpoint, authHeader, expectedBody) => {
    const requests: Request[] = [];
    vi.stubGlobal("fetch", async (input: RequestInfo | URL, init?: RequestInit) => {
      requests.push(new Request(input, init));

      return Response.json(responses[provider]);
    });

    const result = await generateText({
      model: languageModel(settings(provider), Redacted.make("provider-test-key"), [
        "https://compatible.example",
      ]),
      maxOutputTokens: 100,
      messages: [
        {
          role: "user",
          content: [
            { type: "text", text: "Review this chart." },
            { type: "file", data: new Uint8Array([137, 80, 78, 71]), mediaType: "image/png" },
          ],
        },
      ],
      tools: {
        search_guidelines: tool({
          description: "Search guidance",
          inputSchema: z.object({ query: z.string() }),
        }),
      },
    });

    expect(result.text).toBe("Read the guidance.");
    expect(requests).toHaveLength(1);
    expect(requests[0].url).toBe(endpoint);
    expect(requests[0].headers.get(authHeader)).toBe(
      authHeader === "authorization" ? "Bearer provider-test-key" : "provider-test-key",
    );
    const body: unknown = await requests[0].json();
    expect(body).toMatchObject(expectedBody);
    expect(JSON.stringify(body)).not.toContain("provider-test-key");
    expect(requests[0].redirect).toBe("error");
  },
);

it("follows Gemini model pages and excludes embedding-only models", async () => {
  const urls: string[] = [];
  vi.stubGlobal("fetch", async (input: RequestInfo | URL) => {
    const url = new URL(new Request(input).url);
    urls.push(url.href);

    return Response.json(
      url.searchParams.has("pageToken")
        ? {
            models: [
              {
                name: "models/vision",
                displayName: "Vision",
                supportedGenerationMethods: ["generateContent"],
              },
            ],
          }
        : {
            models: [{ name: "models/embed", supportedGenerationMethods: ["embedContent"] }],
            nextPageToken: "page-two",
          },
    );
  });
  expect(
    await Effect.runPromise(
      listProviderModels(settings("google"), Redacted.make("test-key")).pipe(
        Effect.provide(FetchHttpClient.layer),
      ),
    ),
  ).toEqual([{ id: "vision", name: "Vision" }]);
  expect(urls[1]).toContain("pageToken=page-two");
});

it("rejects unapproved destinations before constructing a provider", () => {
  expect(() =>
    providerEndpoint({ provider: "compatible", baseURL: "http://169.254.169.254/latest" }),
  ).toThrow("not allowed");
  expect(() =>
    providerEndpoint({
      provider: "compatible",
      baseURL: "https://user:secret@compatible.example/v1",
    }),
  ).toThrow("base URL");
});

it("cancels an oversized model response before decoding its JSON", async () => {
  let cancelled = false;
  vi.stubGlobal(
    "fetch",
    async () =>
      new Response(
        new ReadableStream({
          pull(controller) {
            controller.enqueue(new Uint8Array(1024 * 1024));
          },
          cancel() {
            cancelled = true;
          },
        }),
      ),
  );
  await expect(
    Effect.runPromise(
      listProviderModels(settings("google"), Redacted.make("test-key")).pipe(
        Effect.provide(FetchHttpClient.layer),
      ),
    ),
  ).rejects.toThrow("too large");
  expect(cancelled).toBe(true);
});

it.each(["google", "anthropic", "openai", "compatible"] as const)(
  "keeps %s failures actionable and private through its native adapter",
  async (provider) => {
    vi.stubGlobal("fetch", async () =>
      Response.json({ error: { message: "Leaked provider-test-key" } }, { status: 401 }),
    );

    const result = generateText({
      model: languageModel(settings(provider), Redacted.make("provider-test-key"), [
        "https://compatible.example",
      ]),
      prompt: "Hello",
      maxRetries: 0,
    });

    await expect(result).rejects.toThrow("Check its value and permissions");
    await expect(result).rejects.not.toThrow("provider-test-key");
    await expect(result).rejects.toThrow("vision-model (HTTP 401)");
  },
);
