import type { ViewerActions, ViewerState } from "@/viewer/contract/types";

function isTypingTarget(target: EventTarget | null): boolean {
  return (
    target instanceof HTMLInputElement ||
    target instanceof HTMLSelectElement ||
    target instanceof HTMLTextAreaElement
  );
}

export function createRootKeydownHandler(getState: () => ViewerState, actions: ViewerActions) {
  return function onKeydown(event: KeyboardEvent): void {
    if (isTypingTarget(event.target)) {
      return;
    }

    const state = getState();

    if (event.key === "ArrowRight") {
      event.preventDefault();
      actions.stepCase(1);
      return;
    }

    if (event.key === "ArrowLeft") {
      event.preventDefault();
      actions.stepCase(-1);
      return;
    }

    if (event.key === "Escape" && state.activePopoverId) {
      event.preventDefault();
      actions.closePopover();
      return;
    }

    if (event.key === "Escape" && state.inspectCellKey) {
      event.preventDefault();
      actions.closeInspect();
    }
  };
}
