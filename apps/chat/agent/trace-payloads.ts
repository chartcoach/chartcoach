import {
  defineInstrumentation,
  type InstrumentationEvent,
  type ProviderDefinition,
} from "eve/instrumentation";
import type { Attributes } from "@opentelemetry/api";
import { traceMessages, errorContent } from "./trace-content";
import { z } from "zod";
import type { JsonValue } from "eve/instrumentation";
import { answerSchema, type Answer } from "../shared/answer";

type ModelPayload = {
  id: string;
  completed: boolean;
  input?: JsonValue;
  output?: JsonValue;
  tools?: JsonValue;
};

type ToolPayload = {
  sessionId: string;
  turnId: string;
  callId: string;
  name: string;
  input: JsonValue;
  output?: JsonValue;
  completed: boolean;
};

type TurnPayload = { input?: JsonValue; output?: JsonValue; answer?: Answer };

export const turnKey = (sessionId: string, turnId: string) => JSON.stringify([sessionId, turnId]);

const stepKey = (sessionId: string, turnId: string, stepIndex: number, attemptIndex = 0) =>
  JSON.stringify([sessionId, turnId, stepIndex, attemptIndex]);

export class TracePayloads {
  private readonly models = new Map<string, ModelPayload[]>();
  private readonly tools = new Map<string, ToolPayload>();
  private readonly turns = new Map<string, TurnPayload>();
  private readonly settled = new Set<string>();

  capture(event: InstrumentationEvent): void {
    if (
      event.type === "channel.delivery.started" &&
      event.turnId &&
      event.input?.message !== undefined
    ) {
      this.turn(event.sessionId, event.turnId).input = traceMessages([
        { role: "user", content: event.input.message },
      ]);
    }

    if (event.type === "model.call.started") {
      const { scope } = event;
      const key = stepKey(scope.sessionId, scope.turnId, scope.stepIndex, scope.attemptIndex);
      const models = this.models.get(key) ?? [];

      if (!models.some((model) => model.id === event.idempotencyKey)) {
        const input = event.input
          ? traceMessages([
              ...(event.input.instructions === undefined
                ? []
                : [
                    z.string().safeParse(event.input.instructions).success
                      ? { role: "system", content: z.string().parse(event.input.instructions) }
                      : event.input.instructions,
                  ]),
              ...event.input.messages,
            ])
          : undefined;

        models.push({
          id: event.idempotencyKey,
          completed: false,
          input,
          tools: z
            .array(
              z.object({
                name: z.string(),
                description: z.string().optional(),
                inputSchema: z.json().optional(),
              }),
            )
            .safeParse(event.input?.tools).data,
        });
        this.models.set(key, models);
        const turn = this.turn(scope.sessionId, scope.turnId);

        if (turn.input === undefined && Array.isArray(input))
          turn.input = input.filter((message) => message.role === "user").slice(-1);
      }
    }

    if (event.type === "model.call.completed" || event.type === "model.call.failed") {
      const { scope } = event;

      const model = this.models
        .get(stepKey(scope.sessionId, scope.turnId, scope.stepIndex, scope.attemptIndex))
        ?.find((model) => model.id === event.idempotencyKey);

      if (model) {
        model.completed = true;
        model.output =
          event.type === "model.call.completed"
            ? event.content === undefined
              ? undefined
              : traceMessages([{ role: "assistant", content: event.content }])
            : errorContent(event.error);
      }

      if (event.type === "model.call.failed")
        this.turn(scope.sessionId, scope.turnId).output = errorContent(event.error);

      if (
        event.type === "model.call.completed" &&
        event.content?.some((part) => part.type === "text" && part.text.length)
      )
        this.turn(scope.sessionId, scope.turnId).output = model?.output;
    }

    if (event.type === "tool.call.started")
      this.tools.set(event.idempotencyKey, {
        sessionId: event.scope.sessionId,
        turnId: event.scope.turnId,
        callId: event.callId,
        name: event.toolName,
        input: z.json().parse(event.input),
        completed: false,
      });

    if (event.type === "tool.call.completed" || event.type === "tool.call.failed") {
      const tool = this.tools.get(event.idempotencyKey);

      if (tool) {
        tool.completed = true;
        tool.output =
          event.type === "tool.call.failed"
            ? errorContent(event.error)
            : event.output.type === "result"
              ? z.json().parse(event.output.output)
              : errorContent(event.output.error);

        if (
          tool.name === "present_answer" &&
          event.type === "tool.call.completed" &&
          event.output.type === "result"
        ) {
          const answer = answerSchema.safeParse(event.output.output);

          if (answer.success) {
            const turn = this.turn(tool.sessionId, tool.turnId);
            turn.answer = answer.data;
          }
        }
      }
    }

    if (
      (event.type === "session.waiting" ||
        event.type === "session.completed" ||
        event.type === "session.failed") &&
      "sessionId" in event &&
      event.turnId
    )
      this.settled.add(turnKey(event.sessionId, event.turnId));
  }

