# The Notation — language specification, v0.1

*A universal writing system for meaning, shared by humans and machines. Working name TBD.*

The whole design rests on one invariant:

> **One meaning has exactly one written form.** Re-emitting a form is therefore the identity — `T(x) = x` — so meaning cannot drift as it passes between people and machines.

That invariant is not a hope; it is produced by the **normalization rules** in §4. Everything else (the primes, the grammar) is in service of them. Humans keep their own language; a model compiles English ⇄ this form and back. The form is the shared record both sides read and trust.

> **⚠ FIX FIRST (operator note):** the current notation is **too bracket-heavy — more complex than C, C++, or assembly.** That is disqualifying; the entire promise is *legibility*. Priority #1 for the next pass is a **flatter surface syntax**: far fewer brackets and nesting, ideally readable left-to-right like a sentence rather than a parse tree. Redesign the serialization (§1 and rule N6 in §4) before extending the lexicon. The reader should never have to count brackets.

---

## 1. What a form looks like

A **form** is a predicate applied to named role-slots:

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
```

---

## 2. The primes (the basis)

The basis is the set of **semantic primes** — meanings that (a) cannot be defined without circularity and (b) have an exponent in every human language. This is not invented: it is the **Natural Semantic Metalanguage** inventory (Goddard & Wierzbicka), ~65 primes, mapped to one glyph + one ASCII handle each. The glyph is canonical (no alphabet, no accent); the handle is a typing aid with a 1:1 mapping.

**Assigned so far (the specimen — frozen):**

| | | | | | |
|---|---|---|---|---|---|
| ◉ `me` I | ◎ `yu` you | ○ `qen` someone | □ `ren` something | ◇ `kind` kind | ▷ `dei` this |
| ≡ `sam` the same | ∀ `al` all | ∃ `som` some | ⋙ `mor` much/many | ⊢ `noe` know | ✲ `tnk` think |
| ⟿ `wnt` want | ⊳ `see` see | ⟪ `sai` say | ▶ `do` do | ⇡ `hap` happen | = `is` be |
| ⊨ `ex` there-is | ⊇ `hav` have | + `gud` good | − `bad` bad | ¬ `not` not | ∵ `bik` because |

**Remaining NSM primes — handles fixed, glyphs to assign (open task):**
`ppl` people · `bod` body · `part` part · `oth` other/else · `one` `two` · `few` little · `big` · `sml` small · `fel` feel · `her` hear · `wrd` words · `tru` true · `mov` move · `liv` live · `die` die · `tim` when/time · `now` · `bef` before · `aft` after · `lng` a-long-time · `mom` moment · `loc` where/place · `here` · `abv` above · `blw` below · `far` · `near` · `side` · `in` inside · `tch` touch · `may` maybe · `can` can · `if` · `vry` very · `lik` like/as

> Glyphs for the remaining set is a deliberate, finite task — not open-ended. Two people don't get to invent symbols; they look them up. (This is what killed every prior attempt — and why it's a fixable engineering job, not a mystery.)

---

## 3. Non-primes, roles, and marks

### 3.1 Roles (closed set — fixed order, see N2)
`agt` agent · `exp` experiencer · `pat` patient · `rec` recipient · `res` result/complement · `ins` instrument · `src` source · `gol` goal · `tim` time · `loc` place · `man` manner · `cau` cause · `pur` purpose

The role set is **closed**. New predicates reuse these slots; they never invent roles.

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
- **N2 · Canonical role order.** Within a predicate, roles serialize in the fixed global order of §3.1 — *regardless of source word order.* So `I see you` and `you are seen by me` normalize to the **same** form.
- **N3 · Commutative operands sorted.** Arguments of `∧ ∨` and unordered sets are flattened and sorted by canonical key (sub-form, by glyph code point). `A ∧ B` and `B ∧ A` are one form.
- **N4 · Deterministic entity indexing.** Entities are numbered by first appearance in a fixed pre-order traversal; `↺` references use those indices. Same referent-graph → same indices, always.
- **N5 · No function words.** No articles, no agreement, no filler. Definiteness lives in `°`/`↺`; tense lives in `tim:`.
- **N6 · One serialization.** Exactly one spacing/bracketing rule (`[ P role:arg ]`, single spaces, no trailing). No formatting freedom.
- **N7 · Maximal shared decomposition.** Registered terms resolve to their explication; two forms that decompose to the same prime structure **are** the same form.
- **N8 · Explicit gaps.** Missing required role → `⟨?⟩`. Supplied default → `⟨≈ v⟩`. Never silently omitted, never silently guessed.

**Consequence:** the normal form is unique per meaning ⇒ `T(form) = form`. Broken phone is not "rarer" — it is structurally impossible.

---

## 5. Worked examples

**Normalization (two English phrasings → one form):**
```
"I see you."             ┐
"You are seen by me."    ┘ →  [ ⊳  agt:◉  pat:◎ ]      (N2 fixes role order)
```

**Reference & negation:**
```
"A person came in; the person said something."
[ mov  agt:⟦qen⟧°  gol:(in) ]  ∧  [ ⟪  agt:⟦qen⟧↺  pat:⟦ren⟧° ]
```

**The admins instruction (with explication + marks):**
```
[ SET-STATE
    pat:  ⟦Account⟧° ∀  where ( ¬[ LOGIN tim: since @2026-03-20 ⟨≈ "last spring"⟩ ] ∧ role ≠ ADMIN )
    res:  state = INACTIVE
    loc:  ⟨≈ ∀ ⟦Tenant⟧ ⟩ ]
```
Re-emit it through ten agents → identical, character for character. The two `⟨≈⟩` marks are the only things the compiler assumed; they are shown, not hidden.

---

## 6. Open design decisions (your call — these are real forks)

1. **Glyph-assignment policy for the remaining ~40 primes.** Pictographic (meaning-suggestive), arbitrary-but-memorable, or systematic (shape encodes category)? This sets the whole visual character.
2. **Decomposition depth.** Do registered terms (ADMIN, Account) always decompose to primes (purest, verbose), or may they stay as opaque typed terms with a registered definition (practical)? Affects how "universal" vs "domain" the form is.
3. **Canonical surface = glyphs or handles?** Glyphs are accent-free and language-neutral (matches the identity); ASCII handles are typable everywhere today. I propose: **glyphs are canonical, handles are the input method** (an IME maps `wnt`→`⟿`). Confirm.
4. **The name.** It needs one.

---

*v0.1 — the first formulation, not the last. The grammar (§1–3) and the normalization law (§4) are the load-bearing parts; the glyph table is finishable work.*
