import { Moon, Sun } from "lucide-react";
import { useEffect, useState } from "react";

const STORAGE_KEY = "chartcoach-theme";

type Theme = "light" | "dark";

function getPreferredTheme(): Theme {
  const stored = localStorage.getItem(STORAGE_KEY);
  if (stored === "light" || stored === "dark") return stored;
  return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
}

function applyTheme(theme: Theme) {
  document.documentElement.classList.toggle("dark", theme === "dark");
  document.documentElement.style.colorScheme = theme;
}

export function ThemeToggle() {
  const [theme, setTheme] = useState<Theme | null>(null);

  useEffect(() => {
    const preferred = getPreferredTheme();
    applyTheme(preferred);
    setTheme(preferred);
  }, []);

  if (!theme) {
    return <div className="h-8 w-8" aria-hidden="true" />;
  }

  const isDark = theme === "dark";

  return (
    <button
      type="button"
      onClick={() => {
        const next = isDark ? "light" : "dark";
        localStorage.setItem(STORAGE_KEY, next);
        applyTheme(next);
        setTheme(next);
      }}
      className="relative flex h-8 w-8 cursor-pointer items-center justify-center rounded-md text-muted transition-colors hover:bg-surface-muted hover:text-fg"
      aria-label="Toggle theme"
      title="Toggle theme"
    >
      {isDark ? (
        <Sun className="h-4 w-4" aria-hidden="true" />
      ) : (
        <Moon className="h-4 w-4" aria-hidden="true" />
      )}
    </button>
  );
}
