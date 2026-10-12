import { useEffect, useRef, useState, useSyncExternalStore } from "react";
import { useRouter } from "next/navigation";
import { guidelinesPath } from "../shared/routes";
import type { useWorkspace } from "./use-workspace";

const desktopQuery = "(min-width: 1100px)";

function subscribe(onChange: () => void) {
  const query = window.matchMedia(desktopQuery);
  query.addEventListener("change", onChange);

  return () => query.removeEventListener("change", onChange);
}

const getDesktop = () => window.matchMedia(desktopQuery).matches;

const getServerDesktop = () => false;

export function useNavigation(workspace: ReturnType<typeof useWorkspace>) {
  const router = useRouter();
  const desktop = useSyncExternalStore(subscribe, getDesktop, getServerDesktop);
  const [desktopOpen, setDesktopOpen] = useState(true);
  const [mobileOpen, setMobileOpen] = useState(false);
  const [searchOpen, setSearchOpen] = useState(false);

  const view: "guidelines" | "chat" = workspace.pathname.endsWith("/guidelines")
    ? "guidelines"
    : "chat";

  const searchInput = useRef<HTMLInputElement>(null);
  const focusSearch = useRef(false);
  useEffect(() => {
    if (desktop) setMobileOpen(false);
  }, [desktop]);
  const open = desktop ? desktopOpen : mobileOpen;

  useEffect(() => {
    if (open && focusSearch.current) {
      searchInput.current?.focus();
      focusSearch.current = false;
    }
  }, [open, searchOpen]);

  return {
    desktop,
    desktopOpen,
    open,
    view,
    guidelinesHref: guidelinesPath(workspace.active?.id),
    showChat: () =>
      router.push(workspace.chatHref(), {
        scroll: false,
        transitionTypes: ["workspace-navigation"],
      }),
    setOpen: desktop ? setDesktopOpen : setMobileOpen,
    closeOnSelect: () => {
      setMobileOpen(false);
    },
    searchInput,
    searchOpen,
    closeSearch: () => setSearchOpen(false),
    openSearch: () => {
      setSearchOpen(true);

      if (open && searchInput.current) searchInput.current.focus();
      else {
        focusSearch.current = true;
        (desktop ? setDesktopOpen : setMobileOpen)(true);
      }
    },
  };
}
