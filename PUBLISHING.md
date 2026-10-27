# Publish under mannixsquared

1. Create an empty **public** GitHub repository named `JSFX`, owned by
   `mannixsquared`. Do not initialize it with a README or a license; both are here.
2. Upload this folder's contents to its `main` branch, including the hidden
   `.github/workflows/reapack.yml` and `.reapack-index.conf` files.
   Alternatively, initialize Git in this folder, commit, add the repository as
   `origin`, and push `main` using credentials allowed to write to mannixsquared.
3. Open the Actions tab and wait for the ReaPack workflow to finish. It checks
   the package and commits the generated `index.xml` automatically. If organization
   policy blocks workflow writes, permit this repository's workflow to write contents.
4. Test the raw index URL from README.md in a fresh/portable REAPER installation.
   Check all 21 presets, knob automation, and the custom interface before announcing it.

The distributable contains only the JSFX, its preset library and documentation.
The local `js-ReaCrusher_jsfx.ini` is intentionally excluded: it is REAPER's local
preset storage and should not replace recipients' user presets.

## Existing installations

ReaPack installs effects below its own repository/category directories. If you
already installed ReaCrusher manually at the Effects root, keep it until projects
using that path have been migrated. The two paths can appear as separate entries.

## Validation performed locally

Run `python3 tools/validate_package.py` from this directory. It checks metadata,
all 21 RPL payloads, slider slots and parameter ranges, license markers, and UI
parameter bindings. GitHub Actions additionally runs the official indexer's
`reapack-index --check` before generating the index.

Local `reapack-index --check` was not run: its native dependency needs CMake,
which is unavailable on this machine. The workflow performs that check on Linux
before publishing. Fresh automatic bank import and ReaPack installation still
require a host test.
