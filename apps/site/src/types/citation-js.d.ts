declare module "citation-js" {
  export type CiteFormat =
    | "citation"
    | "bibliography"
    | "data"
    | "bibtex"
    | "citation-apa"
    | string;

  export type CiteFormatOptions = {
    format?: "text" | "html" | string;
    template?: string;
    lang?: string;
    [key: string]: unknown;
  };

  export default class Cite {
    data: unknown[];

    constructor(input?: unknown);

    format(type: CiteFormat, options?: CiteFormatOptions): string;
  }
}
