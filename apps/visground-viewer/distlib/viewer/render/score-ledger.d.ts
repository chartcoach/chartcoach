import type { CandidateRecord } from "../contract/types";
export declare function ScoreLedger({
  candidate,
  mode,
}: {
  candidate: CandidateRecord;
  mode: "matrix" | "floating";
}): import("react/jsx-runtime").JSX.Element | null;
export declare function ScoreBreakdownList({
  candidate,
  mode,
}: {
  candidate: CandidateRecord;
  mode: "compact" | "detail";
}): import("react/jsx-runtime").JSX.Element | null;
//# sourceMappingURL=score-ledger.d.ts.map
