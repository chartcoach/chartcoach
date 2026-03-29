export const HOVER_HIDE_DELAY_MS = 220;

export function positionHoverCard(hoverCard: HTMLElement, anchor: HTMLElement): void {
  const margin = 24;
  const anchorRect = anchor.getBoundingClientRect();
  hoverCard.style.top = "0px";
  hoverCard.style.left = "0px";
  const cardRect = hoverCard.getBoundingClientRect();

  let left = anchorRect.right + margin;
  if (left + cardRect.width > window.innerWidth - margin) {
    left = Math.max(margin, anchorRect.left - cardRect.width - margin);
  }

  let top = anchorRect.top + anchorRect.height / 2 - cardRect.height / 2;
  if (top + cardRect.height > window.innerHeight - margin) {
    top = Math.max(margin, window.innerHeight - cardRect.height - margin);
  }

  hoverCard.style.left = `${left}px`;
  hoverCard.style.top = `${top}px`;
}
