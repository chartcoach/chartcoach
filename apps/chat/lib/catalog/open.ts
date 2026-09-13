import { openCatalog, indexPath } from "@chartcoach/catalog/node";
import type { Catalog } from "@chartcoach/catalog";
import { settings } from "../../runtime/settings";

let catalog: ReturnType<typeof openCatalog> | undefined;

const indexes = new WeakMap<Catalog, Map<string, ReturnType<typeof openIndex>>>();

export function getCatalog() {
  return (catalog ??= openCatalog(settings.catalog.source, {
    cacheDirectory: settings.storage.cacheDir,
  }).catch((error) => {
    catalog = undefined;
    throw error;
  }));
}

export async function getIndex(catalog: Catalog, profile: string) {
  let profiles = indexes.get(catalog);

  if (!profiles) {
    profiles = new Map();
    indexes.set(catalog, profiles);
  }

  let pending = profiles.get(profile);

  if (!pending) {
    pending = openIndex(catalog, profile).catch((error) => {
      profiles.delete(profile);
      throw error;
    });
    profiles.set(profile, pending);
  }

  return pending;
}

async function openIndex(catalog: Catalog, profile: string) {
  const { profile: info } = await catalog.describe({ profile });

  if (!info) throw new Error("Choose an available catalog index profile.");
  const path = await indexPath(catalog, profile);
  const { connect } = await import("@lancedb/lancedb");
  const db = await connect(path);

  try {
    const table = await db.openTable("documents");

    try {
      await table.checkout(await table.version());
    } catch (error) {
      table.close();
      throw error;
    }

    return {
      catalog,
      db,
      table,
      info,
    };
  } catch (error) {
    db.close();
    throw error;
  }
}
