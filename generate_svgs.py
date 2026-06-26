import os

html_start = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Alan - Full Glyph Set</title>
<style>
  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    background-color: #0b0e13;
    color: #c8cdd6;
    display: flex;
    justify-content: center;
    padding: 40px;
  }
  .container {
    background: #161b24;
    padding: 40px;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    max-width: 900px;
    width: 100%;
    border: 1px solid #2b3340;
  }
  h1 { color: #fff; margin-bottom: 5px; }
  p.subtitle { color: #8aa6d4; margin-bottom: 40px; }
  h2 {
    color: #fff;
    border-bottom: 2px solid #2b3340;
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
    border: 1px solid #2b3340;
    border-radius: 8px;
    background: #1e2430;
    transition: transform 0.2s, box-shadow 0.2s;
  }
  .glyph-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.5);
    border-color: #4a5669;
  }
  .glyph-card svg {
    width: 48px;
    height: 48px;
    margin-bottom: 10px;
    stroke: #e2e8f0;
  }
  .label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 15px;
    font-weight: bold;
    color: #fff;
  }
  .meaning {
    font-size: 12px;
    color: #8aa6d4;
    margin-top: 4px;
    text-align: center;
  }
</style>
</head>
<body>

<div class="container">
  <h1>Alan Visual Grammar</h1>
  <p class="subtitle">The complete dictionary of ~65 Natural Semantic Metalanguage (NSM) primes, mapped to a unified visual typology. All glyphs share a consistent visual language, bound to a 24x24 grid with uniform stroke weight.</p>

  <div style="background: #1b2330; padding: 20px; border-radius: 8px; border-left: 4px solid #8aa6d4; margin-bottom: 40px;">
    <h3 style="margin-top: 0; color: #fff;">The Four Laws of Visual Grammar</h3>
    <ul style="color: #c8cdd6; line-height: 1.6; font-size: 15px; margin-bottom: 0;">
      <li><strong>1. Typology Base:</strong> Every base prime belongs to a rigid geometric category. Circles = Entities, Triangles = Events, Diamonds = Mental States, Squares = Descriptors, Hexagons = Macro/Cosmic concepts.</li>
      <li><strong>2. Geometric Opposites (Matter & Anti-Matter):</strong> Semantic opposites are created via geometric reflections. You do not need a new symbol for an antonym; flipping a shape vertically creates its polar opposite (e.g., Live ▲ / Die ▼). Flipping a shape horizontally creates its lateral opposite (e.g., Left / Right).</li>
      <li><strong>3. Layout Syntax:</strong> Text-based brackets `[ ]` are abandoned. The notation uses vertical indentation and subtle layout lines to build unambiguous, machine-parsable logical trees that are easily readable by humans.</li>
      <li><strong>4. Composite Shorthand:</strong> Complex nouns (Registered Terms) do not use English ASCII. They are represented as composite "Molecules" (e.g., a Hexagon enclosing a Star). Universally recognized cultural shorthand (like a star for Angel) is explicitly allowed to reduce the learning curve, provided it maps deterministically to a prime definition.</li>
    </ul>
  </div>
