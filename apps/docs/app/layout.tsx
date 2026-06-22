import type { Metadata, Viewport } from "next";
import type { ReactNode } from "react";

import { brandAssets } from "@chartcoach/brand";
import "@chartcoach/brand/fonts.css";
import { Provider } from "@/components/provider";
import { docsOrigin } from "@/lib/shared";

import "./global.css";

export const metadata: Metadata = {
  metadataBase: new URL(docsOrigin),
  title: {
    default: "chartcoach docs",
    template: "%s | chartcoach docs",
  },
  description: "Documentation for chartcoach and the Guideline Catalog.",
  icons: {
    icon: [
      { url: brandAssets.favicon, type: "image/svg+xml" },
      { url: brandAssets.faviconPng, type: "image/png", sizes: "32x32" },
    ],
    shortcut: [{ url: brandAssets.favicon, type: "image/svg+xml" }],
    apple: [{ url: brandAssets.appleTouchIcon, sizes: "180x180" }],
  },
};

export const viewport: Viewport = {
  colorScheme: "light dark",
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#ffffff" },
    { media: "(prefers-color-scheme: dark)", color: "#000000" },
  ],
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className="flex min-h-screen flex-col">
        <Provider>{children}</Provider>
      </body>
    </html>
  );
}
