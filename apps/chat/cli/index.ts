#!/usr/bin/env node
import { z } from "zod";
import { Command, Option, CommanderError, InvalidArgumentError } from "@commander-js/extra-typings";
import { launchProviderSchema, modelAuth } from "../shared/model";
import { configSchema } from "../runtime/schema";
import { fileURLToPath } from "node:url";
import { readFile } from "node:fs/promises";
import { ConfigurationError, loadConfig } from "../runtime/config";
import { loadEnvironmentFile } from "../runtime/dotenv";
import { startChat } from "../runtime/start";
import { chalkStderr } from "chalk";
import { renderLoading, renderReady, renderStopped, renderStopping } from "./output";

const distribution = fileURLToPath(new URL("../", import.meta.url));

const { version } = z
  .object({ version: z.string() })
  .parse(JSON.parse(await readFile(new URL("../package.json", import.meta.url), "utf8")));

function integer(value: string) {
  if (!/^\d+$/.test(value)) throw new InvalidArgumentError("Enter a whole number.");

  return Number(value);
}

function fileOptions(command: Command) {
  return command
    .optionsGroup("Configuration:")
    .option("--config <file>", "JSON settings file (env: CHARTCOACH_CONFIG)")
    .option(
      "--env-file <file>",
      "dotenv file overriding inherited values (env: CHARTCOACH_ENV_FILE)",
    );
}

function chatOptions(command: Command) {
  return fileOptions(command)
    .optionsGroup("Model connection:")
    .addOption(
      new Option(
        "--provider <name>",
        "text adapter or hosted preset (env: CHARTCOACH_TEXT_PROVIDER, default: openai)",
      ).choices(launchProviderSchema.options),
    )
    .option("--model <id>", "image and tool-capable model (env: CHARTCOACH_TEXT_MODEL)")
    .option("--base-url <url>", "custom OpenAI-compatible endpoint (env: CHARTCOACH_TEXT_BASE_URL)")
    .addOption(
      new Option(
        "--model-auth <mode>",
        "authentication (env: CHARTCOACH_TEXT_AUTH, default: api-key)",
      ).choices(modelAuth.options),
    )
    .optionsGroup("Catalog and storage:")
    .option(
      "--catalog <location>",
      "catalog release or selection (env: CHARTCOACH_CATALOG, default: official catalog)",
    )
    .option(
      "--data-dir <directory>",
      "conversations and encrypted credentials (env: CHARTCOACH_DATA_DIR)",
    )
    .optionsGroup("Server:")
    .addOption(
      new Option("--host <address>", "listener (env: CHARTCOACH_HOST, default: 127.0.0.1)").choices(
        configSchema.shape.server.unwrap().shape.host.unwrap().options,
      ),
    )
    .option(
      "--port <number>",
      "listener port, 0 selects a free port (env: CHARTCOACH_PORT, default: 4273)",
      integer,
    )
    .option("--public-url <origin>", "reverse proxy origin (env: CHARTCOACH_PUBLIC_URL)")
    .option("--password-file <file>", "server password mount (env: CHARTCOACH_PASSWORD_FILE)")
    .option("--public", "serve without sign-in on a network listener (env: CHARTCOACH_PUBLIC)")
    .option(
      "--no-open",
      "print the URL without opening a browser (env: CHARTCOACH_OPEN)",
      undefined,
    )
    .optionsGroup("Diagnostics:")
    .option(
      "--tracing",
      "enable Langfuse with LANGFUSE_PUBLIC_KEY and LANGFUSE_SECRET_KEY (env: CHARTCOACH_TRACING)",
    )
    .option("--verbose", "print worker diagnostics")
    .addHelpText(
      "after",
      `
Examples:
  chartcoach chat --env-file ./chat.env
  chartcoach chat --provider openrouter --model <vision-model>
  chartcoach chat --provider compatible --base-url http://127.0.0.1:1234/v1 --model <vision-model> --model-auth none

Set CHARTCOACH_TEXT_API_KEY in your environment or env file.
Hosted presets supply their API URL. "compatible" means a custom endpoint
implementing the OpenAI Chat Completions protocol and requires --base-url.

Settings: flags > explicit env file > inherited environment > default .env > JSON > defaults.
With no file selection, .env is read from the working directory.
Advanced settings (context limits, embeddings, guideline URL templates, allowed
origins, cache, and tracing metadata): https://docs.chartcoach.dev/chat
`,
    );
}

