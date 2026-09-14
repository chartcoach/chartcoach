import { disableInstrumentation } from "eve/instrumentation";
import { otelIntegration } from "eve/instrumentation/otel";
import { LangfuseProcessor, traceContext } from "../telemetry";
import { env, langfuseTracingEnabled } from "../../lib/env";

export default langfuseTracingEnabled
  ? otelIntegration({
      spanProcessors: [
        new LangfuseProcessor({
          publicKey: env.LANGFUSE_PUBLIC_KEY,
          secretKey: env.LANGFUSE_SECRET_KEY,
          baseUrl: env.LANGFUSE_BASE_URL,
          release: env.LANGFUSE_RELEASE,
          environment: env.LANGFUSE_TRACING_ENVIRONMENT ?? env.VERCEL_ENV ?? env.NODE_ENV,
        }),
      ],
      runtimeContext: traceContext,
    })
  : disableInstrumentation();
