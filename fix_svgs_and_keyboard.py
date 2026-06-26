import re

with open('/Users/calexander/writing-system-for-ai/generate_svgs.py', 'r') as f:
    svg_py = f.read()

# 1. Update CSS in generate_svgs.py to dark mode
old_css = """  body {
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
  }"""

new_css = """  body {
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
  }"""

svg_py = svg_py.replace(old_css, new_css)
svg_py = svg_py.replace('stroke="#333"', 'stroke="#e2e8f0"')
svg_py = svg_py.replace('fill="#333"', 'fill="#e2e8f0"')

# Read the quotes from index.html
with open('/Users/calexander/writing-system-for-ai/index.html', 'r') as f:
    idx_content = f.read()

# Extract Leibniz
l_start = '<div class="glyphline-visual" style="display: flex; flex-direction: column; gap: 10px; font-size: 18px; font-family: var(--mono); padding: 14px 0px;">'
l_end = '<p class="sub" style="margin-bottom: 40px;">It says: <em>"Let us calculate, to see who is right."</em>'
l_start_idx = idx_content.find(l_start)
l_end_idx = idx_content.find(l_end, l_start_idx)
leibniz_block = idx_content[l_start_idx:l_end_idx]

# Extract Turing
t_start = '<p class="sub" style="margin-top: 40px;">Now, here is a more complex thought'
t_end = '<strong>One meaning, one form.</strong></p>'
t_start_idx = idx_content.find(t_start)
t_end_idx = idx_content.find(t_end, t_start_idx) + len(t_end)
turing_block = idx_content[t_start_idx:t_end_idx]

# Replace html_end in generate_svgs.py
html_end_old_start = 'html_end = """'
html_end_old_idx = svg_py.find(html_end_old_start)
html_end_new = 'html_end = """\n  <hr style="margin-top: 60px; border: 1px solid #2b3340; margin-bottom: 40px;">\n  <h2>Visual Layout Tests</h2>\n' + leibniz_block + '<p class="sub" style="margin-bottom: 40px; color: #8aa6d4;">It says: <em>"Let us calculate, to see who is right."</em> — the words of G. W. Leibniz in 1685.</p>\n' + turing_block + '\n</div>\n</body>\n</html>\n"""\n'

svg_py = svg_py[:html_end_old_idx] + html_end_new + "\nwith open('/Users/calexander/writing-system-for-ai/svg_prototypes.html', 'w') as f:\n    f.write(html_start + html_body + html_end)\n"

with open('/Users/calexander/writing-system-for-ai/generate_svgs.py', 'w') as f:
    f.write(svg_py)

# 2. Fix Keyboard CSS
with open('/Users/calexander/writing-system-for-ai/generate_keyboard.py', 'r') as f:
    kb_py = f.read()

old_kb_css = """  .split-keyboard {
    display: flex;
    gap: 60px; /* The physical split */
    align-items: flex-end;
  }"""

new_kb_css = """  .split-keyboard {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 60px; /* The physical split */
    align-items: flex-end;
  }"""
kb_py = kb_py.replace(old_kb_css, new_kb_css)

old_media = """  /* Responsive Design for smaller iframes/screens */
  @media (max-width: 900px) {
    .split-keyboard {
      transform: scale(0.8);
      transform-origin: center top;
      margin-bottom: -80px; /* Adjust for scaling */
    }
  }
  @media (max-width: 650px) {
    .split-keyboard {
      transform: scale(0.8);
      flex-direction: column;
      align-items: center;
      gap: 30px;
      margin-bottom: 0;
    }
    .half.left { transform: rotate(0deg); }
    .half.right { transform: rotate(0deg); }
  }"""

new_media = """  /* Responsive Design for smaller iframes/screens */
  @media (max-width: 1000px) {
    .split-keyboard {
      gap: 30px;
    }
    .half.left { transform: rotate(2deg); }
    .half.right { transform: rotate(-2deg); }
  }
  @media (max-width: 800px) {
    .split-keyboard {
      flex-direction: column;
      align-items: center;
      gap: 40px;
    }
    .half.left { transform: rotate(0deg); }
    .half.right { transform: rotate(0deg); }
  }"""
kb_py = kb_py.replace(old_media, new_media)

with open('/Users/calexander/writing-system-for-ai/generate_keyboard.py', 'w') as f:
    f.write(kb_py)

print("SUCCESS")
