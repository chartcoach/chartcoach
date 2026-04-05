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

function render({ model, el }: RenderContext) {
  const devArtifactUrl = model.get("_artifact_url");
  const artifactUrl =
    typeof devArtifactUrl === "string" && devArtifactUrl.length > 0
      ? devArtifactUrl
      : new URL(/* @vite-ignore */ "../data/viewer.parquet", import.meta.url).href;
  const mount = mountAnywidgetVisgroundViewer(el, {
    artifactUrl,
    model,
  });

  return () => {
    mount.destroy();
  };
}

export default { render };
