import { agentRuns } from "eve/instrumentation/otel";

export default agentRuns({
  exportPolicy: { span: ({ attributes }) => ({ emit: attributes["chartcoach.media"] !== true }) },
});
