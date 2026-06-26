import os

with open('/Users/calexander/writing-system-for-ai/LANGUAGE.md', 'r') as f:
    content = f.read()

# 1. Update Title and Name
content = content.replace('# The Notation — language specification, v0.1', '# Alan — language specification, v1.0')
content = content.replace('*A universal writing system for meaning, shared by humans and machines. Working name TBD.*', '*A universal writing system for meaning, shared by humans and machines.*')

# 2. Update the "FIX FIRST" warning, as it is now fixed
warning_old = "> **⚠ FIX FIRST (operator note):** the current notation is **too bracket-heavy — more complex than C, C++, or assembly.** That is disqualifying; the entire promise is *legibility*. Priority #1 for the next pass is a **flatter surface syntax**: far fewer brackets and nesting, ideally readable left-to-right like a sentence rather than a parse tree. Redesign the serialization (§1 and rule N6 in §4) before extending the lexicon. The reader should never have to count brackets."
warning_new = "> **✓ SOLVED (Visual Syntax):** The old bracket-heavy syntax has been completely abandoned. Alan now utilizes a **vertical, layout-driven visual grammar**. Structural brackets have been replaced by spatial indentation, and English semantic role labels (`agt`, `pat`) have been replaced by pure geometric connectors. The reader never counts brackets; they simply read the logical graph."
content = content.replace(warning_old, warning_new)

# 3. Update Section 1 to reflect the new visual syntax
sec1_old = """A **form** is a predicate applied to named role-slots:

```
[ PRED  role:arg  role:arg  … ]
```

- `PRED` is a **prime** (§2) or a **registered term** (§3).
- each `role:` is drawn from a small fixed set (§3.1).
- an `arg` is an entity, a value, or another `[ … ]` (forms nest).

Examples:
```
[ ⊳  agt:◉  pat:◎ ]                         I see you.
[ ⟿  agt:◉  rec:◎  res:[ ⊢ agt:◎ pat:▷ ] ]   I want you to know this.
```"""

sec1_new = """A **form** is a predicate applied to arguments using strict canonical ordering and spatial layout:

- `PRED` is a **prime** (§2) or a **Macro-Concept** (§3).
- `arg` is an entity, a value, or a nested predicate.
- Structural connections (roles) are implied by the strict vertical cascading order (Canonical Order) or denoted by geometric role connectors, completely removing the need for English abbreviations like `agt` or `pat`.

Example: "I want you to know this."
```
◇ (WANT)
├── ◉ (I)
└── ✲ (KNOW)
    ├── ◎ (YOU)
    └── ▷ (THIS)
```"""
content = content.replace(sec1_old, sec1_new)

# 4. Update Section 2 (The primes) to reflect the completed geometric typology
sec2_old_start = "The basis is the set of **semantic primes** — meanings that (a) cannot be defined without circularity and (b) have an exponent in every human language. This is not invented: it is the **Natural Semantic Metalanguage** inventory (Goddard & Wierzbicka), ~65 primes, mapped to one glyph + one ASCII handle each. The glyph is canonical (no alphabet, no accent); the handle is a typing aid with a 1:1 mapping."
sec2_new_start = """The basis is the set of **semantic primes** — meanings that (a) cannot be defined without circularity and (b) have an exponent in every human language. This is the **Natural Semantic Metalanguage** inventory, completely realized into a unified **Geometric Typology**:

- **Entities (Circles):** Me, You, Someone, Something.
- **Actions (Triangles):** Do, Happen, Move, Live, Die.
- **Mental (Diamonds):** Think, Know, Want, Feel.
- **Descriptors (Squares):** Good, Bad, Big, Small.
- **Macro-Concepts (Hexagons/Polygons):** Universe/God, System, Law, Computation.

Semantic opposites act like **matter and anti-matter**: flipping a symbol vertically or horizontally mathematically derives its exact opposite (e.g., Live ▲ / Die ▼)."""

# We'll just replace the introductory paragraph of Section 2 and drop the outdated table note.
idx2 = content.find("The basis is the set of **semantic primes**")
idx3 = content.find("## 3. Non-primes, roles, and marks")
if idx2 != -1 and idx3 != -1:
    content = content[:idx2] + sec2_new_start + "\n\n" + content[idx3:]


# 5. Update Open Design Decisions since they are answered
open_decisions = """## 6. Open design decisions (your call — these are real forks)

1. **Glyph-assignment policy for the remaining ~40 primes.** Pictographic (meaning-suggestive), arbitrary-but-memorable, or systematic (shape encodes category)? This sets the whole visual character.
2. **Decomposition depth.** Do registered terms (ADMIN, Account) always decompose to primes (purest, verbose), or may they stay as opaque typed terms with a registered definition (practical)? Affects how "universal" vs "domain" the form is.
3. **Canonical surface = glyphs or handles?** Glyphs are accent-free and language-neutral (matches the identity); ASCII handles are typable everywhere today. I propose: **glyphs are canonical, handles are the input method** (an IME maps `wnt`→`⟿`). Confirm.
4. **The name.** It needs one."""

resolved_decisions = """## 6. Resolved Design Decisions

1. **Glyph-assignment policy:** Systematic. Shape encodes category (Circles=Entities, Triangles=Actions). Opposites are derived via geometric reflection (Matter/Anti-Matter).
2. **Decomposition depth:** Complex concepts use **Macro-Radicals**. For instance, 'Angel' is composed of the Universe Hexagon + the 'Above' modifier. This avoids deep recursive explication while maintaining pure visual logic.
3. **Canonical surface:** Glyphs are canonical. A dedicated mechanical (and virtual) keyboard interface has been mapped to these glyphs, confirming that they can be typed directly.
4. **The name:** The language is named **Alan**, honoring Alan Turing. It uses a composite Turing glyph (Pentagon + Computation Block) as its official symbol."""

content = content.replace(open_decisions, resolved_decisions)

with open('/Users/calexander/writing-system-for-ai/LANGUAGE.md', 'w') as f:
    f.write(content)

print("SUCCESS updating LANGUAGE.md")
