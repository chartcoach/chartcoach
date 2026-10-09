export function ShellLine({ line }: { line: string }) {
  const match = line.match(/^(\S+)(\s+)(.*)$/);

  if (!match) return <span className="text-code-fg">{line}</span>;

  const [, command, spacing, rest] = match;
  const quoteStarts = [rest.indexOf("'"), rest.indexOf('"')].filter((index) => index >= 0);
  const quotedTextStart = quoteStarts.length > 0 ? Math.min(...quoteStarts) : -1;

  if (quotedTextStart === -1) {
    return (
      <>
        <span className="font-medium text-code-fg">{command}</span>
        {spacing}
        <span className="text-code-fg/75">{rest}</span>
      </>
    );
  }

  return (
    <>
      <span className="font-medium text-code-fg">{command}</span>
      {spacing}
      <span className="text-code-fg/75">{rest.slice(0, quotedTextStart)}</span>
      <span className="text-code-fg/90">{rest.slice(quotedTextStart)}</span>
    </>
  );
}
