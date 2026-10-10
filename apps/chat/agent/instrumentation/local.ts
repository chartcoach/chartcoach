import { localTraces } from "eve/instrumentation/otel";

export default localTraces({
  exportPolicy: { span: ({ attributes }) => ({ emit: attributes["chartcoach.media"] !== true }) },
});
