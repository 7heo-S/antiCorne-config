# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

Personal [ZMK](https://zmk.dev) firmware configuration for a custom "Corne Choc Pro" split keyboard (nRF52840-based, 3x6+3 columns per half). The keymap layout is inspired by [optimot](https://optimot.fr/) and adds extra layers for Greek letters and French accented characters. This is a ZMK **user config repo** (the `config/` self-module referenced by `config/west.yml`), not the ZMK firmware itself — firmware sources are pulled in at build time via west.

## Build

Firmware is built exclusively via GitHub Actions (`.github/workflows/build.yml`), which delegates to ZMK's reusable `build-user-config.yml` workflow. There is no local build tooling in this repo (no Makefile/script) — pushing to GitHub (or opening a PR) is how you get firmware binaries, produced as workflow artifacts.

- `build.yaml` defines the build matrix: which board + shield + snippet combos get built. Currently: `corne_choc_pro_left`/`corne_choc_pro_right` with the `nice_view` shield and `studio-rpc-usb-uart` snippet (for ZMK Studio support), plus a `settings_reset` variant of each half for clearing stored settings on the controller.
- `config/west.yml` is the west manifest: pins ZMK to `v0.3`, and pulls in two modules from `urob`: `zmk-unicode` (Unicode/dead-key input via `&uc`) and `zmk-helpers` (the `ZMK_BEHAVIOR(...)` macro sugar used throughout the keymap).
- There is no local test suite or linter — validate keymap changes by reading the devicetree carefully and letting the CI build catch syntax/compile errors, or by building locally with `west` if you have a Zephyr/ZMK toolchain set up (not present in this repo).

## Architecture

Two logically separate things live side by side and are easy to conflate:

1. **The board definition** (`boards/arm/corne_choc_pro/`) — the hardware description for this custom keyboard: pin/matrix transform (`corne_choc_pro.dtsi`), physical key layouts for a 6-column and a 5-column variant (`corne_choc_pro-layouts.dtsi`, with `default_layout`/`five_col_layout` physical-layout nodes and matching position maps), per-half `.dts`/`_defconfig` files for left/right, and Kconfig glue. It also contains its own `corne_choc_pro.keymap`, which is effectively a stale/reference copy — it is **not** what gets built.
2. **The active user keymap** (`config/corne_choc_pro.keymap`) — this is the file that actually defines behavior and is what you should edit when changing the layout. It's picked up via `board_root: .` in `build.yaml` + the `self.path: config` entry in `west.yml`. `config/corne_choc_pro.conf` holds Kconfig overrides (mouse emulation, sleep/idle timeouts, keyboard name — currently all commented out), and `config/corne_choc_pro.json` is the ZMK Studio / keymap-editor physical layout description.

### Keymap structure (`config/corne_choc_pro.keymap`)

- Six layers, each with an ASCII-art comment diagram above its `bindings` block showing the physical key grid — **keep these diagrams in sync when changing bindings**, they're the primary way to reason about the layout: `default_layer` (OPTIMOT French layout), `symbol_layer`, `greek_layer`, `navigation_layer`, `function_layer` (Bluetooth profiles + F-keys), `diacritics_layer` (circumflex/diaeresis/trema accents).
- Layers are accessed via `&lt N ...` (layer-tap) on the home row's thumb keys and pinky keys (e.g. `&lt 5 N`, `&lt 4 ESC`), not via a dedicated momentary-layer key — check existing `&lt`/`&mo` usage before adding a new layer-access binding, and remember layer indices are positional (order in the `keymap { }` node), so inserting a layer in the middle renumbers everything after it.
- Home row mods use two custom `hold-tap` behaviors, `hml` (left hand) and `hmr` (right hand), both `"balanced"` flavor with a 140ms tapping term and `hold-trigger-on-release`. Each declares `hold-trigger-key-positions` as the *opposite* hand's key positions — this is what prevents the home-row-mod hold from firing on same-hand rolls. If you change the physical key count/order (e.g. editing `corne_choc_pro-layouts.dtsi`), these position lists must be updated to match.
- Custom `mod_morph` behaviors (declared with the `ZMK_BEHAVIOR(...)` macro from `zmk-helpers`) implement "smart" punctuation keys that change output based on Shift/Alt: e.g. `COMMA_OPT` (comma / shift→semicolon), `QUOT_OPT` (quote, nests alt→backtick/doublequote under shift→underscore), `SLSH_OPT`, `DASH_OPT`. These follow a two-level nesting pattern (an alt-morph feeding into a shift-morph) — follow that pattern if adding new overloaded punctuation keys.
- French/Greek accented characters are emitted via `&uc UC_FR_*` / `&uc UC_EL_*` Unicode macros from the `zmk-unicode` module (see `keys-extra.h` for available glyph names), with `default-mode = UC_MODE_LINUX` set globally via `&uc { ... };`. Some accented letters (`c_ced`, `e_hat`, `i_hat`, `u_hat`, `y_trema`) are their own named `mod_morph` behaviors combining a plain letter with an alt-modified accented variant, so they can be placed directly on the base layer.
- `hm_upsilon`/`hm_tau` are one-off `hold_tap` behaviors combining a home-row mod (tap → key) with a Greek letter Unicode macro (hold → `&uc_upsilon`/`&uc_tau`), used only on the Greek layer.

### Display shield (`boards/shields/nice_view_disp/`)

A custom fork/variant of the community `nice_view` display shield with a custom status screen (`custom_status_screen.c`) and widgets (`widgets/*.c`: battery/output status, peripheral status, Bluetooth bolt icon, decorative art, shared utils). Edit widget `.c`/`.h` files here to change what's shown on the OLED; `nice_view_disp.overlay` and `.conf`/`Kconfig.*` wire it up as a shield selectable via `build.yaml`'s `shield:` field.
