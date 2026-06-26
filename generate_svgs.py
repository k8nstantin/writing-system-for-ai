import os

html_start = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Characteristica Reborn - Full Glyph Set</title>
<style>
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    background-color: #f5f5f5;
    color: #333;
    display: flex;
    justify-content: center;
    padding: 40px;
  }
  .container {
    background: white;
    padding: 40px;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    max-width: 900px;
    width: 100%;
  }
  h1 { color: #111; margin-bottom: 5px; }
  p.subtitle { color: #666; margin-bottom: 40px; }
  h2 {
    color: #333;
    border-bottom: 2px solid #eee;
    padding-bottom: 8px;
    margin-top: 40px;
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
    gap: 20px;
    margin-top: 20px;
  }
  .glyph-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 15px;
    border: 1px solid #e0e0e0;
    border-radius: 6px;
    background: #fafafa;
    transition: transform 0.2s, box-shadow 0.2s;
  }
  .glyph-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    border-color: #ccc;
  }
  .glyph-card svg {
    width: 48px;
    height: 48px;
    margin-bottom: 10px;
  }
  .label {
    font-family: monospace;
    font-size: 15px;
    font-weight: bold;
    color: #222;
  }
  .meaning {
    font-size: 12px;
    color: #666;
    margin-top: 4px;
    text-align: center;
  }
</style>
</head>
<body>

<div class="container">
  <h1>Characteristica Visual Grammar</h1>
  <p class="subtitle">The complete dictionary of ~65 Natural Semantic Metalanguage (NSM) primes, mapped to a unified visual typology. All glyphs share a consistent visual language, bound to a 24x24 grid with uniform stroke weight.</p>
