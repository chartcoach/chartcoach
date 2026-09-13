import { otel } from "eve/instrumentation/otel";

export default otel({
  tracePolicy: () => true,
  resource: { "service.name": "chartcoach-chat" },
});
