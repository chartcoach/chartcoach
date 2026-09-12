import { ThreadListPrimitive } from "@assistant-ui/react";
import { PanelLeft, Search, SquarePen } from "lucide-react";
import Image from "next/image";
import logo from "@chartcoach/brand/assets/brand/chartcoach-horizontal.svg";
import logoWhite from "@chartcoach/brand/assets/brand/chartcoach-horizontal-white.svg";
import * as stylex from "@stylexjs/stylex";
import type { useNavigation } from "../../chat/use-navigation";
import { media } from "../ui/tokens.stylex";
import { ui } from "../ui/ui";

export function NavigationHeader({
  navigation,
  disabled,
}: {
  navigation: ReturnType<typeof useNavigation>;
  disabled: boolean;
}) {
  const compact = navigation.desktop && !navigation.open;

  const brand = (
    <span {...stylex.props(styles.brand, compact && styles.mark)}>
      <Image
        src={logo}
        alt={compact ? "" : "chartcoach"}
        width={128}
        height={32}
        unoptimized
        {...stylex.props(styles.logoLight)}
      />
      <Image
        src={logoWhite}
        alt={compact ? "" : "chartcoach"}
        width={128}
        height={32}
        unoptimized
        {...stylex.props(styles.logoDark)}
      />
    </span>
  );

  const toggle = (
    <button
      type="button"
      {...stylex.props(ui.button, ui.quietButton, ui.focus, styles.action)}
      aria-label={navigation.open ? "Close sidebar" : "Open sidebar"}
      title={navigation.open ? "Close sidebar" : "Open sidebar"}
      aria-expanded={navigation.open}
      aria-controls={navigation.desktop ? "conversation-sidebar" : "conversation-drawer"}
      onClick={() => navigation.setOpen(!navigation.open)}
    >
      <PanelLeft size={18} />
    </button>
  );

  return (
    <div {...stylex.props(styles.root, !navigation.desktopOpen && styles.collapsed)}>
      {compact ? (
        <button
          type="button"
          {...stylex.props(ui.button, ui.quietButton, ui.focus, styles.markButton)}
          aria-label="Open sidebar"
          title="Open sidebar"
          aria-expanded={false}
          aria-controls="conversation-sidebar"
          onClick={() => navigation.setOpen(true)}
        >
          {brand}
        </button>
      ) : (
        <>
          {!navigation.desktop ? toggle : null}
          <a
            {...stylex.props(ui.focus, styles.brandLink)}
            href="https://chartcoach.dev"
            target="_blank"
            rel="noreferrer"
          >
            {brand}
          </a>
          {navigation.desktop ? (
            <>
              <button
                type="button"
                {...stylex.props(ui.button, ui.quietButton, ui.focus, styles.action)}
                aria-label="Search conversations"
                title="Search conversations"
                onClick={navigation.openSearch}
              >
                <Search size={18} />
              </button>
              {toggle}
            </>
          ) : (
            <ThreadListPrimitive.New
              {...stylex.props(ui.button, ui.quietButton, ui.focus)}
              disabled={disabled}
              aria-label="New chat"
              title="New chat"
              onClick={navigation.closeOnSelect}
            >
              <SquarePen size={18} />
            </ThreadListPrimitive.New>
          )}
        </>
      )}
    </div>
  );
}

const styles = stylex.create({
  root: {
    display: "flex",
    alignItems: "center",
    gap: 4,
    minWidth: 0,
    width: { default: "auto", [media.navigationDesktop]: 256 },
    paddingInline: { default: 16, [media.navigationDesktop]: 12 },
    flexShrink: 0,
  },
  collapsed: {
    width: { default: null, [media.navigationDesktop]: 64 },
    justifyContent: { default: null, [media.navigationDesktop]: "center" },
  },
  brandLink: {
    display: "flex",
    flexShrink: 0,
    marginRight: { default: 0, [media.navigationDesktop]: "auto" },
    borderRadius: 4,
  },
  brand: { display: "block", flexShrink: 0, width: 128, height: 32 },
  mark: { width: 30, overflow: "hidden" },
  logoLight: {
    display: { default: "block", [media.dark]: "none" },
    width: 128,
    height: 32,
    maxWidth: "none",
  },
  logoDark: {
    display: { default: "none", [media.dark]: "block" },
    width: 128,
    height: 32,
    maxWidth: "none",
  },
  action: {
    width: { default: 44, [media.navigationDesktop]: 36 },
    minWidth: { default: 44, [media.navigationDesktop]: 36 },
  },
  markButton: { padding: 6, flexShrink: 0 },
});
