import Anthropic from "@lobehub/icons/es/Anthropic/components/Mono.js";
import OpenAI from "@lobehub/icons/es/OpenAI/components/Mono.js";
import Gemini from "@lobehub/icons/es/Gemini/components/Mono.js";
import Fireworks from "@lobehub/icons/es/Fireworks/components/Mono.js";
import Groq from "@lobehub/icons/es/Groq/components/Mono.js";
import HuggingFace from "@lobehub/icons/es/HuggingFace/components/Mono.js";
import Mistral from "@lobehub/icons/es/Mistral/components/Mono.js";
import Nvidia from "@lobehub/icons/es/Nvidia/components/Mono.js";
import OpenRouter from "@lobehub/icons/es/OpenRouter/components/Mono.js";
import Together from "@lobehub/icons/es/Together/components/Mono.js";
import Vercel from "@lobehub/icons/es/Vercel/components/Mono.js";
import XAI from "@lobehub/icons/es/XAI/components/Mono.js";
import { Plug } from "lucide-react";
import * as stylex from "@stylexjs/stylex";
import { ui } from "../ui/ui";
import {
  compatibleProviderPreset,
  type CompatibleProviderId,
  type Provider,
} from "../../shared/model";

export function CompatibleProviderIcon({
  provider,
  size = 20,
}: {
  provider: CompatibleProviderId;
  size?: number;
}) {
  const props = { size, "aria-hidden": true } as const;

  switch (provider) {
    case "openrouter":
      return <OpenRouter {...props} />;
    case "xai":
      return <XAI {...props} />;
    case "gemini":
      return <Gemini {...props} />;
    case "togetherai":
      return <Together {...props} />;
    case "fireworksai":
      return <Fireworks {...props} />;
    case "groq":
      return <Groq {...props} />;
    case "huggingface":
      return <HuggingFace {...props} />;
    case "mistral":
      return <Mistral {...props} />;
    case "nvidia":
      return <Nvidia {...props} />;
    case "vercelaigateway":
      return <Vercel {...props} />;
  }
}

export function ProviderIcon({
  provider,
  baseURL,
  size = 20,
}: {
  provider: Provider;
  baseURL?: string;
  size?: number;
}) {
  switch (provider) {
    case "anthropic":
      return <Anthropic size={size} aria-hidden="true" />;
    case "openai":
      return <OpenAI size={size} aria-hidden="true" />;
    case "google":
      return <Gemini size={size} aria-hidden="true" />;
    case "compatible":
      const preset = compatibleProviderPreset(baseURL);

      if (preset) return <CompatibleProviderIcon provider={preset.id} size={size} />;

      return <Plug {...stylex.props(ui.icon)} size={size} aria-hidden="true" />;
  }
}