  ready(attributes: Attributes): boolean {
    const sessionId = z.string().safeParse(attributes["agent.run.id"]);
    const turnId = z.string().safeParse(attributes["agent.turn.id"]);

    if (!sessionId.success || !turnId.success) return true;

    if (attributes["gen_ai.operation.name"] === "invoke_agent")
      return this.isTurnSettled(attributes);

    if (attributes["gen_ai.operation.name"] === "chat") {
      const model = this.models.get(
        stepKey(
          sessionId.data,
          turnId.data,
          Number(attributes["agent.step.index"]),
          Number(attributes["agent.step.attempt"] ?? 0),
        ),
      )?.[0];

      return model?.completed ?? this.isTurnSettled(attributes);
    }

    if (attributes["gen_ai.operation.name"] === "execute_tool") {
      const tool = [...this.tools.values()].find(
        (tool) =>
          tool.sessionId === sessionId.data && tool.callId === attributes["gen_ai.tool.call.id"],
      );

      return tool?.completed ?? this.isTurnSettled(attributes);
    }

    return true;
  }

  isTurnSettled(attributes: Attributes): boolean {
    const sessionId = z.string().safeParse(attributes["agent.run.id"]);
    const turnId = z.string().safeParse(attributes["agent.turn.id"]);

    return (
      sessionId.success && turnId.success && this.settled.has(turnKey(sessionId.data, turnId.data))
    );
  }

  enrich(attributes: Attributes): void {
    const identity = z
      .object({ "agent.run.id": z.string(), "agent.turn.id": z.string() })
      .safeParse(attributes);

    if (!identity.success) return;
    const sessionId = identity.data["agent.run.id"];
    const turnId = identity.data["agent.turn.id"];
    const operation = attributes["gen_ai.operation.name"];
    const turn = this.turns.get(turnKey(sessionId, turnId));

    if (operation === "invoke_agent" && turn) {
      this.setContent(attributes, turn.input, turn.answer ?? turn.output);

      if (turn.answer)
        attributes["langfuse.observation.metadata.presentedAnswer"] = JSON.stringify(turn.answer);
    }

    if (operation === "chat") {
      const models = this.models.get(
        stepKey(
          sessionId,
          turnId,
          Number(attributes["agent.step.index"]),
          Number(attributes["agent.step.attempt"] ?? 0),
        ),
      );

      const model = models?.shift();

      if (model) {
        this.setContent(attributes, model.input, model.output);

        if (model.tools)
          attributes["langfuse.observation.metadata.tools"] = JSON.stringify(model.tools);
      }
    }

    if (operation === "execute_tool") {
      const tool = [...this.tools.values()].find(
        (tool) => tool.sessionId === sessionId && tool.callId === attributes["gen_ai.tool.call.id"],
      );

      if (tool) this.setContent(attributes, tool.input, tool.output);
    }
  }

  release(sessionId: string, turnId: string): void {
    const key = turnKey(sessionId, turnId);
    this.turns.delete(key);
    this.settled.delete(key);

    for (const step of this.models.keys())
      if (step.startsWith(key.slice(0, -1) + ",")) this.models.delete(step);

    for (const [id, tool] of this.tools)
      if (turnKey(tool.sessionId, tool.turnId) === key) this.tools.delete(id);
  }

  clear(): void {
    this.models.clear();
    this.tools.clear();
    this.turns.clear();
    this.settled.clear();
  }

  private turn(sessionId: string, turnId: string): TurnPayload {
    const key = turnKey(sessionId, turnId);
    let turn = this.turns.get(key);

    if (!turn) {
      turn = {};
      this.turns.set(key, turn);
    }

    return turn;
  }

  private setContent(
    attributes: Attributes,
    input: JsonValue | undefined,
    output: JsonValue | undefined,
  ): void {
    if (input !== undefined) attributes["langfuse.observation.input"] = JSON.stringify(input);

    if (output !== undefined) attributes["langfuse.observation.output"] = JSON.stringify(output);
  }
}

export function contentInstrumentation(payloads: TracePayloads) {
  const capture = (event: InstrumentationEvent) => payloads.capture(event);

  const definition = {
    tracePolicy: () => ({ emit: true, recordInputs: true, recordOutputs: true }),
    events: {
      "channel.delivery.started": capture,
      "model.call.started": capture,
      "model.call.completed": capture,
      "model.call.failed": capture,
      "tool.call.started": capture,
      "tool.call.completed": capture,
      "tool.call.failed": capture,
      "session.waiting": capture,
      "session.completed": capture,
      "session.failed": capture,
    },
  } satisfies ProviderDefinition;

  return { ...defineInstrumentation(definition), ...definition };
}