type SettingsOptions = Partial<ReturnType<ReturnType<typeof chatOptions>["opts"]>>;

function configuration(values: SettingsOptions, explicitOpen = false) {
  loadEnvironmentFile(values.envFile);

  return loadConfig({
    configFile: values.config,
    overrides: {
      catalog: { source: values.catalog },
      tracing: values.tracing,
      model: {
        provider: values.provider,
        model: values.model,
        baseURL: values.baseUrl,
        auth: values.modelAuth,
      },
      server: {
        host: values.host,
        port: values.port,
        publicURL: values.publicUrl,
        open: explicitOpen ? values.open : undefined,
        passwordFile: values.passwordFile,
        public: values.public,
      },
      storage: { dataDir: values.dataDir },
    },
  });
}

const program = new Command()
  .name("chartcoach")
  .description("Run ChartCoach locally for source-traced visualization design guidance.")
  .version(version)
  .addHelpText(
    "after",
    `
Start: chartcoach chat --env-file ./chat.env
Check: chartcoach doctor --env-file ./chat.env --json
Run chartcoach chat --help for launch settings and provider presets.
`,
  )
  .showHelpAfterError()
  .showSuggestionAfterError()
  .exitOverride();

chatOptions(program.command("chat", { isDefault: true }).description("Start the chat app")).action(
  async (_options, command) => {
    const config = configuration(command.opts(), command.getOptionValueSource("open") === "cli");
    const controller = new AbortController();

    const stop = () => {
      if (controller.signal.aborted) return;
      process.stderr.write(renderStopping());
      controller.abort();
    };

    process.on("SIGINT", stop);
    process.on("SIGTERM", stop);

    try {
      process.stderr.write(renderLoading());

      await using app = await startChat(config, {
        distribution,
        signal: controller.signal,
        verbose: command.opts().verbose,
        log: (message) => process.stderr.write(`${message}\n`),
      });

      process.stderr.write(
        renderReady({
          url: app.url,
          catalog: app.catalog,
          model: config.model.model,
          dataDir: app.dataDir,
        }),
      );

      if (config.server.open && process.stdout.isTTY) {
        const { default: open } = await import("open");
        await open(app.url).catch(() =>
          process.stderr.write(
            `${chalkStderr.yellow("!")} Open ${chalkStderr.cyan.underline(app.url)} in your browser.\n`,
          ),
        );
      }

      await app.wait();
    } catch (error) {
      if (error !== controller.signal.reason) throw error;
    } finally {
      process.off("SIGINT", stop);
      process.off("SIGTERM", stop);
    }

    if (controller.signal.aborted) process.stderr.write(renderStopped());
  },
);

fileOptions(
  program
    .command("doctor")
    .description("Check launch files, credentials, catalog, and native runtime"),
)
  .option("--json", "print a JSON diagnostic report")
  .action(async (_options, command) => {
    try {
      const config = configuration(command.opts());
      const { diagnose } = await import("../runtime/diagnostics");
      const report = await diagnose(config, version);
      process.stdout.write(
        command.opts().json
          ? `${JSON.stringify(report)}\n`
          : `ChartCoach ${version}\nCatalog: ${report.catalog.guidelines} guidelines (${report.catalog.digest ?? "local bundle"})\nData: ${config.storage.dataDir}\nModel: ${config.model.model ?? "Configure in the browser"}\nDuckDB, SQLite, LanceDB, embeddings: available\n`,
      );
    } catch (error) {
      if (!command.opts().json) throw error;
      process.stdout.write(
        `${JSON.stringify({ ok: false, version, error: error instanceof Error ? error.message : "The diagnostic failed." })}\n`,
      );
      process.exitCode = error instanceof ConfigurationError ? 2 : 1;
    }
  });

try {
  await program.parseAsync();
} catch (error) {
  if (error instanceof CommanderError) {
    process.exitCode = error.exitCode === 0 ? 0 : 2;
  } else {
    process.stderr.write(
      `${chalkStderr.red("✗")} ${chalkStderr.bold("chartcoach:")} ${error instanceof Error ? error.message : "The operation failed."}\n`,
    );
    process.exitCode = error instanceof ConfigurationError ? 2 : 1;
  }
}