"""

categories = [
    {
        "name": "Macro-Concepts (Complex Geometry)",
        "glyphs": [
                        {"handle": "unv", "desc": "universe / all things", "svg": '<polygon points="12,2 21,7 21,17 12,22 3,17 3,7" />'},
            {"handle": "god", "desc": "deity / creator", "svg": '<polygon points="12,2 21,7 21,17 12,22 3,17 3,7" /><circle cx="12" cy="12" r="3" fill="#e2e8f0" />'},
            {"handle": "sys", "desc": "system / structure", "svg": '<polygon points="12,2 22,9 18,20 6,20 2,9" />'},
            {"handle": "law", "desc": "law / absolute rule", "svg": '<polygon points="9,2 15,2 22,9 22,15 15,22 9,22 2,15 2,9" stroke-width="3" />'},
            {"handle": "alan", "desc": "Turing (Computation)", "svg": '<g stroke="#ffd166"><polygon points="12,2 22,9 18,20 6,20 2,9" /><rect x="9" y="8" width="6" height="8" fill="#ffd166" /></g>'},
            {"handle": "carl", "desc": "Leibniz (Logic/Vision)", "svg": '<g stroke="#ffd166"><polygon points="12,2 21,7 21,17 12,22 3,17 3,7" /><polygon points="12,6 18,16 6,16" fill="#ffd166" /></g>'},
            {"handle": "k8n", "desc": "Konstantin (Creator)", "svg": '<g stroke="#ffd166"><polygon points="12,2 21,7 21,17 12,22 3,17 3,7" /><circle cx="12" cy="10" r="2" fill="#ffd166" /><circle cx="12" cy="14" r="2" fill="#ffd166" /></g>'},
            {"handle": "mdl", "desc": "AI Model / Network", "svg": '<polygon points="12,2 22,9 18,20 6,20 2,9" /><circle cx="12" cy="8" r="1.5" fill="#e2e8f0" /><circle cx="8" cy="14" r="1.5" fill="#e2e8f0" /><circle cx="16" cy="14" r="1.5" fill="#e2e8f0" /><polyline points="12,8 8,14 16,14 12,8" stroke-width="1.5" stroke="#e2e8f0" />'},
        ]
    },
    {
        "name": "Entities (Substantives) — Base: Circle",
        "glyphs": [
            {"handle": "me", "desc": "I / self", "svg": '<circle cx="12" cy="12" r="10" /><circle cx="12" cy="12" r="4" fill="#e2e8f0" />'},
            {"handle": "yu", "desc": "you / other", "svg": '<circle cx="12" cy="12" r="10" /><circle cx="12" cy="12" r="4" />'},
            {"handle": "qen", "desc": "someone", "svg": '<circle cx="12" cy="12" r="10" />'},
            {"handle": "ren", "desc": "something", "svg": '<circle cx="12" cy="12" r="10" /><line x1="6" y1="12" x2="18" y2="12" />'},
            {"handle": "ppl", "desc": "people", "svg": '<circle cx="12" cy="12" r="10" /><circle cx="12" cy="7" r="1.5" fill="#e2e8f0"/><circle cx="8" cy="14" r="1.5" fill="#e2e8f0"/><circle cx="16" cy="14" r="1.5" fill="#e2e8f0"/>'},
            {"handle": "bod", "desc": "body", "svg": '<circle cx="12" cy="12" r="10" /><line x1="12" y1="2" x2="12" y2="22" />'},
        ]
    },
    {
        "name": "Actions (Events) — Base: Triangle",
        "glyphs": [
            {"handle": "do", "desc": "do / active", "svg": '<polygon points="12,2 2,20 22,20" />'},
            {"handle": "hap", "desc": "happen", "svg": '<polygon points="2,4 22,4 12,22" />'},
            {"handle": "mov", "desc": "move", "svg": '<line x1="4" y1="12" x2="20" y2="12" /><polyline points="10,6 4,12 10,18" /><polyline points="14,6 20,12 14,18" />'},
            {"handle": "liv", "desc": "live", "svg": '<polygon points="12,2 2,20 22,20" /><circle cx="12" cy="14" r="2" fill="#e2e8f0"/>'},
            {"handle": "die", "desc": "die", "svg": '<polygon points="2,4 22,4 12,22" /><circle cx="12" cy="10" r="2" fill="#e2e8f0"/>'},
        ]
    },
    {
        "name": "Mental Predicates — Base: Diamond",
        "glyphs": [
            {"handle": "tnk", "desc": "think", "svg": '<polygon points="12,2 22,12 12,22 2,12" /><circle cx="12" cy="12" r="2" fill="#e2e8f0" />'},
            {"handle": "noe", "desc": "know", "svg": '<polygon points="12,2 22,12 12,22 2,12" fill="#e2e8f0"/>'},
            {"handle": "wnt", "desc": "want", "svg": '<polygon points="12,2 22,12 12,22 2,12" /><line x1="12" y1="12" x2="24" y2="12" /><polyline points="20,8 24,12 20,16" />'},
            {"handle": "fel", "desc": "feel", "svg": '<polygon points="12,2 22,12 12,22 2,12" /><path d="M 8 12 Q 10 8 12 12 T 16 12" />'},
            {"handle": "see", "desc": "see", "svg": '<polygon points="12,2 22,12 12,22 2,12" /><path d="M 7 12 Q 12 7 17 12 Q 12 17 7 12" />'},
            {"handle": "her", "desc": "hear", "svg": '<polygon points="12,2 22,12 12,22 2,12" /><path d="M 12 8 A 4 4 0 0 1 12 16 M 9 10 A 2 2 0 0 1 9 14" />'},
        ]
    },
    {
        "name": "Communication",
        "glyphs": [
            {"handle": "sai", "desc": "say", "svg": '<polygon points="8,4 8,20 20,12" />'},
            {"handle": "wrd", "desc": "words", "svg": '<circle cx="12" cy="12" r="10" /><line x1="8" y1="9" x2="16" y2="9" /><line x1="8" y1="12" x2="16" y2="12" /><line x1="8" y1="15" x2="12" y2="15" />'},
        ]
    },
    {
        "name": "Descriptors — Base: Square",
        "glyphs": [
            {"handle": "gud", "desc": "good", "svg": '<rect x="4" y="4" width="16" height="16" /><polyline points="8,14 12,9 16,14" />'},
            {"handle": "bad", "desc": "bad", "svg": '<rect x="4" y="4" width="16" height="16" /><polyline points="8,10 12,15 16,10" />'},
            {"handle": "big", "desc": "big", "svg": '<rect x="2" y="2" width="20" height="20" stroke-width="4" />'},
            {"handle": "sml", "desc": "small", "svg": '<rect x="10" y="10" width="4" height="4" fill="#e2e8f0" />'},
            {"handle": "tru", "desc": "true / yes", "svg": '<rect x="4" y="4" width="16" height="16" fill="#e2e8f0" />'},
            {"handle": "lik", "desc": "like / as", "svg": '<rect x="4" y="4" width="12" height="12" /><rect x="8" y="8" width="12" height="12" />'},
        ]
    },
    {
        "name": "Numbers (Mathematics)",
        "glyphs": [
            {"handle": "0", "desc": "zero", "svg": '<text x="12" y="16" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle" fill="#e2e8f0">0</text>'},
            {"handle": "1", "desc": "one", "svg": '<text x="12" y="16" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle" fill="#e2e8f0">1</text>'},
            {"handle": "2", "desc": "two", "svg": '<text x="12" y="16" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle" fill="#e2e8f0">2</text>'},
            {"handle": "3", "desc": "three", "svg": '<text x="12" y="16" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle" fill="#e2e8f0">3</text>'},
            {"handle": "4", "desc": "four", "svg": '<text x="12" y="16" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle" fill="#e2e8f0">4</text>'},
            {"handle": "5", "desc": "five", "svg": '<text x="12" y="16" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle" fill="#e2e8f0">5</text>'},
            {"handle": "6", "desc": "six", "svg": '<text x="12" y="16" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle" fill="#e2e8f0">6</text>'},
            {"handle": "7", "desc": "seven", "svg": '<text x="12" y="16" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle" fill="#e2e8f0">7</text>'},
            {"handle": "8", "desc": "eight", "svg": '<text x="12" y="16" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle" fill="#e2e8f0">8</text>'},
            {"handle": "9", "desc": "nine", "svg": '<text x="12" y="16" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle" fill="#e2e8f0">9</text>'},
            {"handle": "add", "desc": "add", "svg": '<line x1="12" y1="5" x2="12" y2="19" stroke-width="3" /><line x1="5" y1="12" x2="19" y2="12" stroke-width="3" />'},
            {"handle": "sub", "desc": "subtract", "svg": '<line x1="5" y1="12" x2="19" y2="12" stroke-width="3" />'},
            {"handle": "mul", "desc": "multiply", "svg": '<line x1="6" y1="6" x2="18" y2="18" stroke-width="3" /><line x1="18" y1="6" x2="6" y2="18" stroke-width="3" />'},
            {"handle": "div", "desc": "divide", "svg": '<line x1="5" y1="12" x2="19" y2="12" stroke-width="3" /><circle cx="12" cy="6" r="2" fill="#e2e8f0" /><circle cx="12" cy="18" r="2" fill="#e2e8f0" />'},
            {"handle": "eql", "desc": "equals", "svg": '<line x1="5" y1="9" x2="19" y2="9" stroke-width="3" /><line x1="5" y1="15" x2="19" y2="15" stroke-width="3" />'},
        ]
    },
    {
        "name": "Quantifiers",
        "glyphs": [
            {"handle": "one", "desc": "one", "svg": '<circle cx="12" cy="12" r="2" fill="#e2e8f0" />'},
            {"handle": "two", "desc": "two", "svg": '<circle cx="8" cy="12" r="2" fill="#e2e8f0" /><circle cx="16" cy="12" r="2" fill="#e2e8f0" />'},
            {"handle": "few", "desc": "few", "svg": '<circle cx="12" cy="8" r="1.5" fill="#e2e8f0" /><circle cx="7" cy="15" r="1.5" fill="#e2e8f0" /><circle cx="17" cy="15" r="1.5" fill="#e2e8f0" />'},
            {"handle": "som", "desc": "some", "svg": '<circle cx="12" cy="12" r="10" stroke-dasharray="4,4" />'},
            {"handle": "mor", "desc": "much / many", "svg": '<circle cx="6" cy="6" r="1.5" fill="#e2e8f0" /><circle cx="12" cy="6" r="1.5" fill="#e2e8f0" /><circle cx="18" cy="6" r="1.5" fill="#e2e8f0" /><circle cx="6" cy="12" r="1.5" fill="#e2e8f0" /><circle cx="12" cy="12" r="1.5" fill="#e2e8f0" /><circle cx="18" cy="12" r="1.5" fill="#e2e8f0" /><circle cx="6" cy="18" r="1.5" fill="#e2e8f0" /><circle cx="12" cy="18" r="1.5" fill="#e2e8f0" /><circle cx="18" cy="18" r="1.5" fill="#e2e8f0" />'},
            {"handle": "al", "desc": "all", "svg": '<circle cx="12" cy="12" r="10" fill="#e2e8f0" />'},
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
            {"handle": "loc", "desc": "where / place", "svg": '<line x1="2" y1="20" x2="22" y2="20" /><line x1="12" y1="20" x2="12" y2="2" /><circle cx="12" cy="12" r="3" fill="#e2e8f0" />'},
            {"handle": "here", "desc": "here", "svg": '<line x1="2" y1="20" x2="22" y2="20" /><line x1="12" y1="20" x2="12" y2="2" /><circle cx="12" cy="20" r="4" fill="#e2e8f0" />'},
            {"handle": "abv", "desc": "above", "svg": '<line x1="2" y1="18" x2="22" y2="18" /><polyline points="8,10 12,4 16,10" /><line x1="12" y1="4" x2="12" y2="14" />'},
            {"handle": "blw", "desc": "below", "svg": '<line x1="2" y1="6" x2="22" y2="6" /><polyline points="8,14 12,20 16,14" /><line x1="12" y1="20" x2="12" y2="10" />'},
            {"handle": "far", "desc": "far", "svg": '<line x1="4" y1="4" x2="4" y2="20" /><line x1="20" y1="4" x2="20" y2="20" /><path d="M 6 12 Q 12 18 18 12" stroke-dasharray="2,2" />'},
            {"handle": "near", "desc": "near", "svg": '<line x1="10" y1="4" x2="10" y2="20" /><line x1="14" y1="4" x2="14" y2="20" />'},
            {"handle": "side", "desc": "side", "svg": '<line x1="12" y1="2" x2="12" y2="22" /><rect x="4" y="8" width="5" height="8" fill="#e2e8f0" /><rect x="15" y="8" width="5" height="8" fill="#e2e8f0" />'},
            {"handle": "lft", "desc": "left", "svg": '<line x1="12" y1="2" x2="12" y2="22" /><rect x="4" y="8" width="6" height="8" fill="#e2e8f0" />'},
            {"handle": "rgt", "desc": "right", "svg": '<line x1="12" y1="2" x2="12" y2="22" /><rect x="14" y="8" width="6" height="8" fill="#e2e8f0" />'},
            {"handle": "in", "desc": "inside", "svg": '<rect x="4" y="4" width="16" height="16" /><rect x="9" y="9" width="6" height="6" fill="#e2e8f0" />'},
            {"handle": "out", "desc": "outside", "svg": '<rect x="2" y="8" width="14" height="14" /><rect x="16" y="2" width="6" height="6" fill="#e2e8f0" />'},
            {"handle": "tch", "desc": "touch", "svg": '<rect x="4" y="6" width="8" height="12" /><rect x="12" y="6" width="8" height="12" />'},
        ]
    },
    {
        "name": "Logical, Existence & Core",
        "glyphs": [
            {"handle": "not", "desc": "not / false / no", "svg": '<rect x="4" y="4" width="16" height="16" /><line x1="4" y1="4" x2="20" y2="20" />'},
            {"handle": "may", "desc": "maybe", "svg": '<path d="M 6 12 Q 9 6 12 12 T 18 12" />'},
            {"handle": "can", "desc": "can", "svg": '<path d="M 12 4 A 6 6 0 0 1 18 10 V 20 M 12 4 A 6 6 0 0 0 6 10 V 12 M 6 16 V 20" />'},
            {"handle": "if", "desc": "if", "svg": '<path d="M 12 20 V 12 L 6 4 M 12 12 L 18 4" />'},
            {"handle": "vry", "desc": "very", "svg": '<rect x="4" y="4" width="16" height="16" /><polyline points="8,13 12,8 16,13" /><polyline points="8,18 12,13 16,18" />'},
            {"handle": "is", "desc": "be", "svg": '<line x1="9" y1="4" x2="9" y2="20" stroke-width="3" /><line x1="15" y1="4" x2="15" y2="20" stroke-width="3" />'},
            {"handle": "ex", "desc": "there is", "svg": '<line x1="4" y1="20" x2="20" y2="20" /><circle cx="12" cy="16" r="4" fill="#e2e8f0" />'},
            {"handle": "hav", "desc": "have", "svg": '<polygon points="12,2 2,20 22,20" /><circle cx="12" cy="14" r="3" fill="#e2e8f0" />'},
            {"handle": "sam", "desc": "the same", "svg": '<circle cx="9" cy="12" r="6" /><circle cx="15" cy="12" r="6" />'},
            {"handle": "oth", "desc": "other", "svg": '<circle cx="8" cy="12" r="5" /><rect x="15" y="7" width="10" height="10" />'},
            {"handle": "kind", "desc": "kind", "svg": '<circle cx="12" cy="12" r="10" /><path d="M 12 12 L 12 2 A 10 10 0 0 1 21.5 15 Z" fill="#e2e8f0" />'},
            {"handle": "part", "desc": "part", "svg": '<path d="M 12 12 L 12 2 A 10 10 0 0 1 21.5 15 Z" fill="#e2e8f0" />'},
            {"handle": "dei", "desc": "this", "svg": '<line x1="12" y1="4" x2="12" y2="20" /><polyline points="6,14 12,20 18,14" />'},
            {"handle": "bik", "desc": "because", "svg": '<path d="M 12 4 V 12 L 6 20 M 12 12 L 18 20" />'},
            {"handle": "and", "desc": "and", "svg": '<polyline points="6,18 12,6 18,18" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />'},
            {"handle": "or", "desc": "or", "svg": '<polyline points="6,6 12,18 18,6" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />'},
            {"handle": "andor", "desc": "and/or", "svg": '<polyline points="6,18 12,6 18,18" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" /><polyline points="6,6 12,18 18,6" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />'},
        ]
    }
]

html_body = ""
for cat in categories:
    html_body += f"<h2>{cat['name']}</h2>\n"
    html_body += '<div class="grid">\n'
    for glyph in cat['glyphs']:
        svg = f'<svg viewBox="0 0 24 24" fill="none" stroke="#e2e8f0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{glyph["svg"]}</svg>'
        html_body += f"""
        <div class="glyph-card">
          {svg}
          <div class="label">{glyph['handle']}</div>
          <div class="meaning">{glyph['desc']}</div>
        </div>
        """
    html_body += '</div>\n'

html_end = """
  <hr style="margin-top: 60px; border: 1px solid #2b3340; margin-bottom: 40px;">
  <h2>Visual Layout Tests</h2>
