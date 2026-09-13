import { localTraces } from "eve/instrumentation/otel";

export default localTraces({
  exportPolicy: { span: ({ attributes }) => attributes["chartcoach.media"] !== true },
});
