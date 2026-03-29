export function positionPopover(
  root: HTMLElement,
  popover: HTMLElement,
  anchor: HTMLElement,
): void {
  popover.style.top = "0px";
  popover.style.left = "0px";
  popover.style.right = "auto";
  popover.style.width = "";
  popover.style.maxWidth = "";
  popover.style.position = "absolute";

  const rootRect = root.getBoundingClientRect();
  const anchorRect = anchor.getBoundingClientRect();
  const popRect = popover.getBoundingClientRect();
  const margin = 12;
  const useViewportPositioning =
    window.innerWidth <= 980 || rootRect.width > window.innerWidth + margin * 2;

  if (useViewportPositioning) {
    popover.style.position = "fixed";
    popover.style.left = `${margin}px`;
    popover.style.right = `${margin}px`;
    popover.style.width = "auto";
    popover.style.maxWidth = `${window.innerWidth - margin * 2}px`;

    const viewportRect = popover.getBoundingClientRect();
    let top = anchorRect.bottom + 10;
    if (top + viewportRect.height > window.innerHeight - margin) {
      top = anchorRect.top - viewportRect.height - 10;
    }
    top = Math.max(margin, Math.min(top, window.innerHeight - viewportRect.height - margin));

    popover.style.top = `${top}px`;
    return;
  }

  const minLeft = Math.max(margin, margin - rootRect.left);
  const maxLeft = Math.min(rootRect.width - margin, window.innerWidth - rootRect.left - margin);
  const minTop = Math.max(margin, margin - rootRect.top);
  const maxTop = Math.min(rootRect.height - margin, window.innerHeight - rootRect.top - margin);

  let left = anchorRect.left - rootRect.left;
  left = Math.max(minLeft, Math.min(left, maxLeft - popRect.width));

  let top = anchorRect.bottom - rootRect.top + 10;
  if (top + popRect.height > maxTop) {
    top = anchorRect.top - rootRect.top - popRect.height - 10;
  }
  top = Math.max(minTop, Math.min(top, maxTop - popRect.height));

  popover.style.left = `${left}px`;
  popover.style.top = `${top}px`;
}
