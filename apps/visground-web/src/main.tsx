import { bootStandaloneViewer } from "@/bootstrap";

try {
  bootStandaloneViewer();
} catch (error) {
  console.error("[visground-viewer:web] bootstrap failed", error);
  const target = document.getElementById("root");
  if (!target) {
    throw error;
  }
  target.innerHTML = `
    <main style="font-family: Inter, sans-serif; padding: 24px; color: #111;">
      <h1 style="margin: 0 0 12px; font-size: 20px;">Viewer bootstrap failed</h1>
      <p style="margin: 0 0 8px;">${error instanceof Error ? error.message : String(error)}</p>
      <p style="margin: 0;">Expected artifact: <code>${new URL("/data/viewer.parquet", window.location.origin).href}</code></p>
    </main>
  `;
}
