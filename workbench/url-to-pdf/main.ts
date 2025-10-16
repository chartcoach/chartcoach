#!/usr/bin/env -S deno run --allow-read --allow-write --allow-net --allow-env --allow-run

import { chromium } from "playwright";
import { ensureDir } from "@std/fs";

interface ConversionOptions {
  outputDir?: string;
  waitForNetworkIdle?: boolean;
  scrollToBottom?: boolean;
  waitAfterScroll?: number;
  viewport?: { width: number; height: number };
  pdfOptions?: {
    format?: string;
    printBackground?: boolean;
    margin?: {
      top?: string;
      right?: string;
      bottom?: string;
      left?: string;
    };
  };
}

/**
 * Scrolls to the bottom of the page gradually to trigger lazy-loading
 */
async function scrollToBottom(page: any, pauseTime = 300) {
  await page.evaluate(async (pause: number) => {
    await new Promise<void>((resolve) => {
      let totalHeight = 0;
      const distance = 100;
      const timer = setInterval(() => {
        const scrollHeight = document.body.scrollHeight;
        window.scrollBy(0, distance);
        totalHeight += distance;

        if (totalHeight >= scrollHeight) {
          clearInterval(timer);
          resolve();
        }
      }, pause);
    });
  }, pauseTime);
}

/**
 * Converts a single URL to PDF
 */
async function urlToPdf(
  url: string,
  outputPath: string,
  options: ConversionOptions = {}
) {
  const browser = await chromium.launch({
    headless: true,
  });

  try {
    const context = await browser.newContext({
      viewport: options.viewport || { width: 1920, height: 1080 },
    });

    const page = await context.newPage();

    console.log(`📄 Loading: ${url}`);

    // Navigate to the URL and wait for network idle
    await page.goto(url, {
      waitUntil: options.waitForNetworkIdle ? "networkidle" : "load",
      timeout: 150_000,
    });

    // Wait a bit for any dynamic content to render
    await page.waitForTimeout(1000);

    // Scroll to bottom if requested
    if (options.scrollToBottom) {
      console.log(`📜 Scrolling to bottom...`);
      await scrollToBottom(page, 300);

      // Wait for any lazy-loaded content
      await page.waitForTimeout(options.waitAfterScroll || 2000);

      // Wait for network to be idle after scrolling
      if (options.waitForNetworkIdle) {
        await page.waitForLoadState("networkidle");
      }
    }

    // Scroll back to top for PDF generation
    await page.evaluate(() => window.scrollTo(0, 0));
    await page.waitForTimeout(500);

    // Get the full page height to capture everything in one viewport
    const pageHeight = await page.evaluate(() => {
      return Math.max(
        document.body.scrollHeight,
        document.body.offsetHeight,
        document.documentElement.clientHeight,
        document.documentElement.scrollHeight,
        document.documentElement.offsetHeight
      );
    });

    const pageWidth = options.viewport?.width || 1920;

    // Cap the height at a reasonable maximum (e.g., 50000px) to avoid memory issues
    const maxHeight = 50000;
    const actualHeight = Math.min(pageHeight, maxHeight);

    console.log(
      `📐 Page dimensions: ${pageWidth}x${pageHeight}px (using ${actualHeight}px)`
    );

    // Resize viewport to match the full page height
    await page.setViewportSize({
      width: pageWidth,
      height: actualHeight,
    });

    // Wait for viewport resize to take effect
    await page.waitForTimeout(500);

    console.log(`💾 Generating PDF: ${outputPath}`);

    // Generate PDF with custom width and height to capture the full page
    await page.pdf({
      path: outputPath,
      width: `${pageWidth}px`,
      height: `${actualHeight}px`,
      printBackground: options.pdfOptions?.printBackground ?? true,
      margin: options.pdfOptions?.margin || {
        top: "0px",
        right: "0px",
        bottom: "0px",
        left: "0px",
      },
    });

    console.log(`✅ Successfully created: ${outputPath}`);
  } catch (error) {
    console.error(`❌ Error processing ${url}:`, error.message);
    throw error;
  } finally {
    await browser.close();
  }
}

/**
 * Converts multiple URLs to PDFs
 */
