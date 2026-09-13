import { agentRuns } from "eve/instrumentation/otel";

export default agentRuns({
  exportPolicy: { span: ({ attributes }) => attributes["chartcoach.media"] !== true },
});
