import type { Metadata } from "next";
import type { ReactNode } from "react";

import { Provider } from "@/components/provider";

import "./global.css";

export const metadata: Metadata = {
  title: {
    default: "ChartCoach Docs",
    template: "%s | ChartCoach Docs",
  },
  description: "Documentation for ChartCoach and the Guideline Catalog.",
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
