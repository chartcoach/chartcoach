// A sandboxed embedding frame gives chartcoach an opaque origin. Requests to its own
// server are then cross-origin, and fetch omits the browser identity and embed access
// cookies unless credentials are included. Eve and Next call the global fetch;
// Next explicitly requests same-origin credentials even in this frame.
if (globalThis.origin === "null") {
  const send = globalThis.fetch.bind(globalThis);

  globalThis.fetch = (input, init) => {
    const url = new URL(input instanceof Request ? input.url : String(input), location.href);

    return url.origin === location.origin
      ? send(input, { ...init, credentials: "include" })
      : send(input, init);
  };
}
