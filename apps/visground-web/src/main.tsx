import { bootStandaloneViewer, expectedStandaloneViewerAssets } from "@/bootstrap";

void bootStandaloneViewer().catch((error) => {
  console.error("[visground-viewer:web] bootstrap failed", error);
  const target = document.getElementById("root");
  if (!target) {
    throw error;
  }

  const expected = expectedStandaloneViewerAssets();
  target.innerHTML = `
    <main style="font-family: Inter, sans-serif; padding: 24px; color: #111;">
      <h1 style="margin: 0 0 12px; font-size: 20px;">Viewer bootstrap failed</h1>
      <p style="margin: 0 0 8px;">${error instanceof Error ? error.message : String(error)}</p>
      <p style="margin: 0 0 8px;">Expected artifact: <code>${expected.artifactUrl}</code></p>
      <p style="margin: 0;">Expected runtime config: <code>${expected.runtimeConfigUrl}</code></p>
    </main>
  `;
});
