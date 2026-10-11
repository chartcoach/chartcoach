import { disableInstrumentation } from "eve/instrumentation";
import { otelIntegration } from "eve/instrumentation/otel";
import { LangfuseProcessor } from "../telemetry";
import { traceContext } from "../trace-context";
import { contentInstrumentation } from "../trace-payloads";
import { env, langfuseTracingEnabled } from "../../lib/env";

function destination() {
  const processor = new LangfuseProcessor({
    publicKey: env.LANGFUSE_PUBLIC_KEY,
    secretKey: env.LANGFUSE_SECRET_KEY,
    baseUrl: env.LANGFUSE_BASE_URL,
    release: env.LANGFUSE_RELEASE,
    environment: env.LANGFUSE_TRACING_ENVIRONMENT ?? env.VERCEL_ENV ?? env.NODE_ENV,
  });

  // Eve bundles instrumentation entries independently. Keep capture and export
  // in this declaration so they always share the same payload collector.
  return {
    ...otelIntegration({ spanProcessors: [processor], runtimeContext: traceContext }),
    ...contentInstrumentation(processor.payloads),
  };
}

export default langfuseTracingEnabled ? destination() : disableInstrumentation();
