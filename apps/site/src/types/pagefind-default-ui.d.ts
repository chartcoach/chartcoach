declare module "@pagefind/default-ui" {
  export type PagefindResult = {
    url: string;
    sub_results?: Array<{ url: string }>;
  };

  export type PagefindUIOptions = {
    element: string | HTMLElement;
    bundlePath?: string;
    baseUrl?: string;
    showImages?: boolean;
    showSubResults?: boolean;
    resetStyles?: boolean;
    translations?: Record<string, string>;
    processResult?: (result: PagefindResult) => void;
  };

  export class PagefindUI {
    constructor(options: PagefindUIOptions);
  }
}
