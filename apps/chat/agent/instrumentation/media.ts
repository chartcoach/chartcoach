import { disableInstrumentation } from "eve/instrumentation";
import { langfuseTracingEnabled } from "../../lib/env";
import { mediaInstrumentation } from "../media";

export default langfuseTracingEnabled ? mediaInstrumentation() : disableInstrumentation();
