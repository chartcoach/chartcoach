const warnedLocalStorageOps = new Set<string>();

function warnLocalStorageOnce(opts: {
  action: "getItem" | "setItem" | "removeItem";
  key: string;
  error: unknown;
}) {
  const signature = `${opts.action}:${opts.key}`;
  if (warnedLocalStorageOps.has(signature)) return;
  warnedLocalStorageOps.add(signature);
  console.warn(`[eval-ui] localStorage.${opts.action} failed for key "${opts.key}".`, opts.error);
}

export function getLocalStorageItem(key: string) {
  if (typeof window === "undefined") return null;
  try {
    const value = window.localStorage.getItem(key);
    if (value === "") return null;
    return value;
  } catch (error) {
    warnLocalStorageOnce({ action: "getItem", key, error });
    return null;
  }
}

export function setLocalStorageItem(key: string, value: string) {
  if (typeof window === "undefined") return;
  try {
    window.localStorage.setItem(key, value);
  } catch (error) {
    warnLocalStorageOnce({ action: "setItem", key, error });
  }
}

export function removeLocalStorageItem(key: string) {
  if (typeof window === "undefined") return;
  try {
    window.localStorage.removeItem(key);
  } catch (error) {
    warnLocalStorageOnce({ action: "removeItem", key, error });
  }
}

const FNV_OFFSET_BASIS_64 = 14695981039346656037n;
const FNV_PRIME_64 = 1099511628211n;
const FNV_MASK_64 = 0xffff_ffff_ffff_ffffn;

function fnv1a64Hex(input: string) {
  let hash = FNV_OFFSET_BASIS_64;
  for (let i = 0; i < input.length; i++) {
    hash ^= BigInt(input.charCodeAt(i));
    hash = (hash * FNV_PRIME_64) & FNV_MASK_64;
  }
  return hash.toString(16).padStart(16, "0");
}

export function makeRowsSignature(rows: unknown[][]) {
  const raw = JSON.stringify(rows);
  const digest = fnv1a64Hex(raw);
  return `fnv1a64:${digest}:${rows.length}`;
}
