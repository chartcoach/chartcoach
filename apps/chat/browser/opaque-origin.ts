// A sandboxed embedding frame gives ChartCoach an opaque origin. Requests to its own
// server are then cross-origin, and fetch omits the browser identity and embed access
// cookies unless credentials are included. Eve's client calls the global fetch, so
// the default is installed there.
if (globalThis.origin === "null") {
  const send = globalThis.fetch.bind(globalThis);

  globalThis.fetch = (input, init) => {
    const url = new URL(input instanceof Request ? input.url : String(input), location.href);

    return url.origin === location.origin
      ? send(input, { credentials: "include", ...init })
      : send(input, init);
  };
}
