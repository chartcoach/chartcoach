import { Moon, Sun } from "lucide-react";
import { useEffect, useSyncExternalStore } from "react";

const STORAGE_KEY = "chartcoach-theme";
const THEME_CHANGE_EVENT = "chartcoach-theme-change";

type Theme = "light" | "dark";
type ThemeSnapshot = Theme | null;
type ThemeToggleProps = {
  variant?: "icon" | "menu";
};

function getPreferredTheme(): Theme {
  const stored = localStorage.getItem(STORAGE_KEY);
  if (stored === "light" || stored === "dark") return stored;
  return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
}

function applyTheme(theme: Theme) {
  document.documentElement.classList.toggle("dark", theme === "dark");
  document.documentElement.style.colorScheme = theme;
}

function getThemeSnapshot(): ThemeSnapshot {
  if (typeof window === "undefined") return null;
  return getPreferredTheme();
}

function getServerThemeSnapshot(): ThemeSnapshot {
  return null;
}

function subscribeTheme(onStoreChange: () => void) {
  const media = window.matchMedia("(prefers-color-scheme: dark)");
  media.addEventListener("change", onStoreChange);
  window.addEventListener("storage", onStoreChange);
  window.addEventListener(THEME_CHANGE_EVENT, onStoreChange);

  return () => {
    media.removeEventListener("change", onStoreChange);
    window.removeEventListener("storage", onStoreChange);
    window.removeEventListener(THEME_CHANGE_EVENT, onStoreChange);
  };
}

export function ThemeToggle({ variant = "icon" }: ThemeToggleProps) {
  const theme = useSyncExternalStore(subscribeTheme, getThemeSnapshot, getServerThemeSnapshot);
  const visibleTheme = theme ?? "light";

  useEffect(() => {
    if (theme) applyTheme(theme);
  }, [theme]);

  const isDark = visibleTheme === "dark";
  const label = isDark ? "Switch to light mode" : "Switch to dark mode";
  const Icon = isDark ? Sun : Moon;

  function toggleTheme() {
    const next = isDark ? "light" : "dark";
    localStorage.setItem(STORAGE_KEY, next);
    applyTheme(next);
    window.dispatchEvent(new Event(THEME_CHANGE_EVENT));
  }

  if (variant === "menu") {
    return (
      <button
        type="button"
        onClick={toggleTheme}
        className="group flex min-h-14 w-full cursor-pointer items-center justify-between gap-3 rounded-xl px-3 py-2.5 text-left text-muted transition-colors hover:bg-bg/70 hover:text-fg focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-fg/20"
        aria-label={label}
        title={label}
      >
        <span className="flex min-w-0 items-center gap-3">
          <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg border border-border bg-bg text-muted transition-colors group-hover:text-fg">
            <Icon className="h-4 w-4" aria-hidden="true" />
          </span>
          <span className="grid min-w-0 gap-0.5">
            <span className="text-[0.9375rem] font-medium leading-5 text-fg">Appearance</span>
            <span className="truncate text-[0.8125rem] leading-5 text-muted">
              {isDark ? "Dark mode" : "Light mode"}
            </span>
          </span>
        </span>
        <span className="rounded-full border border-border bg-bg px-2.5 py-1 text-[0.6875rem] font-semibold uppercase leading-none tracking-[0.14em] text-muted transition-colors group-hover:text-fg">
          Switch
        </span>
      </button>
    );
  }

  return (
    <button
      type="button"
      onClick={toggleTheme}
      className="relative flex h-8 w-8 cursor-pointer items-center justify-center rounded-md text-muted transition-colors hover:bg-surface-muted hover:text-fg"
      aria-label={label}
      title={label}
    >
      <Icon className="h-4 w-4" aria-hidden="true" />
    </button>
  );
}
