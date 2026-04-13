import { mountAnywidgetVisgroundViewer } from "@chartcoach/visground-viewer";

type ModelLike = {
  get(name: string): unknown;
  set(name: string, value: unknown): void;
  save_changes(): void;
  on(name: string, callback: (...args: unknown[]) => void): void;
  off(name: string, callback: (...args: unknown[]) => void): void;
  send?(content: unknown): void;
};

type RenderContext = {
  model: ModelLike;
  el: HTMLElement;
};

function resolveArtifactUrl(model: ModelLike) {
  const artifactUrl = model.get("_artifact_url");
  if (typeof artifactUrl === "string" && artifactUrl.length > 0) {
    return artifactUrl;
  }

  throw new Error("VisGround viewer requires `_artifact_url` to point to a viewer artifact.");
}

function render({ model, el }: RenderContext) {
  const artifactUrl = resolveArtifactUrl(model);
  const mount = mountAnywidgetVisgroundViewer(el, {
    artifactUrl,
    model,
  });

  return () => {
    mount.destroy();
  };
}

export default { render };
