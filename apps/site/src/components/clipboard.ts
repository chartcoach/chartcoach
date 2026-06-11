export async function writeClipboard(text: string) {
  try {
    await navigator.clipboard.writeText(text);
    return;
  } catch {
    const field = document.createElement("textarea");
    field.value = text;
    field.setAttribute("readonly", "");
    field.style.position = "fixed";
    field.style.left = "0";
    field.style.top = "0";
    field.style.opacity = "0";
    document.body.append(field);
    field.focus();
    field.select();

    try {
      const copyDocument = document as unknown as {
        execCommand(commandId: string): boolean;
      };
      if (!copyDocument.execCommand("copy")) throw new Error("Copy command failed");
    } finally {
      field.remove();
    }
  }
}
