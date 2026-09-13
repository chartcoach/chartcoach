import { defineSandbox } from "eve/sandbox";
import { justbash } from "eve/sandbox/just-bash";

export const sandboxBackend = justbash({ autoInstall: false });

export default defineSandbox({ backend: sandboxBackend });
