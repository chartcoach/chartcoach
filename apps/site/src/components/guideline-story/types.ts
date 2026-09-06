export type StoryArtifactId =
  | "markdown"
  | "references"
  | "structured"
  | "embedding"
  | "access"
  | "skills"
  | "improve";

export type StoryStep = {
  eyebrow: string;
  title: string;
  body: string;
  surface: {
    intent: string;
    form: string;
    detail: string;
  };
  artifact: StoryArtifactId;
};

export type TokenKind =
  | "plain"
  | "comment"
  | "key"
  | "string"
  | "keyword"
  | "function"
  | "type"
  | "number"
  | "operator"
  | "punctuation";

export type CodeToken = {
  text: string;
  kind?: TokenKind;
};

export type CodeLine = readonly CodeToken[];
