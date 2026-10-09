#!/usr/bin/env node
import { z } from "zod";
import { Command, Option, CommanderError, InvalidArgumentError } from "@commander-js/extra-typings";
import { providerSchema, modelAuth } from "../shared/model";
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

function options(command: Command) {
  return command
    .option("--config <file>", "read a JSON configuration file")
    .option("--env-file <file>", "load dotenv settings (default: .env in the working directory)")
    .option(
      "--catalog <location>",
      "catalog release directory, release.json URL, or catalog.json URL",
    )
    .option("--catalog-profile <name>", "catalog index profile")
    .addOption(new Option("--provider <name>", "model provider").choices(providerSchema.options))
    .option("--model <id>", "default model connection")
    .option("--model-origin <origin...>", "allow custom model origins in browser settings")
    .option("--base-url <url>", "OpenAI-compatible API base URL")
    .option("--api-key-env <name>", "environment variable containing the provider key")
    .addOption(new Option("--model-auth <mode>", "model authentication").choices(modelAuth.options))
    .option("--context-window <tokens>", "model context limit", integer)
    .option("--data-dir <directory>", "persistent conversations, credentials, and workflow state")
    .option("--cache-dir <directory>", "downloaded catalog, indexes, and model weights")
    .option("--username <name>", "server sign-in username (default: chartcoach)")
    .option("--password-env <name>", "environment variable containing the server password")
    .option("--password-file <file>", "read the server password from a secret mount")
    .option("--tracing", "enable configured Langfuse tracing")
    .addOption(
      new Option("--host <address>", "listen address (default: 127.0.0.1)").choices(
        configSchema.shape.server.unwrap().shape.host.unwrap().options,
      ),
    )
    .option("--port <number>", "public port, or 0 for an available port (default: 4273)", integer)
    .option("--public-url <origin>", "external origin when using a reverse proxy")
    .option(
      "--embed-origin <origin...>",
      "allow pages at these origins, or * for any page, to embed the app",
    )
    .option("--no-open", "print the URL without opening a browser", undefined);
}

type SettingsOptions = ReturnType<ReturnType<typeof options>["opts"]>;

function configuration(values: SettingsOptions, explicitOpen: boolean) {
  loadEnvironmentFile(values.envFile);

  return loadConfig({
    configFile: values.config,
    overrides: {
      catalog: { source: values.catalog, profile: values.catalogProfile },
      modelOrigins: values.modelOrigin,
      tracing: values.tracing,
      model: {
        provider: values.provider,
        model: values.model,
        baseURL: values.baseUrl,
        apiKeyEnv: values.apiKeyEnv,
        auth: values.modelAuth,
        contextWindow: values.contextWindow,
      },
      server: {
        host: values.host,
        port: values.port,
        publicURL: values.publicUrl,
        open: explicitOpen ? values.open : undefined,
        username: values.username,
        passwordEnv: values.passwordEnv,
        passwordFile: values.passwordFile,
        embedOrigins: values.embedOrigin,
      },
      storage: { dataDir: values.dataDir, cacheDir: values.cacheDir },
    },
  });
}

const program = new Command()
  .name("chartcoach")
  .description("Run ChartCoach locally for source-traced visualization design guidance.")
  .version(version)
  .showHelpAfterError()
  .showSuggestionAfterError()
  .exitOverride();

options(program.command("chat", { isDefault: true }).description("Start the chat app"))
  .option("--verbose", "print worker diagnostics")
  .action(async (_options, command) => {
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
          dataDir: config.storage.dataDir,
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
  });

options(program.command("doctor").description("Check configuration, catalog, and native runtime"))
  .option("--json", "print a JSON diagnostic report")
  .action(async (_options, command) => {
    try {
      const config = configuration(command.opts(), command.getOptionValueSource("open") === "cli");
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
