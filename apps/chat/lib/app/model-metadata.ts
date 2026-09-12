import type { Connection } from "../../shared/preferences";

export function modelMetadata(connection: Connection, endpoint?: string) {
  return {
    modelConnectionId: connection.id,
    modelConnectionName: connection.name,
    modelProvider: connection.provider,
    modelName: connection.model,
    modelContextWindow: connection.contextWindow,
    modelManaged: connection.managed,
    modelEndpointOrigin: endpoint ? new URL(endpoint).origin : undefined,
  };
}
