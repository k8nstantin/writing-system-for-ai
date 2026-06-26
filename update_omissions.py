import re

with open('/Users/calexander/writing-system-for-ai/index.html', 'r') as f:
    content = f.read()

# 1. Update the glyphfield background
old_glyphfield = '<div class="glyphfield" aria-hidden="true">◉ ◎ ○ □ ◇ ▷ ≡ ∀ ∃ ⋙ ⊢ ✲ ⟿ ⊳ ⟪ ▶ ⇡ ⊨ ⊇ ¬ ∵ ◉ ◎ ○ □ ◇ ▷ ≡ ∀ ∃ ⋙ ⊢ ✲ ⟿ ⊳ ⟪ ▶ ⇡ ⊨ ⊇ ¬ ∵ ◉ ◎ ○ □ ◇ ▷ ≡ ∀ ∃ ⋙ ⊢ ✲ ⟿ ⊳ ⟪ ▶ ⇡ ⊨ ⊇ ¬ ∵</div>'
new_glyphfield = '<div class="glyphfield" aria-hidden="true">◉ ◎ ○ □ ◇ ▷ ⬡ ⬢ ∀ ∃ ⋙ ◼ ⧄ ▲ ▼ ⇿ || ∧ ∨ ⧖ ◉ ◎ ○ □ ◇ ▷ ⬡ ⬢ ∀ ∃ ⋙ ◼ ⧄ ▲ ▼ ⇿ || ∧ ∨ ⧖ ◉ ◎ ○ □ ◇ ▷ ⬡ ⬢ ∀ ∃ ⋙ ◼ ⧄ ▲ ▼ ⇿ || ∧ ∨ ⧖</div>'
content = content.replace(old_glyphfield, new_glyphfield)

# 2. Update the "See it in motion" drift section to use the visual layout indent style
old_drift = """        <p class="hop" data-h="0">A: [ SET-STATE … ∧ role≠ADMIN … since @2026-03-20 ]</p>
        <p class="hop" data-h="1">B: [ SET-STATE … identical … ]</p>
        <p class="hop" data-h="2">C: [ SET-STATE … identical … ]</p>"""

new_drift = """        <div class="hop" data-h="0" style="font-family: monospace; white-space: pre; line-height: 1.3;">A: SET-STATE
   ├── ACCOUNT (∀)
   ├── ⧄ (LOGIN)
   │   └── TIM: @2026-03-20
   └── ⧄ (ADMIN)</div>
        <p class="hop" data-h="1" style="font-family: monospace;">B: <em>... identical logical graph ...</em></p>
        <p class="hop" data-h="2" style="font-family: monospace;">C: <em>... identical logical graph ...</em></p>"""
content = content.replace(old_drift, new_drift)

with open('/Users/calexander/writing-system-for-ai/index.html', 'w') as f:
    f.write(content)

# Now update LANGUAGE.md
with open('/Users/calexander/writing-system-for-ai/LANGUAGE.md', 'r') as f:
    lang_content = f.read()

# Remove the old roles section
old_roles = """### 3.1 Roles (closed set — fixed order, see N2)
`agt` agent · `exp` experiencer · `pat` patient · `rec` recipient · `res` result/complement · `ins` instrument · `src` source · `gol` goal · `tim` time · `loc` place · `man` manner · `cau` cause · `pur` purpose

The role set is **closed**. New predicates reuse these slots; they never invent roles.

### 3.2 Entities & reference (this retires "the")"""

new_roles = """### 3.1 Structural Connections (Roles)
English semantic role labels (`agt`, `pat`, `res`) are completely abandoned. Roles are established purely through **Canonical Order** in the vertical layout or through specific geometric connective lines (e.g., an arrow with a solid root for the doer, an arrow hitting a wall for the receiver).

### 3.2 Entities & reference (this retires "the")"""
lang_content = lang_content.replace(old_roles, new_roles)

# Fix N2
old_n2 = """- **N2 · Canonical role order.** Within a predicate, roles serialize in the fixed global order of §3.1 — *regardless of source word order.* So `I see you` and `you are seen by me` normalize to the **same** form."""
new_n2 = """- **N2 · Canonical Cascading Order.** Within a predicate, arguments cascade vertically in a strict, globally fixed order (Doer → Receiver → Manner/Result) — *regardless of source word order.* So `I see you` and `you are seen by me` normalize to the **exact same** vertical graph."""
lang_content = lang_content.replace(old_n2, new_n2)

# Fix N6
old_n6 = """- **N6 · One serialization.** Exactly one spacing/bracketing rule (`[ P role:arg ]`, single spaces, no trailing). No formatting freedom."""
new_n6 = """- **N6 · One visualization.** Exactly one layout rule: geometric predicates on the left, arguments indented vertically below. No formatting freedom. No text-based brackets."""
lang_content = lang_content.replace(old_n6, new_n6)

# Fix Worked Examples
old_examples = """## 5. Worked examples

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
```"""

new_examples = """## 5. Worked examples

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
▲ (MOVE)
├── ○ (SOMEONE °)
└── ⧄ (INSIDE)
∧ (AND)
▲ (SAY)
├── ↺ (Aforementioned SOMEONE)
└── □ (SOMETHING °)
```"""
lang_content = lang_content.replace(old_examples, new_examples)

with open('/Users/calexander/writing-system-for-ai/LANGUAGE.md', 'w') as f:
    f.write(lang_content)

print("SUCCESS fixing omissions")