"""

categories = [
    {
        "name": "Macro-Concepts (Complex Geometry)",
        "glyphs": [
            {"handle": "unv", "desc": "universe / all things", "svg": '<polygon points="12,2 21,7 21,17 12,22 3,17 3,7" /><circle cx="12" cy="12" r="3" fill="#333" />'},
            {"handle": "sys", "desc": "system / structure", "svg": '<polygon points="12,2 22,9 18,20 6,20 2,9" />'},
            {"handle": "law", "desc": "law / absolute rule", "svg": '<polygon points="9,2 15,2 22,9 22,15 15,22 9,22 2,15 2,9" stroke-width="3" />'},
        ]
    },
    {
        "name": "Entities (Substantives) — Base: Circle",
        "glyphs": [
            {"handle": "me", "desc": "I / self", "svg": '<circle cx="12" cy="12" r="10" /><circle cx="12" cy="12" r="4" fill="#333" />'},
            {"handle": "yu", "desc": "you / other", "svg": '<circle cx="12" cy="12" r="10" /><circle cx="12" cy="12" r="4" />'},
            {"handle": "qen", "desc": "someone", "svg": '<circle cx="12" cy="12" r="10" />'},
            {"handle": "ren", "desc": "something", "svg": '<circle cx="12" cy="12" r="10" /><line x1="6" y1="12" x2="18" y2="12" />'},
            {"handle": "ppl", "desc": "people", "svg": '<circle cx="12" cy="12" r="10" /><circle cx="12" cy="7" r="1.5" fill="#333"/><circle cx="8" cy="14" r="1.5" fill="#333"/><circle cx="16" cy="14" r="1.5" fill="#333"/>'},
            {"handle": "bod", "desc": "body", "svg": '<circle cx="12" cy="12" r="10" /><line x1="12" y1="2" x2="12" y2="22" />'},
        ]
    },
    {
        "name": "Actions (Events) — Base: Triangle",
        "glyphs": [
            {"handle": "do", "desc": "do / active", "svg": '<polygon points="6,20 18,12 6,4" />'},
            {"handle": "hap", "desc": "happen", "svg": '<polygon points="4,6 20,6 12,18" />'},
            {"handle": "mov", "desc": "move", "svg": '<line x1="4" y1="12" x2="20" y2="12" /><polyline points="14,6 20,12 14,18" /><line x1="6" y1="12" x2="10" y2="12" stroke="#fff" stroke-width="4"/>'},
            {"handle": "liv", "desc": "live", "svg": '<polygon points="12,4 4,20 20,20" /><circle cx="12" cy="14" r="2" fill="#333"/>'},
            {"handle": "die", "desc": "die", "svg": '<polygon points="12,20 4,4 20,4" /><circle cx="12" cy="10" r="2" fill="#333"/>'},
        ]
    },
    {
        "name": "Mental Predicates — Base: Diamond",
        "glyphs": [
            {"handle": "tnk", "desc": "think", "svg": '<polygon points="12,2 22,12 12,22 2,12" /><circle cx="12" cy="12" r="2" fill="#333" />'},
            {"handle": "noe", "desc": "know", "svg": '<polygon points="12,2 22,12 12,22 2,12" fill="#333"/>'},
            {"handle": "wnt", "desc": "want", "svg": '<polygon points="12,2 22,12 12,22 2,12" /><line x1="12" y1="12" x2="24" y2="12" /><polyline points="20,8 24,12 20,16" />'},
            {"handle": "fel", "desc": "feel", "svg": '<polygon points="12,2 22,12 12,22 2,12" /><path d="M 8 12 Q 10 8 12 12 T 16 12" />'},
            {"handle": "see", "desc": "see", "svg": '<polygon points="12,2 22,12 12,22 2,12" /><path d="M 7 12 Q 12 7 17 12 Q 12 17 7 12" />'},
            {"handle": "her", "desc": "hear", "svg": '<polygon points="12,2 22,12 12,22 2,12" /><path d="M 12 8 A 4 4 0 0 1 12 16 M 9 10 A 2 2 0 0 1 9 14" />'},
        ]
    },
    {
        "name": "Communication",
        "glyphs": [
            {"handle": "sai", "desc": "say", "svg": '<path d="M 4 12 L 12 4 A 10 10 0 0 1 12 20 Z" />'},
            {"handle": "wrd", "desc": "words", "svg": '<line x1="4" y1="8" x2="20" y2="8" /><line x1="4" y1="12" x2="16" y2="12" /><line x1="4" y1="16" x2="20" y2="16" />'},
        ]
    },
    {
        "name": "Descriptors — Base: Square",
        "glyphs": [
            {"handle": "gud", "desc": "good", "svg": '<rect x="4" y="4" width="16" height="16" /><polyline points="8,14 12,9 16,14" />'},
            {"handle": "bad", "desc": "bad", "svg": '<rect x="4" y="4" width="16" height="16" /><polyline points="8,10 12,15 16,10" />'},
            {"handle": "big", "desc": "big", "svg": '<rect x="2" y="2" width="20" height="20" stroke-width="4" />'},
            {"handle": "sml", "desc": "small", "svg": '<rect x="10" y="10" width="4" height="4" fill="#333" />'},
            {"handle": "tru", "desc": "true", "svg": '<rect x="4" y="4" width="16" height="16" fill="#333" />'},
            {"handle": "lik", "desc": "like / as", "svg": '<rect x="4" y="4" width="12" height="12" /><rect x="8" y="8" width="12" height="12" />'},
        ]
    },
    {
        "name": "Quantifiers",
        "glyphs": [
            {"handle": "one", "desc": "one", "svg": '<circle cx="12" cy="12" r="2" fill="#333" />'},
            {"handle": "two", "desc": "two", "svg": '<circle cx="8" cy="12" r="2" fill="#333" /><circle cx="16" cy="12" r="2" fill="#333" />'},
            {"handle": "few", "desc": "few", "svg": '<circle cx="12" cy="8" r="1.5" fill="#333" /><circle cx="7" cy="15" r="1.5" fill="#333" /><circle cx="17" cy="15" r="1.5" fill="#333" />'},
            {"handle": "som", "desc": "some", "svg": '<circle cx="12" cy="12" r="10" stroke-dasharray="4,4" />'},
            {"handle": "mor", "desc": "much / many", "svg": '<circle cx="6" cy="6" r="1.5" fill="#333" /><circle cx="12" cy="6" r="1.5" fill="#333" /><circle cx="18" cy="6" r="1.5" fill="#333" /><circle cx="6" cy="12" r="1.5" fill="#333" /><circle cx="12" cy="12" r="1.5" fill="#333" /><circle cx="18" cy="12" r="1.5" fill="#333" /><circle cx="6" cy="18" r="1.5" fill="#333" /><circle cx="12" cy="18" r="1.5" fill="#333" /><circle cx="18" cy="18" r="1.5" fill="#333" />'},
            {"handle": "al", "desc": "all", "svg": '<circle cx="12" cy="12" r="10" fill="#333" />'},
        ]
    },
    {
        "name": "Time — Base: Horizontal Line",
        "glyphs": [
            {"handle": "tim", "desc": "when / time", "svg": '<line x1="2" y1="12" x2="22" y2="12" /><line x1="12" y1="8" x2="12" y2="16" />'},
            {"handle": "now", "desc": "now", "svg": '<line x1="2" y1="12" x2="22" y2="12" /><line x1="12" y1="6" x2="12" y2="18" stroke-width="4" />'},
            {"handle": "bef", "desc": "before", "svg": '<line x1="2" y1="12" x2="22" y2="12" /><line x1="12" y1="8" x2="12" y2="16" /><polyline points="10,12 6,12" /><polyline points="8,10 6,12 8,14" />'},
            {"handle": "aft", "desc": "after", "svg": '<line x1="2" y1="12" x2="22" y2="12" /><line x1="12" y1="8" x2="12" y2="16" /><polyline points="14,12 18,12" /><polyline points="16,10 18,12 16,14" />'},
            {"handle": "lng", "desc": "a long time", "svg": '<line x1="4" y1="12" x2="20" y2="12" /><polyline points="6,9 2,12 6,15" /><polyline points="18,9 22,12 18,15" />'},
            {"handle": "mom", "desc": "moment", "svg": '<line x1="12" y1="6" x2="12" y2="18" stroke-width="4" />'},
        ]
    },
    {
        "name": "Space — Base: Axes",
        "glyphs": [
            {"handle": "loc", "desc": "where / place", "svg": '<line x1="2" y1="20" x2="22" y2="20" /><line x1="12" y1="20" x2="12" y2="2" /><circle cx="12" cy="12" r="3" fill="#333" />'},
            {"handle": "here", "desc": "here", "svg": '<line x1="2" y1="20" x2="22" y2="20" /><line x1="12" y1="20" x2="12" y2="2" /><circle cx="12" cy="20" r="4" fill="#333" />'},
            {"handle": "abv", "desc": "above", "svg": '<line x1="2" y1="18" x2="22" y2="18" /><polyline points="8,10 12,4 16,10" /><line x1="12" y1="4" x2="12" y2="14" />'},
            {"handle": "blw", "desc": "below", "svg": '<line x1="2" y1="6" x2="22" y2="6" /><polyline points="8,14 12,20 16,14" /><line x1="12" y1="20" x2="12" y2="10" />'},
            {"handle": "far", "desc": "far", "svg": '<line x1="4" y1="4" x2="4" y2="20" /><line x1="20" y1="4" x2="20" y2="20" /><path d="M 6 12 Q 12 18 18 12" stroke-dasharray="2,2" />'},
            {"handle": "near", "desc": "near", "svg": '<line x1="10" y1="4" x2="10" y2="20" /><line x1="14" y1="4" x2="14" y2="20" />'},
            {"handle": "side", "desc": "side", "svg": '<line x1="12" y1="2" x2="12" y2="22" /><rect x="16" y="8" width="6" height="8" fill="#333" />'},
            {"handle": "in", "desc": "inside", "svg": '<rect x="4" y="4" width="16" height="16" /><rect x="9" y="9" width="6" height="6" fill="#333" />'},
            {"handle": "tch", "desc": "touch", "svg": '<rect x="4" y="6" width="8" height="12" /><rect x="12" y="6" width="8" height="12" />'},
        ]
    },
    {
        "name": "Logical, Existence & Core",
        "glyphs": [
            {"handle": "not", "desc": "not", "svg": '<circle cx="12" cy="12" r="10" /><line x1="5" y1="5" x2="19" y2="19" />'},
            {"handle": "may", "desc": "maybe", "svg": '<path d="M 6 12 Q 9 6 12 12 T 18 12" />'},
            {"handle": "can", "desc": "can", "svg": '<path d="M 12 4 A 6 6 0 0 1 18 10 V 20 M 12 4 A 6 6 0 0 0 6 10 V 12 M 6 16 V 20" />'},
            {"handle": "if", "desc": "if", "svg": '<path d="M 12 20 V 12 L 6 4 M 12 12 L 18 4" />'},
            {"handle": "vry", "desc": "very", "svg": '<polygon points="12,2 4,20 20,20" fill="#333" />'},
            {"handle": "is", "desc": "be", "svg": '<line x1="4" y1="9" x2="20" y2="9" /><line x1="4" y1="15" x2="20" y2="15" />'},
            {"handle": "ex", "desc": "there is", "svg": '<line x1="4" y1="20" x2="20" y2="20" /><circle cx="12" cy="16" r="4" fill="#333" />'},
            {"handle": "hav", "desc": "have", "svg": '<circle cx="12" cy="12" r="10" /><circle cx="12" cy="12" r="4" fill="#333" />'},
            {"handle": "sam", "desc": "the same", "svg": '<line x1="4" y1="7" x2="20" y2="7" /><line x1="4" y1="12" x2="20" y2="12" /><line x1="4" y1="17" x2="20" y2="17" />'},
            {"handle": "oth", "desc": "other", "svg": '<circle cx="8" cy="12" r="5" /><rect x="15" y="7" width="10" height="10" />'},
            {"handle": "kind", "desc": "kind", "svg": '<circle cx="12" cy="12" r="10" /><path d="M 12 12 L 12 2 A 10 10 0 0 1 21.5 15 Z" fill="#333" />'},
            {"handle": "part", "desc": "part", "svg": '<path d="M 12 12 L 12 2 A 10 10 0 0 1 21.5 15 Z" fill="#333" />'},
            {"handle": "dei", "desc": "this", "svg": '<line x1="12" y1="4" x2="12" y2="20" /><polyline points="6,14 12,20 18,14" />'},
            {"handle": "bik", "desc": "because", "svg": '<polygon points="12,2 21,7 21,17 12,22 3,17 3,7" />'},
        ]
    }
]

html_body = ""
for cat in categories:
    html_body += f"<h2>{cat['name']}</h2>\n"
    html_body += '<div class="grid">\n'
    for glyph in cat['glyphs']:
        svg = f'<svg viewBox="0 0 24 24" fill="none" stroke="#333" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{glyph["svg"]}</svg>'
        html_body += f"""
        <div class="glyph-card">
          {svg}
          <div class="label">{glyph['handle']}</div>
          <div class="meaning">{glyph['desc']}</div>
        </div>
        """
    html_body += '</div>\n'

html_end = """
  <hr style="margin-top: 60px; border: 1px solid #eee; margin-bottom: 40px;">
  <h2>Visual Layout Test: Romans 8:38-39 (With Reference Text)</h2>
  <p class="subtitle" style="margin-bottom: 20px; font-style: italic;">"For I am convinced that neither death nor life... will be able to separate us from the love of God that is in Christ Jesus our Lord."</p>

  <style>
    .syntax-new { display: flex; flex-direction: column; gap: 10px; font-size: 18px; font-family: monospace; padding-bottom: 40px; }
    .statement { display: flex; align-items: flex-start; gap: 12px; }
    .prime-icon { width: 28px; height: 28px; flex-shrink: 0; }
    .args-block { display: flex; flex-direction: column; gap: 6px; border-left: 2px solid #e0e0e0; padding-left: 12px; margin-top: 4px; }
    .arg-line { display: flex; align-items: flex-start; gap: 8px; }
    .role-label { font-size: 12px; color: #888; text-transform: uppercase; letter-spacing: 0.5px; width: 40px; text-align: right; margin-top: 4px; }
    .nested-block { background: #f0f4f8; border-radius: 6px; padding: 10px 15px; border: 1px solid #d9e2ec; }
    .list-items { font-size: 14px; font-family: sans-serif; color: #555; background: #fff; padding: 4px 8px; border: 1px solid #ccc; border-radius: 4px; margin-top: 2px; }
  </style>

  <div class="syntax-new">
    <div class="statement">
      <!-- noe prime -->
      <svg class="prime-icon" viewBox="0 0 24 24" fill="none" stroke="#333" stroke-width="2" stroke-linejoin="round"><polygon points="12,2 22,12 12,22 2,12" fill="#333"/></svg>
      <div class="args-block">
        <div class="arg-line">
          <span class="role-label">agt</span>
          <svg class="prime-icon" viewBox="0 0 24 24" fill="none" stroke="#333" stroke-width="2"><circle cx="12" cy="12" r="10" /><circle cx="12" cy="12" r="4" fill="#333" /></svg> <!-- me -->
        </div>
        <div class="arg-line">
          <span class="role-label">man</span>
          <svg class="prime-icon" viewBox="0 0 24 24" fill="none" stroke="#333" stroke-width="2"><rect x="4" y="4" width="16" height="16" fill="#333" /></svg> <!-- tru -->
        </div>
        <div class="arg-line">
          <span class="role-label">pat</span>
          <div class="statement nested-block">
            <!-- not prime -->
            <svg class="prime-icon" viewBox="0 0 24 24" fill="none" stroke="#333" stroke-width="2"><circle cx="12" cy="12" r="10" /><line x1="5" y1="5" x2="19" y2="19" /></svg>
            <div class="args-block" style="border-left-color: #b0bec5;">
              <div class="arg-line">
                <span class="role-label">res</span>
                <div class="statement nested-block" style="background: #fff;">
                  <!-- bik (cause) -->
                  <svg class="prime-icon" viewBox="0 0 24 24" fill="none" stroke="#333" stroke-width="2"><polygon points="12,2 21,7 21,17 12,22 3,17 3,7" /></svg>
                  <div class="args-block" style="border-left-color: #cfd8dc;">
                    <div class="arg-line">
                      <span class="role-label">agt</span>
                      <div class="list-items">DEATH ∨ LIFE ∨ ANGELS ∨ DEMONS ∨ NOW ∨ LATER ∨ HEIGHT ∨ DEPTH ∨ ∀ OTHERS</div>
                    </div>
                    <div class="arg-line">
                      <span class="role-label">res</span>
                      <div class="statement nested-block" style="background: #f9f9f9;">
                        <!-- not prime -->
                        <svg class="prime-icon" viewBox="0 0 24 24" fill="none" stroke="#333" stroke-width="2"><circle cx="12" cy="12" r="10" /><line x1="5" y1="5" x2="19" y2="19" /></svg>
                        <div class="args-block">
                          <div class="arg-line">
                            <span class="role-label">res</span>
                            <div class="statement nested-block" style="background: #eef2f5;">
                              <!-- fel (feel) -->
                              <svg class="prime-icon" viewBox="0 0 24 24" fill="none" stroke="#333" stroke-width="2" stroke-linejoin="round"><polygon points="12,2 22,12 12,22 2,12" /><path d="M 8 12 Q 10 8 12 12 T 16 12" /></svg>
                              <div class="args-block">
                                <div class="arg-line">
                                  <span class="role-label">exp</span>
                                  <span style="font-weight:bold; font-size: 16px; margin-top:2px;">GOD</span>
                                </div>
                                <div class="arg-line">
                                  <span class="role-label">pat</span>
                                  <span style="font-weight:bold; font-size: 16px; margin-top:2px;">us</span>
                                </div>
                                <div class="arg-line">
                                  <span class="role-label">man</span>
                                  <span style="display:flex; align-items:center; gap:4px;">
                                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#333" stroke-width="2"><polygon points="12,2 4,20 20,20" fill="#333" /></svg> <!-- vry -->
                                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#333" stroke-width="2"><rect x="4" y="4" width="16" height="16" /><polyline points="8,14 12,9 16,14" /></svg> <!-- gud -->
                                  </span>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  
  <hr style="border: 1px solid #eee; margin-bottom: 40px;">
  <h2>Visual Layout Test: Pure Symbolic Grammar</h2>
  <p class="subtitle" style="margin-bottom: 20px;">The exact same structure, but with all English reference text removed. This is how the Characteristica looks purely to a machine or fluent reader. The capitalized terms (like GOD or DEATH) are 'Registered Terms', and 'us' represents the entity variable.</p>

  <div class="syntax-new">
    <div class="statement">
      <!-- noe prime -->
      <svg class="prime-icon" viewBox="0 0 24 24" fill="none" stroke="#333" stroke-width="2" stroke-linejoin="round"><polygon points="12,2 22,12 12,22 2,12" fill="#333"/></svg>
      <div class="args-block">
        <div class="arg-line">
          <span class="role-label">agt</span>
          <svg class="prime-icon" viewBox="0 0 24 24" fill="none" stroke="#333" stroke-width="2"><circle cx="12" cy="12" r="10" /><circle cx="12" cy="12" r="4" fill="#333" /></svg>
        </div>
        <div class="arg-line">
          <span class="role-label">man</span>
          <svg class="prime-icon" viewBox="0 0 24 24" fill="none" stroke="#333" stroke-width="2"><rect x="4" y="4" width="16" height="16" fill="#333" /></svg>
        </div>
        <div class="arg-line">
          <span class="role-label">pat</span>
          <div class="statement nested-block">
            <!-- not prime -->
            <svg class="prime-icon" viewBox="0 0 24 24" fill="none" stroke="#333" stroke-width="2"><circle cx="12" cy="12" r="10" /><line x1="5" y1="5" x2="19" y2="19" /></svg>
            <div class="args-block" style="border-left-color: #b0bec5;">
              <div class="arg-line">
                <span class="role-label">res</span>
                <div class="statement nested-block" style="background: #fff;">
                  <!-- bik (cause) -->
                  <svg class="prime-icon" viewBox="0 0 24 24" fill="none" stroke="#333" stroke-width="2"><polygon points="12,2 21,7 21,17 12,22 3,17 3,7" /></svg>
                  <div class="args-block" style="border-left-color: #cfd8dc;">
                    <div class="arg-line">
                      <span class="role-label">agt</span>
                      <div class="list-items" style="font-family: monospace;">DEATH ∨ LIFE ∨ ANGEL ∨ DEMON ∨ ⟦tim⟧now ∨ ⟦tim⟧aft ∨ HEIGHT ∨ DEPTH ∨ ∀⟦ren⟧oth</div>
                    </div>
                    <div class="arg-line">
                      <span class="role-label">res</span>
                      <div class="statement nested-block" style="background: #f9f9f9;">
                        <!-- not prime -->
                        <svg class="prime-icon" viewBox="0 0 24 24" fill="none" stroke="#333" stroke-width="2"><circle cx="12" cy="12" r="10" /><line x1="5" y1="5" x2="19" y2="19" /></svg>
                        <div class="args-block">
                          <div class="arg-line">
                            <span class="role-label">res</span>
                            <div class="statement nested-block" style="background: #eef2f5;">
                              <!-- fel (feel) -->
                              <svg class="prime-icon" viewBox="0 0 24 24" fill="none" stroke="#333" stroke-width="2" stroke-linejoin="round"><polygon points="12,2 22,12 12,22 2,12" /><path d="M 8 12 Q 10 8 12 12 T 16 12" /></svg>
                              <div class="args-block">
                                <div class="arg-line">
                                  <span class="role-label">exp</span>
                                  <span style="font-weight:bold; font-size: 16px; margin-top:2px; font-family: monospace;">GOD</span>
                                </div>
                                <div class="arg-line">
                                  <span class="role-label">pat</span>
                                  <span style="font-weight:bold; font-size: 16px; margin-top:2px; font-family: monospace;">⟦qen⟧↺</span>
                                </div>
                                <div class="arg-line">
                                  <span class="role-label">man</span>
                                  <span style="display:flex; align-items:center; gap:4px;">
                                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#333" stroke-width="2"><polygon points="12,2 4,20 20,20" fill="#333" /></svg> <!-- vry -->
                                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#333" stroke-width="2"><rect x="4" y="4" width="16" height="16" /><polyline points="8,14 12,9 16,14" /></svg> <!-- gud -->
                                  </span>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</body>
</html>
"""

with open('/Users/calexander/writing-system-for-ai/svg_prototypes.html', 'w') as f:
    f.write(html_start + html_body + html_end)
