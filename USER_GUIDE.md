# ReaCrusher — JSFX

A standalone stereo JSFX effect combining distortion, resonant filtering and
compression. No external includes, images, or plugin installation required.

## Install in REAPER

1. Choose **Options → Show REAPER resource path in explorer/finder**.
2. Copy `ReaCrusher.jsfx` into the `Effects` folder (or a subfolder).
3. Open the FX browser, refresh its list, and search for **ReaCrusher**.

The custom drawn interface exposes distortion enable, mechanical,
tube, filter enable, cutoff, resonance, compressor enable, amount, Normal/Phat,
master enable, wet mix, and master volume. Continuous controls use the rebuild's
normalized 0–1 ranges. Master volume uses its nonlinear taper; 1 is unity.
Master bypass passes the input unchanged. With Master on, the final output clips
at ±0.9999, including at zero wet mix, as in the native rebuild.

The 20 factory presets plus Clear use REAPER's native preset menu. Install
`ReaCrusher.jsfx.rpl` alongside `ReaCrusher.jsfx`. REAPER imports the bank on first
instantiation. If the effect is already known to REAPER, use the preset toolbar's
**+ → Import preset library (.rpl)** command. User-edited presets are kept in REAPER's
own preset storage; the package does not overwrite that storage.

## DSP and compatibility

The signal order is mechanical distortion → resonant biquad low-pass and linked
limiter → tube distortion → linked compressor → wet/dry → master gain → clip.
Normal compression uses the recovered envelope follower; Phat uses direct peaks.
Cutoff uses a nonlinear frequency taper, resonance maps to Q, and output volume
uses a nonlinear gain taper.

JSFX uses double precision. This version smooths continuous controls per sample
with a 10 ms time constant and updates filter coefficients every 16 samples.
The C++ engine uses block-based linear ramps and single precision, so automation,
startup transients, and output rounding differ. It does not claim bit-exact
matching. No oversampling is added; nonlinear stages can alias.

The interface is original procedural artwork, with no original skin assets.
Drag knobs vertically; hold Shift for fine adjustment, scroll to adjust, and
double-click to reset. Buttons toggle their corresponding parameters. The window
scales its composition to fit and supports Retina rendering. Input/output meters
show decaying stereo peaks. REAPER's native preset toolbar remains available.
All 12 parameter IDs and ranges are unchanged, preserving automation and presets.
FXP/FXB import, MIDI learn, and the original randomizer are not implemented; use
REAPER's parameter learning and project/preset storage.

Validation so far: static delimiter/declaration and UI binding checks, and comparison of all 240
factory parameter values against the C++ bank. The interface has been loaded in
REAPER and adjusted using user screenshots. Audio matching and a fresh ReaPack
installation have not yet been verified.

