# Mannix Squared JSFX

A collection of JSFX effects for REAPER, distributed through ReaPack.

## ReaCrusher

Stereo distortion, resonant low-pass filtering and compression for REAPER.
An original scalable interface, seven knobs, linked stereo processing, and
20 factory presets plus Clear using REAPER's native preset menu.

The interface uses procedural drawing and requires no image assets or external
plugin installation.

## Install with ReaPack

Import this repository URL in
**Extensions → ReaPack → Import repositories**:

```
https://raw.githubusercontent.com/mannixsquared/JSFX/main/index.xml
```

Browse packages, install ReaCrusher, then refresh REAPER's FX browser. The adjacent
`.rpl` bank is imported on first use. If the effect was previously installed,
use **+ → Import preset library (.rpl)** in its native preset toolbar.

## Manual installation

Copy both files from `Effects/` to the same directory beneath your REAPER resource
folder's `Effects` directory. Open the FX browser and search for ReaCrusher.

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