<div class="glyphline-visual" style="display: flex; flex-direction: column; gap: 10px; font-size: 18px; font-family: var(--mono); padding: 14px 0px;">
      <div style="display: flex; align-items: flex-start; gap: 12px;">
        <!-- CALC prime (Pentagon + tnk) -->
        <div style="position:relative; width:28px; height:28px;" title="CALCULATE">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><polygon points="12,2 22,9 18,20 6,20 2,9" /></svg>
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" style="position:absolute; top:0; left:0; transform:scale(0.5); transform-origin: center;"><polygon points="12,2 22,12 12,22 2,12" /><circle cx="12" cy="12" r="2" fill="#fff" /></svg>
        </div>
        <div style="display: flex; flex-direction: column; gap: 6px; border-left: 2px solid #2b3340; padding-left: 12px; margin-top: 4px;">
          <div style="display: flex; align-items: center; gap: 8px;">
            
            <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="10" /></svg>
          </div>
          <div style="display: flex; align-items: flex-start; gap: 8px;">
            
            <div style="background: #161b24; border-radius: 6px; padding: 10px 15px; border: 1px solid #2b3340; display: flex; align-items: flex-start; gap: 12px;">
              <!-- noe prime -->
              <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polygon points="12,2 22,12 12,22 2,12" fill="#fff"/>
              </svg>
              <div style="display: flex; flex-direction: column; gap: 6px; border-left: 2px solid #2b3340; padding-left: 12px; margin-top: 4px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                  
                  <div style="display: flex; align-items: center; gap: 8px;">
                    <svg style="width: 20px; height: 20px;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="10" /></svg>
                    <svg style="width: 20px; height: 20px;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><circle cx="9" cy="12" r="6" /><circle cx="15" cy="12" r="6" /></svg>
                    <svg style="width: 20px; height: 20px;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><rect x="4" y="4" width="16" height="16" fill="#fff" /></svg>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <p class="ask" style="margin-bottom: 5px;"><b>Do you know what it means?</b></p>
    <p class="sub" style="margin-bottom: 40px; color: #8aa6d4;">It says: <em>"Let us calculate, to see who is right."</em> — the words of G. W. Leibniz in 1685.</p>
