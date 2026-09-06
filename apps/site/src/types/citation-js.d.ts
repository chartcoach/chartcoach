declare module "citation-js" {
  export type CiteFormat = string;

  export type CiteFormatOptions = {
    format?: string;
    template?: string;
    lang?: string;
  };

  export default class Cite<Data extends object = object> {
    data: Data[];

    constructor(input?: string | Data | readonly Data[]);

    format(type: CiteFormat, options?: CiteFormatOptions): string;
  }
}
