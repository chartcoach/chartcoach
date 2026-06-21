import type { Metadata } from "next";
import type { ReactNode } from "react";

import { brandAssets } from "@chartcoach/brand";
import "@chartcoach/brand/fonts.css";
import { Provider } from "@/components/provider";

import "./global.css";

export const metadata: Metadata = {
  title: {
    default: "chartcoach docs",
    template: "%s | chartcoach docs",
  },
  description: "Documentation for chartcoach and the Guideline Catalog.",
  icons: {
    icon: brandAssets.favicon,
    shortcut: brandAssets.favicon,
    apple: brandAssets.appleTouchIcon,
  },
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