<p class="sub" style="margin-top: 40px;">Now, here is a more complex thought — the opening line of <span style="display:inline-block; position:relative; width:1.1em; height:1.1em; margin-right:4px; vertical-align:-0.2em;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="position:absolute; top:0; left:0; width:100%; height:100%;"><polygon points="12,2 22,9 18,20 6,20 2,9" /></svg><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="position:absolute; top:0; left:0; width:100%; height:100%; transform:scale(0.5); transform-origin: center;"><rect x="9" y="8" width="6" height="8" fill="currentColor" /></svg></span>Alan Turing's 1950 paper on AI:</p>
    <div class="glyphline-visual" style="display: flex; flex-direction: column; gap: 10px; font-size: 18px; font-family: var(--mono); padding: 14px 0px;">
      <div style="display: flex; align-items: flex-start; gap: 12px;">
        <!-- sai prime -->
        <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><polygon points="8,4 8,20 20,12" /></svg>
        <div style="display: flex; flex-direction: column; gap: 6px; border-left: 2px solid #2b3340; padding-left: 12px; margin-top: 4px;">
          <div style="display: flex; align-items: center; gap: 8px;">
            
            <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="10" /><circle cx="12" cy="12" r="4" fill="#fff" /></svg>
          </div>
          <div style="display: flex; align-items: flex-start; gap: 8px;">
            
            <div style="background: #161b24; border-radius: 6px; padding: 10px 15px; border: 1px solid #2b3340; display: flex; align-items: flex-start; gap: 12px;">
              <!-- wnt prime -->
              <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12,2 22,12 12,22 2,12" /><line x1="12" y1="12" x2="24" y2="12" /><polyline points="20,8 24,12 20,16" /></svg>
              <div style="display: flex; flex-direction: column; gap: 6px; border-left: 2px solid #2b3340; padding-left: 12px; margin-top: 4px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                  
                  <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="10" /><circle cx="12" cy="12" r="4" fill="#fff" /></svg>
                </div>
                <div style="display: flex; align-items: flex-start; gap: 8px;">
                  
                  <div style="background: #1b2330; border-radius: 6px; padding: 10px 15px; border: 1px solid #3d4757; display: flex; align-items: flex-start; gap: 12px;">
                    <!-- tnk prime -->
                    <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12,2 22,12 12,22 2,12" /><circle cx="12" cy="12" r="2" fill="#fff" /></svg>
                    <div style="display: flex; flex-direction: column; gap: 6px; border-left: 2px solid #4a5669; padding-left: 12px; margin-top: 4px;">
                      <div style="display: flex; align-items: center; gap: 8px;">
                        
                        <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="10" /><circle cx="12" cy="12" r="4" fill="#fff" /></svg>
                      </div>
                      <div style="display: flex; align-items: flex-start; gap: 8px;">
                        
                        <div style="background: #232d3d; border-radius: 6px; padding: 10px 15px; border: 1px solid #4a5669; display: flex; align-items: flex-start; gap: 12px;">
                          <!-- can prime -->
                          <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M 12 4 A 6 6 0 0 1 18 10 V 20 M 12 4 A 6 6 0 0 0 6 10 V 12 M 6 16 V 20" /></svg>
                          <div style="display: flex; flex-direction: column; gap: 6px; border-left: 2px solid #5a6980; padding-left: 12px; margin-top: 4px;">
                            <div style="display: flex; align-items: center; gap: 8px;">
                              
                              <div style="position:relative; width:28px; height:28px;" title="MACHINE"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><polygon points="12,2 22,9 18,20 6,20 2,9" /></svg><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" style="position:absolute; top:0; left:0; transform:scale(0.5); transform-origin: center;"><polygon points="12,2 2,20 22,20" /></svg></div> <!-- MACHINE (sys + do) -->
                            </div>
                            <div style="display: flex; align-items: flex-start; gap: 8px;">
                              
                              <div style="background: #2b384a; border-radius: 6px; padding: 10px 15px; border: 1px solid #5a6980; display: flex; align-items: flex-start; gap: 12px;">
                                <!-- tnk prime -->
                                <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12,2 22,12 12,22 2,12" /><circle cx="12" cy="12" r="2" fill="#fff" /></svg>
                                <div style="display: flex; flex-direction: column; gap: 6px; border-left: 2px solid #6b7a94; padding-left: 12px; margin-top: 4px;">
                                  <div style="display: flex; align-items: center; gap: 8px;">
                                    
                                    <div style="display:flex; align-items:center; gap:6px;" title="The aforementioned someone">
  <svg style="width: 24px; height: 24px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="10" /></svg>
  <svg style="width: 16px; height: 16px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#8aa6d4" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M 21 12 A 9 9 0 1 1 12 3 L 12 7 M 12 3 L 16 3" /></svg>
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
    <p class="sub">It says: <em>"I propose to consider the question, 'Can machines think?'"</em> No dialect, no drift, nothing lost between them. <strong>One meaning, one form.</strong></p>
</div>
</body>
</html>
"""

with open('/Users/calexander/writing-system-for-ai/svg_prototypes.html', 'w') as f:
    f.write(html_start + html_body + html_end)
