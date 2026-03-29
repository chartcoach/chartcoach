import { mountVisgroundViewer } from "../../../packages/visground-viewer/src/index";

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
  const mount = mountVisgroundViewer(el, {
    model,
  });

  return () => {
    mount.destroy();
  };
}

export default { render };
