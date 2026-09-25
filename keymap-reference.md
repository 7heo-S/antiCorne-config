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

**Combos** (all default layer only, released by holding both keys within a short window):
- **U** (left) + **T** (right) → toggles **Caps Word** (auto-releases at the next word break).
- **A** + **E** → **æ**.
- **O** + **E** → **œ** — same column, different row (both likely the same finger), so this one has a longer timeout than the other two to give that roll more room.

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
| — | **%** | **&** | **$** | **^** | **[** | | | **]** | **7** | **8** | **9** | **#** | — |
| **/**<br>⌥`&#124;` ⇧`\` | **√** | **+**<br>⇧`±` | **=**<br>⌥`≈` ⇧`≠` | **\***<br>⌥`×` ⇧`†` | **(** | | | **)** | **4**<br>⇧ | **5**<br>⌃ | **6**<br>⌥ | **0** | — |
| — | **@** | **<**<br>⌥`⟨` ⇧`«` | **-**<br>⌥`~` ⇧`_` | **>**<br>⌥`⟩` ⇧`»` | **{** | | | **}** | **1** | **2** | **3** | **.** | **,** |

Thumbs: **Esc** · **Tab** · **Space** — — · **Enter** · **Del**

`4`/`5`/`6` are home-row mods (same as `T`/`S`/`R` on the default layer). `^` sits on the `é` key's physical position — deliberately, to match the Accent layer's circumflex key at the same spot (see Layer 6).

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

## Layer 6 — Accent

Held with **Del** (right thumb). Two different kinds of key on this layer:

- **Letter positions** — tap directly for the precomposed circumflex form of that letter, *if one exists*. 12 do here: A, E, G, H, I, J, O, S, U, W, Y, Z. (C also has one — ĉ — but its slot went to cedilla instead, see below.) Of the 26 Latin letters, exactly **13 have no precomposed circumflex codepoint at all, in any font** (verified against Unicode, not guessed) — this isn't a gap in the layer, it's a gap in Unicode itself. 8 of these 12 (A, E, H, I, O, U, W, Y) *also* have a precomposed diaeresis, so those are Alt-tap for the second form — same pattern as the Diacritics layer's `e_hat`/`i_hat`/`u_hat` (E/I/U here literally reuse those same three behaviors). G, J, S, Z have no diaeresis codepoint either, so they stay circumflex-only.
- **6 other positions** — combining marks (U+0300 block) instead of a replacement letter. Type the base letter **first**, then hold Del and tap one of these — it visually fuses onto whatever you just typed, so it works on **any** letter, including all 13 that have no precomposed circumflex (e.g. `n` + circumflex → n̂). 3 of these 6 carry a second mark on Shift.

| | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| — | — | **ĵ** | **ô**<br>⌥`ö` | **^**<br>⇧`ˇ` | — | | | — | — | — | **&#96;** | — | — |
| — | **â**<br>⌥`ä` | **î**<br>⌥`ï` | **ê**<br>⌥`ë` | **û**<br>⌥`ü` | **´** | | | — | — | **ŝ** | — | — | — |
| **¯**<br>⇧`~` | — | **ŷ**<br>⌥`ÿ` | — | **˙**<br>⇧`¨` | **ŵ**<br>⌥`ẅ` | | | **ĝ** | **¸** | — | **ĥ**<br>⌥`ḧ` | — | **ẑ** |

Thumbs: **Esc** · **Tab** · **Space** — **Bspc** · **Enter** · —

| Key | Meaning | Tap | Shift+tap |
|---|---|---|---|
| `é` position | circumflex / caron | combining circumflex | combining caron |
| `,` position | acute | combining acute | — |
| `'` position | grave | combining grave | — |
| `-` position | macron / tilde | combining macron | combining tilde |
| `.` position | dot above / diaeresis | combining dot above | combining diaeresis |
| `ç`/`C` position | cedilla | combining cedilla | — |

The `é`-position circumflex key deliberately shares its physical spot with the Symbol layer's `^` (see Layer 1 note) — same finger, same meaning, different layer. `?` (where circumflex used to live) is now free (`&none`).

This was a trial to replace the N-key Diacritics layer above — arguably breaks home-row symmetry by living there, and this layer now covers noticeably more ground: 12 direct letters instead of 5 (each with its own diaeresis Alt-tap where one exists, same as Diacritics), plus universal combining-mark fallback for everything else, plus grave/acute/macron/tilde/cedilla/caron that Diacritics never had at all. Diacritics hasn't been removed, but is a likely retirement candidate.

---

## Quick index — "where's that character?"

### French accents
| Char | Where |
|---|---|
| ù à é | Default layer, plain keys |
| è | Default layer, `.`/`è` key (row 2) |
| ç | Default layer, `⌥ C` (as a letter) — general combining cedilla is also on the Accent layer, at the same `C` position |
| æ | **A**+**E** combo (default layer), or Diacritics layer plain key |
| œ | **O**+**E** combo (default layer), or Diacritics layer plain key |
| ê/ë î/ï û/ü | Both layers, same tap/`⌥` pattern — Accent's E/I/U positions literally reuse Diacritics' `e_hat`/`i_hat`/`u_hat` behaviors |
| â / ä | â on both layers; **ä is Accent-only** (Diacritics' `â` key has no diaeresis Alt-tap) |
| ô / ö | ô on both layers; **ö is Accent-only** (same story as ä) |
| y / ÿ | Diacritics layer, tap / `⌥` — or Accent layer's `Y` position, same tap/`⌥` pattern |
| ĵ ŝ ĝ ẑ | Accent layer letter positions only — circumflex, no diaeresis form exists for these |
| ŷ/ÿ ŵ/ẅ ĥ/ḧ | Accent layer letter positions only — tap/`⌥` pattern, Esperanto/Welsh/transliteration letters, not French, but free via the same mechanism |

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

### Any letter + an accent (Accent layer)
Hold Del, then either tap a letter position directly (A, E, G, H, I, J, O, S, U, W, Y, Z give a precomposed circumflex form), or type the letter first and then hold Del and tap: acute (comma position), grave (quote position), circumflex / shift for caron (e-acute position), macron / shift for tilde (dash position), dot-above / shift for diaeresis (dot position), or cedilla (C position). The combining-mark keys work after any letter, including ones with no precomposed form at all (n + circumflex, etc).
