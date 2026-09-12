import type { Metadata, Viewport } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import type { ReactNode } from "react";
import * as stylex from "@stylexjs/stylex";
import { colors } from "../components/ui/tokens.stylex";
import favicon from "@chartcoach/brand/assets/brand/favicon.svg";
import faviconPng from "@chartcoach/brand/assets/brand/favicon.png";
import appleTouchIcon from "@chartcoach/brand/assets/brand/app-icon-light.png";
import "./stylex.css";
import "./transitions.css";

const sans = Geist({ subsets: ["latin"], variable: "--font-geist" });

const mono = Geist_Mono({ subsets: ["latin"], variable: "--font-geist-mono" });

const styles = stylex.create({
  body: {
    backgroundColor: colors.background,
    color: colors.foreground,
    fontFamily: "var(--font-geist), Arial, Helvetica, sans-serif",
    lineHeight: 1.5,
  },
});

export const viewport: Viewport = {
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#ffffff" },
    { media: "(prefers-color-scheme: dark)", color: "#111113" },
  ],
};

export const metadata: Metadata = {
  title: "ChartCoach",
  description: "Discuss your chart with an agent that cites visualization guidance.",
  icons: {
    icon: [
      { url: favicon.src, type: "image/svg+xml" },
      { url: faviconPng.src, type: "image/png", sizes: `${faviconPng.width}x${faviconPng.height}` },
    ],
    shortcut: [{ url: favicon.src, type: "image/svg+xml" }],
    apple: [{ url: appleTouchIcon.src, sizes: `${appleTouchIcon.width}x${appleTouchIcon.height}` }],
  },
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en" className={`${sans.variable} ${mono.variable}`}>
      <body {...stylex.props(styles.body)}>{children}</body>
    </html>
  );
}
