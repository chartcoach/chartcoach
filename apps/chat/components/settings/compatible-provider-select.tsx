import { Select } from "radix-ui";
import { Check, ChevronDown, Plug } from "lucide-react";
import * as stylex from "@stylexjs/stylex";
import type { useConnectionForm } from "../../chat/use-connection-form";
import { compatibleProviderPresets } from "../../shared/model";
import { styles } from "./styles";
import { ui } from "../ui/ui";
import { CompatibleProviderIcon } from "./provider-icon";

export function CompatibleProviderSelect({
  form,
  id,
  origins,
}: {
  form: ReturnType<typeof useConnectionForm>;
  id: string;
  origins: string[];
}) {
  const allowedOrigins = new Set(origins);

  const providers = compatibleProviderPresets.filter(
    ({ baseURL }) =>
      allowedOrigins.has(new URL(baseURL).origin) || form.compatibleProvider?.baseURL === baseURL,
  );

  return (
    <div {...stylex.props(styles.field)}>
      <span id={`${id}-compatible-provider`} {...stylex.props(styles.label)}>
        Compatible provider
      </span>
      <Select.Root
        value={form.compatibleProvider?.id ?? "custom"}
        onValueChange={form.changeCompatibleProvider}
      >
        <Select.Trigger
          {...stylex.props(styles.input, styles.providerSelect, ui.focus)}
          aria-labelledby={`${id}-compatible-provider`}
        >
          <span {...stylex.props(styles.providerSelectValue)}>
            {form.compatibleProvider ? (
              <>
                <CompatibleProviderIcon provider={form.compatibleProvider.id} />
                {form.compatibleProvider.name}
              </>
            ) : (
              <>
                <Plug size={20} aria-hidden="true" />
                Custom endpoint
              </>
            )}
          </span>
          <Select.Icon asChild>
            <ChevronDown {...stylex.props(ui.icon)} size={16} aria-hidden="true" />
          </Select.Icon>
        </Select.Trigger>
        <Select.Portal>
          <Select.Content
            {...stylex.props(styles.providerSelectContent)}
            position="popper"
            sideOffset={4}
          >
            <Select.Viewport {...stylex.props(styles.providerSelectViewport)}>
              {providers.map((provider) => (
                <Select.Item
                  key={provider.id}
                  value={provider.id}
                  textValue={provider.name}
                  {...stylex.props(styles.providerSelectItem)}
                >
                  <CompatibleProviderIcon provider={provider.id} />
                  <Select.ItemText>{provider.name}</Select.ItemText>
                  <Select.ItemIndicator {...stylex.props(styles.providerSelectIndicator)}>
                    <Check size={15} aria-hidden="true" />
                  </Select.ItemIndicator>
                </Select.Item>
              ))}
              <Select.Item
                value="custom"
                textValue="Custom endpoint"
                {...stylex.props(styles.providerSelectItem)}
              >
                <Plug size={20} aria-hidden="true" />
                <Select.ItemText>Custom endpoint</Select.ItemText>
                <Select.ItemIndicator {...stylex.props(styles.providerSelectIndicator)}>
                  <Check size={15} aria-hidden="true" />
                </Select.ItemIndicator>
              </Select.Item>
            </Select.Viewport>
          </Select.Content>
        </Select.Portal>
      </Select.Root>
      <span {...stylex.props(styles.hint)}>Choose a preset or enter another allowed URL.</span>
    </div>
  );
}
