export type ChartCoachDefaults = {
  catalogArtifactBaseUrl: string;
  catalogDigest: string;
  catalogVersion: string;
  guidelineUrlTemplate: string;
  indexTopK: number;
  lanceDocumentTable: string;
};

export const CHARTCOACH_DEFAULTS = {
  catalogArtifactBaseUrl: "https://artifacts.chartcoach.dev",
  catalogDigest: "7cfd43ee820be252b8ae9058c4c36109a9c8415c6b3a5ff8a9127117b4a10c19",
  catalogVersion: "0.1.6",
  guidelineUrlTemplate: "https://chartcoach.dev/guidelines/{id}",
  indexTopK: 10,
  lanceDocumentTable: "catalog_documents",
} as const satisfies ChartCoachDefaults;
