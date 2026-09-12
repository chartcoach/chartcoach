import { useEffect, useEffectEvent, useState } from "react";

export function useFileDrop(disabled: boolean, onFiles: (files: File[]) => void) {
  const [active, setActive] = useState(false);

  const dragOver = useEffectEvent((event: DragEvent) => {
    if (!event.dataTransfer?.types.includes("Files")) return;
    event.preventDefault();
    event.dataTransfer.dropEffect = disabled ? "none" : "copy";
  });

  const drop = useEffectEvent((event: DragEvent) => {
    if (!event.dataTransfer?.types.includes("Files")) return;
    event.preventDefault();

    if (!disabled) onFiles(Array.from(event.dataTransfer.files));
  });

  useEffect(() => {
    const targets = new Set<EventTarget>();

    function reset() {
      targets.clear();
      setActive(false);
    }

    function enter(event: DragEvent) {
      if (!event.dataTransfer?.types.includes("Files") || !event.target) return;
      targets.add(event.target);
      setActive(true);
    }

    function leave(event: DragEvent) {
      if (event.target) targets.delete(event.target);

      if (targets.size === 0) reset();
    }

    function finish(event: DragEvent) {
      reset();
      drop(event);
    }

    function keyDown(event: KeyboardEvent) {
      if (event.key === "Escape") reset();
    }

    window.addEventListener("dragenter", enter);
    window.addEventListener("dragleave", leave);
    window.addEventListener("dragover", dragOver);
    window.addEventListener("drop", finish);
    window.addEventListener("dragend", reset);
    window.addEventListener("blur", reset);
    window.addEventListener("keydown", keyDown);

    return () => {
      window.removeEventListener("dragenter", enter);
      window.removeEventListener("dragleave", leave);
      window.removeEventListener("dragover", dragOver);
      window.removeEventListener("drop", finish);
      window.removeEventListener("dragend", reset);
      window.removeEventListener("blur", reset);
      window.removeEventListener("keydown", keyDown);
    };
  }, []);

  return active;
}
