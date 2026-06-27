# Alan — language specification, v1.0

*A universal writing system for meaning, shared by humans and machines.*

The whole design rests on one invariant:

> **One meaning has exactly one written form.** Re-emitting a form is therefore the identity — `T(x) = x` — so meaning cannot drift as it passes between people and machines.

That invariant is not a hope; it is produced by the **normalization rules** in §4. Everything else (the primes, the grammar) is in service of them. Humans keep their own language; a model compiles English ⇄ this form and back. The form is the shared record both sides read and trust.

> **✓ SOLVED (Visual Syntax):** The old bracket-heavy syntax has been completely abandoned. Alan now utilizes a **vertical, layout-driven visual grammar**. Structural brackets have been replaced by spatial indentation, and English semantic role labels (`agt`, `pat`) have been replaced by pure geometric connectors. The reader never counts brackets; they simply read the logical graph.

---

## 1. What a form looks like

A **form** is a predicate applied to arguments using strict canonical ordering and spatial layout:

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
```

---

## 2. The primes (the basis)

The basis is the set of **semantic primes** — meanings that (a) cannot be defined without circularity and (b) have an exponent in every human language. This is the **Natural Semantic Metalanguage** inventory, completely realized into a unified **Geometric Typology**:

- **Entities (Circles):** Me, You, Someone, Something.
- **Actions (Triangles):** Do, Happen, Move, Live, Die.
- **Mental (Diamonds):** Think, Know, Want, Feel.
- **Descriptors (Squares):** Good, Bad, Big, Small.
- **Macro-Concepts (Hexagons/Polygons):** Universe/God, System, Law, Computation.

Semantic opposites act like **matter and anti-matter**: flipping a symbol vertically or horizontally mathematically derives its exact opposite (e.g., Live ▲ / Die ▼).

## 3. Non-primes, roles, and marks

### 3.1 Structural Connections (Roles)
English semantic role labels (`agt`, `pat`, `res`) are completely abandoned. Roles are established purely through **Canonical Order** in the vertical layout or through specific geometric connective lines (e.g., an arrow with a solid root for the doer, an arrow hitting a wall for the receiver).

### 3.2 Entities & reference (this retires "the")
- `⟦T⟧°` — introduce a **new** entity of type `T`.
- `⟦T⟧↺` — refer to an **already-introduced** entity (definiteness is structural — no articles).
- Entities carry indices assigned by N4.

### 3.3 Non-primes by explication (the generative lexicon)
Concepts beyond the basis are **defined**, never assumed:
```
ADMIN ≔ [ ⟦Account⟧ : role = (qen do: manage-system) ]
```
A registered term is shared, not paraphrased: everyone uses `ADMIN`, no one re-invents it. The dictionary is **generated from the basis, not stored** (millions of words, one small basis — like chemistry from ~100 elements).

### 3.4 Logic & quantifiers
`∧ ∨ ⇒ ⟺` over forms · `∀ ∃` + numerals over entity variables · `¬` negates a form.

### 3.5 Marks (uncertainty is first-class)
- `⟨?⟩` — a **hole**: a required value is missing. The compiler must ask; it may not guess.
- `⟨≈ v⟩` — an **assumption**: a value the compiler supplied. Surfaced for confirmation, never hidden.

---

## 4. Normalization — why one meaning has one form (the core)

A form is **canonical** iff all of these hold. The compiler emits only canonical forms; two writers (or one model run twice) who mean the same thing produce **byte-identical** output.

- **N1 · One word per meaning.** Every concept is written with its single assigned glyph or registered term. No synonyms, no spelling variants. (Synonyms are resolved to the canonical entry on the way in.)
- **N2 · Canonical Cascading Order.** Within a predicate, arguments cascade vertically in a strict, globally fixed order (Doer → Receiver → Manner/Result) — *regardless of source word order.* So `I see you` and `you are seen by me` normalize to the **exact same** vertical graph.
- **N3 · Commutative operands sorted.** Arguments of `∧ ∨` and unordered sets are flattened and sorted by canonical key (sub-form, by glyph code point). `A ∧ B` and `B ∧ A` are one form.
- **N4 · Deterministic entity indexing.** Entities are numbered by first appearance in a fixed pre-order traversal; `↺` references use those indices. Same referent-graph → same indices, always.
- **N5 · No function words.** No articles, no agreement, no filler. Definiteness lives in `°`/`↺`; tense lives in `tim:`.
- **N6 · One visualization.** Exactly one layout rule: geometric predicates on the left, arguments indented vertically below. No formatting freedom. No text-based brackets.
- **N7 · Maximal shared decomposition.** Registered terms resolve to their explication; two forms that decompose to the same prime structure **are** the same form.
- **N8 · Explicit gaps.** Missing required role → `⟨?⟩`. Supplied default → `⟨≈ v⟩`. Never silently omitted, never silently guessed.

**Consequence:** the normal form is unique per meaning ⇒ `T(form) = form`. Broken phone is not "rarer" — it is structurally impossible.

---

## 5. Worked examples

**Normalization (two English phrasings → one form):**
```
"I see you."             ┐
"You are seen by me."    ┘ →  ◇ (SEE)
                              ├── ◉ (I)
                              └── ◎ (YOU)
```

**Reference & negation:**
```
"A person came in; the person said something."
↔ (MOVE)
├── ○ (SOMEONE °)
└── 回 (INSIDE)
∧ (AND)
▷ (SAY)
├── ↺ (Aforementioned SOMEONE)
└── ⊖ (SOMETHING °)
```
Re-emit it through ten agents → identical, character for character. The two `⟨≈⟩` marks are the only things the compiler assumed; they are shown, not hidden.

---

## 6. Resolved Design Decisions

1. **Glyph-assignment policy:** Systematic. Shape encodes category (Circles=Entities, Triangles=Actions). Opposites are derived via geometric reflection (Matter/Anti-Matter).
2. **Decomposition depth:** Complex concepts use **Macro-Radicals**. For instance, 'Angel' is composed of the Universe Hexagon + the 'Above' modifier. This avoids deep recursive explication while maintaining pure visual logic.
3. **Canonical surface:** Glyphs are canonical. A dedicated mechanical (and virtual) keyboard interface has been mapped to these glyphs, confirming that they can be typed directly.
4. **The name:** The language is named **Alan**, honoring Alan Turing. It uses a composite Turing glyph (Pentagon + Computation Block) as its official symbol.

---

*v1.0 — the first formulation, not the last. The grammar (§1–3) and the normalization law (§4) are the load-bearing parts; the glyph table is finishable work.*
