import { z } from "zod";

export const StrategyInfoSchema = z.object({
  id: z.string().min(1),
  name: z.string().min(1),
  description: z.string(),
});

export type StrategyInfo = z.infer<typeof StrategyInfoSchema>;

export type RetrievalRequestWire = {
  context: Array<Record<string, unknown>>;
  lang?: string;
  meta?: Record<string, unknown>;
  k?: number;
};

export type RetrievalResponseWire = {
  catalog: unknown[];
  meta: Record<string, unknown>;
};

const StrategiesResponseSchema = z.array(StrategyInfoSchema);

const RetrievalResponseWireSchema = z.object({
  catalog: z.array(z.unknown()),
  meta: z.record(z.string(), z.unknown()).default({}),
});

function normalizeBaseUrl(baseUrl: string) {
  return baseUrl.replace(/\/+$/, "");
}

async function readResponseText(res: Response) {
  try {
    return await res.text();
  } catch {
    return "";
  }
}

export class ChartCoachRetrievalClient {
  readonly baseUrl: string;
  readonly fetch: typeof fetch;

  constructor(opts: { baseUrl: string; fetch?: typeof fetch }) {
    this.baseUrl = normalizeBaseUrl(opts.baseUrl);
    this.fetch = opts.fetch ?? fetch;
  }

  async listStrategies(): Promise<StrategyInfo[]> {
    const res = await this.fetch(`${this.baseUrl}/v1/strategies`);
    if (!res.ok) {
      const body = await readResponseText(res);
      throw new Error(`Retrieval server error ${res.status} (${res.statusText}): ${body}`);
    }
    const json = await res.json();
    return StrategiesResponseSchema.parse(json);
  }

  async runStrategy(args: {
    strategyId: string;
    catalogUri: string;
    request: RetrievalRequestWire;
  }): Promise<RetrievalResponseWire> {
    const res = await this.fetch(`${this.baseUrl}/v1/strategies/${args.strategyId}`, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({
        catalog_uri: args.catalogUri,
        request: args.request,
      }),
    });

    if (!res.ok) {
      const body = await readResponseText(res);
      throw new Error(`Retrieval server error ${res.status} (${res.statusText}): ${body}`);
    }

    const json = await res.json();
    return RetrievalResponseWireSchema.parse(json);
  }
}