async function convertUrlsToPdfs(
  urls: string[],
  options: ConversionOptions = {}
) {
  const outputDir = options.outputDir || "./pdfs";
  await ensureDir(outputDir);

  console.log(`🚀 Converting ${urls.length} URLs to PDFs...`);
  console.log(`📁 Output directory: ${outputDir}\n`);

  const results: Array<{
    url: string;
    success: boolean;
    skipped?: boolean;
    output?: string;
    error?: string;
  }> = [];

  for (let i = 0; i < urls.length; i++) {
    const url = urls[i];

    try {
      // Generate filename from URL
      const urlObj = new URL(url);
      const hostname = urlObj.hostname.replace(/\./g, "_");
      const pathname = urlObj.pathname
        .replace(/^\/+|\/+$/g, "")
        .replace(/\//g, "_")
        .replace(/[^a-zA-Z0-9_-]/g, "_");

      const filename = `${hostname}${pathname ? "_" + pathname : ""}.pdf`;
      const outputPath = `${outputDir}/${filename}`;

      // Check if file already exists before attempting conversion
      try {
        await Deno.stat(outputPath);
        console.log(`⏭️  Skipping (already exists): ${outputPath}`);
        results.push({
          url,
          success: true,
          skipped: true,
          output: outputPath,
        });
        continue;
      } catch {
        // File doesn't exist, proceed with conversion
      }

      await urlToPdf(url, outputPath, options);

      results.push({
        url,
        success: true,
        skipped: false,
        output: outputPath,
      });
    } catch (error) {
      results.push({
        url,
        success: false,
        skipped: false,
        error: error.message,
      });
    }

    if (i < urls.length - 1) {
      console.log(""); // Empty line between conversions
    }
  }

  // Print summary
  console.log("\n" + "=".repeat(60));
  console.log("📊 Conversion Summary");
  console.log("=".repeat(60));

  const successful = results.filter((r) => r.success && !r.skipped).length;
  const skipped = results.filter((r) => r.skipped).length;
  const failed = results.filter((r) => !r.success).length;

  console.log(`✅ Successful: ${successful}`);
  console.log(`⏭️  Skipped: ${skipped}`);
  console.log(`❌ Failed: ${failed}`);
  console.log(`📝 Total: ${results.length}`);

  if (failed > 0) {
    console.log("\nFailed URLs:");
    results
      .filter((r) => !r.success)
      .forEach((r) => {
        console.log(`  - ${r.url}: ${r.error}`);
      });
  }

  return results;
}

/**
 * Main CLI handler
 */
async function main() {
  const args = Deno.args;

  if (args.length === 0 || args.includes("--help") || args.includes("-h")) {
    console.log(`
Usage: deno run --allow-all url-to-pdf.ts [OPTIONS] <urls...>

Convert URLs to PDFs with fully rendered images, charts, etc.
The script automatically captures the full page height to minimize PDF pages.

Options:
  --output-dir, -o <dir>    Output directory (default: ./pdfs)
  --no-scroll               Don't scroll to bottom
  --no-network-idle         Don't wait for network idle
  --wait <ms>               Wait time after scrolling (default: 2000ms)
  --width <px>              Viewport width (default: 1920)
  --help, -h                Show this help message

Note: Page height is automatically calculated to capture the full page.

Examples:
  # Single URL
  deno run --allow-all url-to-pdf.ts https://example.com

  # Multiple URLs
  deno run --allow-all url-to-pdf.ts https://example.com https://another.com

  # With custom options
  deno run --allow-all url-to-pdf.ts --output-dir ./my-pdfs --wait 3000 https://example.com

  # Read URLs from file
  cat urls.txt | xargs deno run --allow-all url-to-pdf.ts
`);
    Deno.exit(0);
  }

  // Parse arguments
  const options: ConversionOptions = {
    outputDir: "./pdfs",
    scrollToBottom: true,
    waitForNetworkIdle: true,
    waitAfterScroll: 2000,
    viewport: { width: 1920, height: 1080 }, // Initial height, will be adjusted to full page
    pdfOptions: {
      printBackground: true,
    },
  };

  const urls: string[] = [];

  for (let i = 0; i < args.length; i++) {
    const arg = args[i];

    if (arg === "--output-dir" || arg === "-o") {
      options.outputDir = args[++i];
    } else if (arg === "--no-scroll") {
      options.scrollToBottom = false;
    } else if (arg === "--no-network-idle") {
      options.waitForNetworkIdle = false;
    } else if (arg === "--wait") {
      options.waitAfterScroll = parseInt(args[++i], 10);
    } else if (arg === "--width") {
      options.viewport!.width = parseInt(args[++i], 10);
    } else if (arg.startsWith("http://") || arg.startsWith("https://")) {
      urls.push(arg);
    } else {
      console.error(`Unknown argument or invalid URL: ${arg}`);
      Deno.exit(1);
    }
  }

  if (urls.length === 0) {
    console.error("Error: No URLs provided");
    Deno.exit(1);
  }

  try {
    await convertUrlsToPdfs(urls, options);
  } catch (error) {
    console.error("Fatal error:", error);
    Deno.exit(1);
  }
}

// Run main if this is the main module
if (import.meta.main) {
  main();
}

// Export functions for use as a library
export { urlToPdf, convertUrlsToPdfs, scrollToBottom };
