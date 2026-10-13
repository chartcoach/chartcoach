import type { EveMessage } from "eve/react";

/** A message the user sent, shown before the runtime confirms it. */
export interface SentTurn {
  id: string;
  /** Runtime message count when the turn was sent. */
  start: number;
  parts: EveMessage["parts"];
  /** The send failed or was cancelled. Messages the runtime accepted keep their ids. */
  withdrawn?: boolean;
}

/**
 * Shows the latest sent turn until the runtime confirms its messages. Confirmed
 * messages take their turn's ids, so the elements rendered for the optimistic
 * messages stay mounted through the handoff.
 */
export function projectTurns(
  messages: readonly EveMessage[],
  turns: readonly SentTurn[],
  running: boolean,
) {
  const ids = new Map<string, string>();
  const pending: EveMessage[] = [];

  for (const [index, turn] of turns.entries()) {
    const sent = messages.slice(turn.start, turns[index + 1]?.start);
    const user = sent.findIndex((message) => message.role === "user");

    const assistant =
      user < 0 ? -1 : sent.findIndex((message, at) => at > user && message.role === "assistant");

    if (user >= 0) ids.set(sent[user]!.id, `${turn.id}:user`);

    if (assistant >= 0) ids.set(sent[assistant]!.id, `${turn.id}:assistant`);

    if (index < turns.length - 1 || turn.withdrawn) continue;

    if (user < 0)
      pending.push({
        id: `${turn.id}:user`,
        role: "user",
        parts: turn.parts,
        metadata: { optimistic: true, status: "submitted" },
      });

    // An unconfirmed turn is still in flight even between its preparation and send.
    if (assistant < 0 && (running || user < 0))
      pending.push({
        id: `${turn.id}:assistant`,
        role: "assistant",
        parts: [],
        metadata: { optimistic: true, status: "streaming" },
      });
  }

  return {
    messages: [
      ...messages.map((message) => {
        const id = ids.get(message.id);

        return id ? { ...message, id } : message;
      }),
      ...pending,
    ],
    id: (id: string) => ids.get(id) ?? id,
  };
}
