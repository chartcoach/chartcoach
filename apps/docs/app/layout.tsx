import type { Metadata, Viewport } from "next";
import type { ReactNode } from "react";

import appleTouchIcon from "@chartcoach/brand/assets/brand/app-icon-light.png";
import faviconPng from "@chartcoach/brand/assets/brand/favicon.png";
import favicon from "@chartcoach/brand/assets/brand/favicon.svg";
import "@chartcoach/brand/fonts.css";
import { Provider } from "@/components/provider";
import { docsOrigin, isPreviewDeployment } from "@/lib/shared";

import "./global.css";

export const metadata: Metadata = {
  metadataBase: new URL(docsOrigin),
  title: {
    default: "chartcoach",
    template: "%s | chartcoach",
  },
  description: "Find, inspect, query, and cite source-traced visualization guidelines.",
  robots: isPreviewDeployment()
    ? {
        index: false,
        follow: false,
        nocache: true,
        googleBot: {
          index: false,
          follow: false,
          noimageindex: true,
        },
      }
    : {
        index: true,
        follow: true,
      },
  icons: {
    icon: [
      { url: favicon.src, type: "image/svg+xml" },
      { url: faviconPng.src, type: "image/png", sizes: "32x32" },
    ],
    shortcut: [{ url: favicon.src, type: "image/svg+xml" }],
    apple: [{ url: appleTouchIcon.src, sizes: "180x180" }],
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
