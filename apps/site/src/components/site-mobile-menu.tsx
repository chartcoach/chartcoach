import githubIconUrl from "@/assets/icons/github.svg?url";
import { ExternalLink, X } from "lucide-react";
import { useEffect, useId, useRef, useState, useSyncExternalStore } from "react";

import { ThemeToggle } from "@/components/theme-toggle";
import { isExternalHttpHref, normalizePathname } from "@/lib/routes";

type MobileMenuLink = {
  label: string;
  href: string;
};

type SiteMobileMenuProps = {
  links: readonly MobileMenuLink[];
  githubHref: string;
};

const githubIconStyle = {
  mask: `url("${githubIconUrl}") center / contain no-repeat`,
  WebkitMask: `url("${githubIconUrl}") center / contain no-repeat`,
};

function classNames(...values: Array<string | false | null | undefined>) {
  return values.filter(Boolean).join(" ");
}

function isActiveHref(href: string, pathname: string) {
  if (isExternalHttpHref(href)) return false;

  return normalizePathname(pathname) === normalizePathname(href);
}

function subscribePathname(onChange: () => void) {
  window.addEventListener("popstate", onChange);

  return () => window.removeEventListener("popstate", onChange);
}

function getPathnameSnapshot() {
  return window.location.pathname;
}

function getServerPathnameSnapshot() {
  return "";
}

export function SiteMobileMenu({ links, githubHref }: SiteMobileMenuProps) {
  const [open, setOpen] = useState(false);

  const pathname = useSyncExternalStore(
    subscribePathname,
    getPathnameSnapshot,
    getServerPathnameSnapshot,
  );

  const menuId = useId();
  const dialogRef = useRef<HTMLDialogElement>(null);
  const triggerRef = useRef<HTMLButtonElement>(null);

  useEffect(() => {
    const dialog = dialogRef.current;

    if (!dialog) return;

    if (!open) {
      dialog.close();

      return;
    }

    dialog.showModal();
    const previousOverflow = document.body.style.overflow;
    const desktop = window.matchMedia("(min-width: 768px)");
    const close = () => setOpen(false);

    const closeOnDesktop = () => {
      if (desktop.matches) close();
    };

    closeOnDesktop();
    desktop.addEventListener("change", closeOnDesktop);
    document.addEventListener("astro:before-preparation", close);
    document.body.style.overflow = "hidden";

    return () => {
      desktop.removeEventListener("change", closeOnDesktop);
      document.removeEventListener("astro:before-preparation", close);
      document.body.style.overflow = previousOverflow;
    };
  }, [open]);

  return (
    <>
      <button
        ref={triggerRef}
        type="button"
        className="relative flex h-11 w-11 shrink-0 cursor-pointer items-center justify-center rounded-md border border-border text-fg transition-colors hover:bg-surface-muted focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-fg/20 md:hidden"
        aria-label={open ? "Close menu" : "Open menu"}
        aria-expanded={open}
        aria-haspopup="dialog"
        aria-controls={open ? menuId : undefined}
        onClick={() => setOpen((current) => !current)}
      >
        <span className="flex flex-col items-center justify-center gap-[5px]" aria-hidden="true">
          <span
            className={classNames(
              "block h-[1.5px] w-3.5 rounded-full bg-current transition-transform duration-150",
              open && "translate-y-[3.25px] rotate-45",
            )}
          />
          <span
            className={classNames(
              "block h-[1.5px] w-3.5 rounded-full bg-current transition-transform duration-150",
              open && "-translate-y-[3.25px] -rotate-45",
            )}
          />
        </span>
      </button>

      <dialog
        ref={dialogRef}
        id={menuId}
        aria-label="Site navigation"
        onClose={() => {
          setOpen(false);
          triggerRef.current?.focus({ preventScroll: true });
        }}
        className="site-mobile-dialog fixed inset-0 m-0 h-dvh max-h-none w-full max-w-none overflow-y-auto border-0 bg-bg p-5 text-fg"
      >
        <div className="mb-5 flex items-center justify-between gap-4">
          <span className="text-base font-medium">Navigation</span>
          <button
            type="button"
            className="flex size-11 items-center justify-center rounded-md border border-border"
            aria-label="Close menu"
            onClick={() => setOpen(false)}
          >
            <X className="size-4" aria-hidden="true" />
          </button>
        </div>
        <div className="mx-auto grid w-full max-w-[28rem] gap-3">
          <nav
            className="rounded-2xl border border-border bg-surface-muted/50 p-1 shadow-[0_16px_48px_color-mix(in_srgb,var(--color-fg)_8%,transparent)]"
            aria-label="Mobile primary"
          >
            <ul className="m-0 grid list-none gap-1 p-0">
              {links.map((link) => {
                const external = isExternalHttpHref(link.href);
                const active = isActiveHref(link.href, pathname);

                return (
                  <li key={link.href}>
                    <a
                      href={link.href}
                      target={external ? "_blank" : undefined}
                      rel={external ? "noreferrer" : undefined}
                      aria-current={active ? "page" : undefined}
                      className={classNames(
                        "flex min-h-12 items-center justify-between rounded-xl px-3 text-[0.9375rem] font-medium no-underline transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-fg/20",
                        active
                          ? "bg-bg text-fg shadow-[0_1px_0_color-mix(in_srgb,var(--color-fg)_8%,transparent)]"
                          : "text-muted hover:bg-bg/70 hover:text-fg",
                      )}
                      onClick={() => setOpen(false)}
                    >
                      <span>{link.label}</span>
                      {external ? (
                        <ExternalLink aria-hidden="true" className="h-4 w-4 shrink-0" />
                      ) : null}
                    </a>
                  </li>
                );
              })}
            </ul>
          </nav>

          <div className="rounded-2xl border border-border bg-surface-muted/50 p-1 shadow-[0_16px_48px_color-mix(in_srgb,var(--color-fg)_8%,transparent)]">
            <a
              href={githubHref}
              target="_blank"
              rel="noreferrer"
              className="group flex min-h-14 items-center justify-between gap-3 rounded-xl px-3 py-2.5 text-muted no-underline transition-colors hover:bg-bg/70 hover:text-fg focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-fg/20"
              aria-label="chartcoach catalog repository on GitHub"
              onClick={() => setOpen(false)}
            >
              <span className="flex min-w-0 items-center gap-3">
                <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg border border-border bg-bg text-muted transition-colors group-hover:text-fg">
                  <span
                    className="h-[1.0625rem] w-[1.0625rem] bg-current"
                    style={githubIconStyle}
                    aria-hidden="true"
                  />
                </span>
                <span className="grid min-w-0 gap-0.5">
                  <span className="text-[0.9375rem] font-medium leading-5 text-fg">GitHub</span>
                  <span className="truncate text-[0.8125rem] leading-5 text-muted">
                    Catalog repository
                  </span>
                </span>
              </span>
              <ExternalLink aria-hidden="true" className="h-4 w-4 shrink-0" />
            </a>
            <ThemeToggle variant="menu" />
          </div>
        </div>
      </dialog>
    </>
  );
}
