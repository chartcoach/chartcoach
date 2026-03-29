import type { AnywidgetModelLike, AssetPayloads } from "@/viewer/contract/types";

export function createCommandInvoker(model: AnywidgetModelLike) {
  let nextId = 0;

  return function invoke(
    name: "load_assets",
    msg: Record<string, unknown> = {},
  ): Promise<AssetPayloads> {
    return new Promise<AssetPayloads>((resolve, reject) => {
      const requestId = `cmd-${Date.now()}-${nextId++}`;
      const timer = window.setTimeout(() => {
        model.off("msg:custom", onMessage);
        reject(new Error(`Command timed out: ${name}`));
      }, 60000);

      function onMessage(content: unknown) {
        if (
          !content ||
          typeof content !== "object" ||
          (content as { kind?: string }).kind !== "anywidget-command-response"
        ) {
          return;
        }
        if ((content as { id?: string }).id !== requestId) {
          return;
        }

        window.clearTimeout(timer);
        model.off("msg:custom", onMessage);

        const response = (
          content as {
            response?: {
              ok?: boolean;
              payload?: AssetPayloads;
              error?: { message?: string };
            };
          }
        ).response;

        if (response?.ok === false) {
          reject(new Error(response.error?.message || `Command failed: ${name}`));
          return;
        }

        resolve(response?.payload ?? { assets: [] });
      }

      model.on("msg:custom", onMessage);

      try {
        model.send?.({
          kind: "anywidget-command",
          id: requestId,
          name,
          msg,
        });
      } catch (error) {
        window.clearTimeout(timer);
        model.off("msg:custom", onMessage);
        reject(error);
      }
    });
  };
}
