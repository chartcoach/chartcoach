import * as React from "react";

import {
  type ChartCoachMarkMode,
  type ChartCoachMarkPose,
  type ChartCoachTheme,
  renderChartCoachMarimekkoSvg,
} from "../lib/chartcoach-marimekko";

type ChartCoachMarimekkoMarkProps = {
  className?: string;
  style?: React.CSSProperties;
  mode?: ChartCoachMarkMode;
  pose?: ChartCoachMarkPose;
  theme?: ChartCoachTheme;
  title?: string;
  idPrefix?: string;
};

function ChartCoachMarimekkoMark({
  className,
  style,
  mode = "static",
  pose = "end",
  theme = "auto",
  title,
  idPrefix,
}: ChartCoachMarimekkoMarkProps) {
  return (
    <span
      aria-hidden={title ? undefined : true}
      className={className}
      style={{ display: "block", lineHeight: 0, ...style }}
      dangerouslySetInnerHTML={{
        __html: renderChartCoachMarimekkoSvg({ mode, pose, theme, title, idPrefix }),
      }}
    />
  );
}

export { ChartCoachMarimekkoMark };
export type { ChartCoachMarimekkoMarkProps };
