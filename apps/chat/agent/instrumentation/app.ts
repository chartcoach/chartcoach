import { defineInstrumentation } from "eve/instrumentation";
import { closeAppRuntime } from "../../lib/app/runtime";

export default defineInstrumentation({ shutdown: closeAppRuntime });
