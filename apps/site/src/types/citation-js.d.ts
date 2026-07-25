declare module "citation-js" {
  export type CiteFormat = string;

  export type CiteFormatOptions = {
    format?: string;
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
