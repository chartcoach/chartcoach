import {
  ForbiddenError,
  localDev,
  placeholderAuth,
  vercelOidc,
  type AuthFn,
} from "eve/channels/auth";
import { decodeSelection } from "./selection-context";
import { resolveCatalogSelection } from "../lib/catalog/selection";

export const catalogRouteAuth = [vercelOidc(), localDev(), placeholderAuth()];

// Eve maps onMessage exceptions to HTTP 500, so reject invalid headers during its auth walk.
export const reviewRouteAuth = catalogRouteAuth.map(
  (authenticate): AuthFn<Request> =>
    async (request) => {
      const caller = await authenticate(request);
      const header = request.headers.get("x-chartcoach-selection");
      if (
        !caller ||
        header === null ||
        request.method !== "POST" ||
        !new URL(request.url).pathname.endsWith("/session")
      )
        return caller;
      try {
        const selection = await resolveCatalogSelection(await decodeSelection(header), {
          signal: request.signal,
        });
        return {
          ...caller,
          attributes: { ...caller.attributes, "chartcoach.selection": JSON.stringify(selection) },
        };
      } catch (error) {
        throw new ForbiddenError({
          code: "invalid_catalog_selection",
          message: error instanceof Error ? error.message : "Check your knowledge selection.",
        });
      }
    },
);
