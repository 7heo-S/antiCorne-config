# antiCorne keymap reference

Corne Choc Pro, 7 layers. Generated from `config/corne_choc_pro.keymap`.

## Notation

- **Bold** = plain tap
- `⌥ x` = **hold Alt** (from another key) **then tap this key** → `x`
- `⇧ x` = **Shift** + tap → `x`
- `⌘`/`⌥`/`⌃`/`⇧` under a bold letter = **hold this key** for that modifier (Gui/Alt/Ctrl/Shift), tap for the letter
- `Esc→FUNC` = **hold this key** to switch to the FUNC layer, tap for Esc
- `—` = unused (`&none`)
- the empty gap in the middle of each row is the physical split between the two halves

## Layer access (held from the default layer)

| Key | Layer |
|---|---|
| `Esc` (left thumb) | FUNCTION |
| `Tab` (left thumb) | GREEK |
| `Bspc` (right thumb) | SYMBOL |
| `Enter` (right thumb) | NAVIGATION |
| `N` (right pinky, home row) | DIACRITICS |
| `Del` (right thumb) | ACCENT *(trial — see Layer 6)* |

**Caps Word combo:** hold **U** (left) + **T** (right) together → toggles Caps Word (auto-releases at the next word break). Default layer only.

---

## Layer 0 — Default (OPTIMOT)

| | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **ù** | **à** | **J** | **O** | **é** | **B** | | | **F** | **D** | **L** | **'**<br>⌥`"` ⇧`&#96;` | **Q** | **X** |
| **/**<br>⌥`&#124;` ⇧`\` | **A**<br>⌘ | **I**<br>⌥ | **E**<br>⌃ | **U**<br>⇧ | **,**<br>⇧`;` | | | **P** | **T**<br>⇧ | **S**<br>⌃ | **R**<br>⌥ | **N**<br>→DIAC | **?**<br>⇧`!` |
| **-**<br>⌥`~` ⇧`_` | **K** | **Y** | **è** | **.**<br>⇧`:` | **W** | | | **G** | **ç**<br>(⌥`C`) | **M** | **H** | **V** | **Z** |

Thumbs: **Esc**→FUNC · **Tab**→GREEK · **Space** — **Bspc**→SYMBOL · **Enter**→NAV · **Del**→ACCENT

`A`/`I`/`E`/`U` (left) and `T`/`S`/`R` (right) are home-row mods: hold for the modifier shown, tap for the letter.

---

## Layer 1 — Symbol

| | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| — | **%** | **&** | **^** | **$** | **[** | | | **]** | **7** | **8** | **9** | **#** | — |
| **/**<br>⌥`&#124;` ⇧`\` | **√** | **+**<br>⇧`±` | **=**<br>⌥`≈` ⇧`≠` | **\***<br>⌥`×` ⇧`†` | **(** | | | **)** | **4**<br>⇧ | **5**<br>⌃ | **6**<br>⌥ | **0** | — |
| — | **@** | **<**<br>⌥`⟨` ⇧`«` | **-**<br>⌥`~` ⇧`_` | **>**<br>⌥`⟩` ⇧`»` | **{** | | | **}** | **1** | **2** | **3** | **.** | **,** |

Thumbs: **Esc** · **Tab** · **Space** — — · **Enter** · **Del**

`4`/`5`/`6` are home-row mods (same as `T`/`S`/`R` on the default layer).

---

## Layer 2 — Greek

| | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| — | — | — | **ο** omikron | **θ**<br>⌥`ϑ` | **β** beta | | | **φ**<br>⌥`ϕ` | **δ** delta | **λ** lambda | — | — | **ξ** xi |
| — | **α** alpha | **ι** iota<br>⌥ | **ε**<br>⌥`ϵ` | **υ** upsilon<br>⇧ | | | | **π**<br>⌥`ϖ` | **τ** tau<br>⇧ | **σ**<br>⌥`ς` | **ρ**<br>⌥`ϱ`<br>(⌥ hold) | **ν** nu | — |
| **ψ** psi | **κ**<br>⌥`ϰ` | — | — | — | **ω** omega | | | **γ** gamma | **χ** chi | **μ** mu | **η** eta | — | **ζ** zeta |

Thumbs: **Esc** · — · **Space** — **Bspc** · **Enter** · **Del**

`I` and `R` are Alt home-row mods here (mirroring the default layer's Alt placement), so you can hold one and tap θ/φ/ε/κ/π/ρ/σ on the other hand for their variant forms (vartheta/varphi/varepsilon/varkappa/varpi/varrho/varsigma). `U`/`T` still hold Shift, same physical keys as the default layer.

---

## Layer 3 — Navigation

| | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| — | — | **Vol−** | **Mute** | **Vol+** | **Paste**<br>(⌃V) | | | — | **PgDn** | **↑** | **PgUp** | — | — |
| — | **Gui** | **Alt** | **Ctrl** | **Shift** | **Cut**<br>(⌃X) | | | **Home** | **←** | **↓** | **→** | **End** | — |
| — | — | **⏮** prev track | **⏯** play/pause | **⏭** next track | **Copy**<br>(⌃C) | | | — | **Undo**<br>(⌃Z) | — | **Redo**<br>(⌃Y) | — | — |

Thumbs: **Esc** · **Tab** · **Space** — **Bspc** · — · **Del**

Undo/redo/cut/copy/paste are literal `Ctrl+Z/Y/X/C/V` shortcuts, not HID consumer codes — Linux and most apps don't listen for the consumer "AC_*" versions. Media transport keys (volume, mute, play/pause, track skip) stay as real consumer codes since those work everywhere.

---

## Layer 4 — Function

| | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **BT clear** | **BT 5** | **BT 4** | **BT 3** | **BT 2** | **BT 1** | | | — | — | **F7** | **F8** | **F9** | **F12** |
| **RGB toggle** | **Gui** | **Alt** | **Ctrl** | **Shift** | — | | | — | — | **F4** | **F5** | **F6** | **F11** |
| — | — | — | — | — | — | | | — | — | **F1** | **F2** | **F3** | **F10** |

Thumbs: — · **Tab** · **Space** — **Bspc** · **Enter** · **Del**

`BT 1`–`BT 5` select Bluetooth profile 1–5 (`BT_SEL 0`–`4` in code — profile numbers are 1-indexed here, 0-indexed in source). F-keys are arranged like a numpad (F1-F9 as a 3×3 grid bottom-to-top), matching the numbers on the Symbol layer; F10-F12 fill the remaining pinky column.

---

## Layer 5 — Diacritics ("hats & dots")

| | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| — | — | **æ** | **ô** | **œ** | — | | | — | — | — | — | — | — |
| — | **â** | **î**<br>⌥`ï` | **ê**<br>⌥`ë` | **û**<br>⌥`ü` | — | | | — | **RShift** | — | **RAlt** | — | — |
| — | — | **y**<br>⌥`ÿ` | — | — | — | | | — | — | — | — | — | — |

Thumbs: **Esc** · **Tab** · **Space** — **Bspc** · **Enter** · **Del**

Held with the `N` key (right pinky, home row on the default layer). `RShift`/`RAlt` are plain modifier keys here, handy for chording with the alt-tap accents on this layer.

---

## Layer 6 — Accent *(trial)*

| | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | | | — | — | — | — | — | — |
| — | — | **^**<br>⌥`¨` | **&#96;**<br>⌥`´` | **~**<br>⌥`¯` | — | | | — | **¸**<br>⌥`ˇ` | **˚**<br>⌥`˙` | — | — | — |
| — | — | — | — | — | — | | | — | — | — | — | — | — |

Thumbs: **Esc** · **Tab** · **Space** — **Bspc** · **Enter** · —

Held with **Del** (right thumb — see note above). Type the base letter **first**, then hold Del and tap one of these. Unlike every other accent key in this file, these send a *combining* Unicode mark (U+0300 block) rather than a replacement letter — it visually fuses onto whatever you just typed, so it works on **any** letter, not just the ones with a precomposed accented form (e.g. `n` + circumflex → n̂, which has no other way to type here). Cells above show the plain "spacing" form of each mark for legibility; what's actually sent is the combining version.

| Key | Tap | Alt+tap |
|---|---|---|
| circumflex/diaeresis | combining circumflex | combining diaeresis |
| grave/acute | combining grave | combining acute |
| tilde/macron | combining tilde | combining macron |
| cedilla/caron | combining cedilla | combining caron |
| ring/dot above | combining ring above | combining dot above |

This is a trial to replace the Diacritics layer above (arguably breaks home-row symmetry by living on the `N` key) — if it earns its keep, Diacritics may retire.

---

## Quick index — "where's that character?"

### French accents
| Char | Where |
|---|---|
| ù à é | Default layer, plain keys |
| è | Default layer, `.`/`è` key (row 2) |
| ç | Default layer, `⌥ C` |
| æ ô œ | Diacritics layer, plain keys |
| â | Diacritics layer, plain key |
| î / ï | Diacritics layer, tap / `⌥` |
| ê / ë | Diacritics layer, tap / `⌥` |
| û / ü | Diacritics layer, tap / `⌥` |
| y / ÿ | Diacritics layer, tap / `⌥` |

### Greek letters & variants
All on the **Greek layer**. Base forms are plain taps; θ, φ, ε, κ, π, ρ, σ also have an `⌥` (alt-tap) variant form (vartheta ϑ, varphi ϕ, varepsilon ϵ, varkappa ϰ, varpi ϖ, varrho ϱ, varsigma/final-sigma ς).

### Punctuation with hidden forms (default layer position, unless noted)
| Key | Tap | Alt+tap | Shift+tap |
|---|---|---|---|
| `'` | `'` | `"` | `&#96;` |
| `/` | `/` | `&#124;` | `\` |
| `-` | `-` | `~` | `_` |
| `,` | `,` | | `;` |
| `.` | `.` | | `:` |
| `?` | `?` | | `!` |

### Math & symbols (Symbol layer)
| Key | Tap | Alt+tap | Shift+tap |
|---|---|---|---|
| `<` | `<` | `⟨` | `«` |
| `>` | `>` | `⟩` | `»` |
| `*` | `*` | `×` | `†` |
| `+` | `+` | | `±` |
| `=` | `=` | `≈` | `≠` |
| — | `√` | | (plain key, no modifier) |

### Editing / navigation (Navigation layer)
Undo `⌃Z` · Redo `⌃Y` · Cut `⌃X` · Copy `⌃C` · Paste `⌃V` · Home · End · Page Up · Page Down · arrow keys · media transport (volume/mute/play-pause/track skip)

### Any letter + an accent (Accent layer, trial)
Hold **Del**, tap one of: circumflex/diaeresis · grave/acute · tilde/macron · cedilla/caron · ring/dot-above. Works after *any* letter, including combinations with no precomposed Unicode form (n̂, ǧ, ȭ...). Type the letter first, accent second.
