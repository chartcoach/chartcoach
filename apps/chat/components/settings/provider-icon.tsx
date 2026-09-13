import Anthropic from "@lobehub/icons/es/Anthropic/components/Mono.js";
import OpenAI from "@lobehub/icons/es/OpenAI/components/Mono.js";
import Gemini from "@lobehub/icons/es/Gemini/components/Mono.js";
import { Plug } from "lucide-react";
import * as stylex from "@stylexjs/stylex";
import { ui } from "../ui/ui";
import type { Provider } from "../../shared/model";

export function ProviderIcon({ provider, size = 20 }: { provider: Provider; size?: number }) {
  switch (provider) {
    case "anthropic":
      return <Anthropic size={size} aria-hidden="true" />;
    case "openai":
      return <OpenAI size={size} aria-hidden="true" />;
    case "google":
      return <Gemini size={size} aria-hidden="true" />;
    case "compatible":
      return <Plug {...stylex.props(ui.icon)} size={size} aria-hidden="true" />;
  }
}
