import { disableInstrumentation } from "eve/instrumentation";
import { env } from "../../lib/env";
import { mediaInstrumentation } from "../media";

export default env.LANGFUSE_PUBLIC_KEY && env.LANGFUSE_SECRET_KEY
  ? mediaInstrumentation()
  : disableInstrumentation();
