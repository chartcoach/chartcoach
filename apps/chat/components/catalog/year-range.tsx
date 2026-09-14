import { Slider } from "radix-ui";
import { useRef } from "react";
import * as stylex from "@stylexjs/stylex";
import { ui } from "../ui/ui";
import { styles } from "./filters.styles";

export function YearRange({
  min,
  max,
  from,
  to,
  disabled,
  onChange,
}: {
  min: number;
  max: number;
  from: number;
  to: number;
  disabled?: boolean;
  onChange: (from: number, to: number) => void;
}) {
  const clampedFrom = Math.max(min, Math.min(max, from));
  const clampedTo = Math.max(min, Math.min(max, to));
  const rangeFrom = Math.min(clampedFrom, clampedTo);
  const rangeTo = Math.max(clampedFrom, clampedTo);

  const drag = useRef<
    | {
        pointer: number;
        startX: number;
        width: number;
        from: number;
        to: number;
      }
    | undefined
  >(undefined);

  return (
    <Slider.Root
      {...stylex.props(styles.slider)}
      min={min}
      max={max}
      step={1}
      disabled={disabled}
      minStepsBetweenThumbs={0}
      value={[rangeFrom, rangeTo]}
      onValueChange={([start, end]) => onChange(start!, end!)}
      onPointerDownCapture={(event) => {
        const target = event.target;

        if (
          disabled ||
          event.button !== 0 ||
          !(target instanceof Element) ||
          !target.closest("[data-year-range]")
        )
          return;

        const width = event.currentTarget
          .querySelector("[data-year-track]")
          ?.getBoundingClientRect().width;

        if (!width) return;
        event.preventDefault();
        event.stopPropagation();
        drag.current = {
          pointer: event.pointerId,
          startX: event.clientX,
          width,
          from: rangeFrom,
          to: rangeTo,
        };
        event.currentTarget.setPointerCapture(event.pointerId);
      }}
      onPointerMoveCapture={(event) => {
        const current = drag.current;

        if (!current || current.pointer !== event.pointerId) return;
        event.stopPropagation();
        const span = current.to - current.from;

        const delta = Math.round(((event.clientX - current.startX) / current.width) * (max - min));

        const start = Math.max(min, Math.min(max - span, current.from + delta));

        onChange(start, start + span);
      }}
      onPointerUpCapture={(event) => {
        if (drag.current?.pointer !== event.pointerId) return;
        event.stopPropagation();
        drag.current = undefined;
        event.currentTarget.releasePointerCapture(event.pointerId);
      }}
      onPointerCancel={() => {
        drag.current = undefined;
      }}
      onLostPointerCapture={() => {
        drag.current = undefined;
      }}
    >
      <Slider.Track {...stylex.props(styles.sliderTrack)} data-year-track="">
        <Slider.Range
          {...stylex.props(styles.sliderRange)}
          data-year-range=""
          title="Drag to move the selected year range"
        />
      </Slider.Track>
      <Slider.Thumb
        {...stylex.props(ui.focus, styles.sliderThumb)}
        aria-label="Earliest publication year"
      />
      <Slider.Thumb
        {...stylex.props(ui.focus, styles.sliderThumb)}
        aria-label="Latest publication year"
      />
    </Slider.Root>
  );
}
