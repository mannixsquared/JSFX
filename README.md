# Mannix Squared JSFX

A collection of JSFX effects for REAPER, distributed through ReaPack.

## ReaCrusher

Stereo distortion, resonant low-pass filtering and compression for REAPER.
An original scalable interface, seven knobs, linked stereo processing, and
20 factory presets plus Clear using REAPER's native preset menu.

The interface uses procedural drawing and requires no image assets or external
plugin installation.

## Macro Knob

A single macro control for REAPER parameter links. It uses the same charcoal and
amber interface as ReaCrusher, with scaled typography, vertical dragging,
Shift for fine changes, wheel adjustment, and double-click or right-click reset.
Audio and MIDI pass through unchanged.

## XY Pad

A four-source stereo blender: route four stereo sources to channels 1–8 and blend
them with the pad. It retains equal-power interpolation, smooth XY movement, and
the linked output limiter. The panel uses ReaCrusher's palette and typography,
with matching ceiling/release knobs, source-weight indicators and a gain-reduction
readout. Shift-drag for fine movement; double-click the pad to centre it.

## Install with ReaPack

Import this repository URL in
**Extensions → ReaPack → Import repositories**:

```
https://raw.githubusercontent.com/mannixsquared/JSFX/main/index.xml
```

Browse packages, search for ReaCrusher, Macro Knob, or XY Pad, and install the
effects you want. Then refresh REAPER's FX browser. The adjacent
`.rpl` bank is imported on first use. If the effect was previously installed,
use **+ → Import preset library (.rpl)** in its native preset toolbar.

## Manual installation

Copy the `.jsfx` files you want from `Effects/` into your REAPER resource folder's
`Effects` directory. For ReaCrusher, copy its `.rpl` file alongside it. Open the FX
browser and search for the effect name.

Drag vertically to adjust; Shift-drag for fine changes, scroll to adjust, and
double-click to reset a knob. See [USER_GUIDE.md](USER_GUIDE.md) for DSP details.

## License

Copyright (C) 2026 Mannix Squared.
Licensed under GNU GPL version 3 or later; see [LICENSE](LICENSE).

## Development and updates

The `main` branch is indexed by GitHub Actions. Increase `@version` in
`Effects/ReaCrusher.jsfx`, update `@changelog`, then push to publish an update.
Keep the effect's filename and category path stable to preserve project references.
The generated `index.xml` points to committed file versions.

## Adding effects

Add each effect as a separate `.jsfx` package under a category directory such as
`Effects/`. Give each package its own version and metadata header, and list any
companion files with `@provides`. Mark shared scripts and development helpers
`@noindex`. All packages share this repository’s ReaPack index.
