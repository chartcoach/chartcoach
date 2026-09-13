import {
  addTransitionType,
  startTransition,
  useEffect,
  useRef,
  useState,
  useSyncExternalStore,
} from "react";

const desktopQuery = "(min-width: 1100px)";

function subscribe(onChange: () => void) {
  const query = window.matchMedia(desktopQuery);
  query.addEventListener("change", onChange);

  return () => query.removeEventListener("change", onChange);
}

const getDesktop = () => window.matchMedia(desktopQuery).matches;

const getServerDesktop = () => false;

export function useNavigation() {
  const desktop = useSyncExternalStore(subscribe, getDesktop, getServerDesktop);
  const [desktopOpen, setDesktopOpen] = useState(true);
  const [mobileOpen, setMobileOpen] = useState(false);
  const [searchOpen, setSearchOpen] = useState(false);
  const [view, setView] = useState<"chat" | "guidelines">("chat");
  const searchInput = useRef<HTMLInputElement>(null);
  const focusSearch = useRef(false);
  useEffect(() => {
    if (desktop) setMobileOpen(false);
  }, [desktop]);
  const open = desktop ? desktopOpen : mobileOpen;

  function showView(next: "chat" | "guidelines") {
    if (view === next) return;
    startTransition(() => {
      addTransitionType("workspace-navigation");
      setView(next);
    });
  }

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
    showGuidelines: () => {
      showView("guidelines");
      setMobileOpen(false);
    },
    showChat: () => showView("chat"),
    setOpen: desktop ? setDesktopOpen : setMobileOpen,
    closeOnSelect: () => {
      setMobileOpen(false);
      showView("chat");
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
