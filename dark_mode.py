import re

with open('/Users/calexander/writing-system-for-ai/index.html', 'r') as f:
    content = f.read()

# Update :root CSS
old_css_root = """:root{
  --blue:#2c4a78; --teal:#0792a8; --red:#d23f1a; --amber:#bd7a06; --green:#118a5a;
  --gold:#b8901f; --purple:#7a59c0;
  --ink:#181a1f; --muted:#5d626c; --line:#e7e4dc; --paper:#faf8f3; --paperwarm:#fff7df;
  --dark:#0e1116; --dark2:#161b24; --darkline:#2b3340; --darktext:#c8cdd6;
  --glyph:#edefea; --handle:#93aedc; --accent:#e89a89;
  --serif:'Spectral',Georgia,'Times New Roman',serif;
  --sans:'Inter',system-ui,-apple-system,Segoe UI,Roboto,sans-serif;
  --mono:'JetBrains Mono',ui-monospace,SFMono-Regular,Menlo,monospace;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);
  font-size:19px;line-height:1.72;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
.progress{position:fixed;top:0;left:0;height:3px;width:0;z-index:50;
  background:linear-gradient(90deg,var(--blue),var(--teal),var(--green),var(--gold),var(--purple))}
.wrap{max-width:760px;margin:0 auto;padding:0 26px}
a{color:var(--blue);text-decoration:none;border-bottom:1px solid #c9d3e6}
a:hover{border-color:var(--blue)}
strong{font-weight:700}
em{font-style:italic}
code{font-family:var(--mono);font-size:.85em;background:#eee9dd;padding:.08em .35em;border-radius:4px}"""

new_css_root = """:root{
  --blue:#8aa6d4; --teal:#48b5c4; --red:#f67280; --amber:#ffd166; --green:#7fcf9f;
  --gold:#ffd166; --purple:#a388ed;
  --ink:#c8cdd6; --muted:#5d626c; --line:#2b3340; --paper:#0b0e13; --paperwarm:#11151c;
  --dark:#0e1116; --dark2:#161b24; --darkline:#2b3340; --darktext:#c8cdd6;
  --glyph:#edefea; --handle:#93aedc; --accent:#e89a89;
  --serif:'Spectral',Georgia,'Times New Roman',serif;
  --sans:'Inter',system-ui,-apple-system,Segoe UI,Roboto,sans-serif;
  --mono:'JetBrains Mono',ui-monospace,SFMono-Regular,Menlo,monospace;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);
  font-size:19px;line-height:1.72;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
.progress{position:fixed;top:0;left:0;height:3px;width:0;z-index:50;
  background:linear-gradient(90deg,var(--blue),var(--teal),var(--green),var(--gold),var(--purple))}
.wrap{max-width:760px;margin:0 auto;padding:0 26px}
a{color:var(--blue);text-decoration:none;border-bottom:1px solid var(--line)}
a:hover{border-color:var(--blue); color:#fff;}
strong{font-weight:700; color:#fff;}
em{font-style:italic}
code{font-family:var(--mono);font-size:.85em;background:var(--dark2);color:#fff;padding:.08em .35em;border-radius:4px; border:1px solid var(--line)}"""

if old_css_root in content:
    content = content.replace(old_css_root, new_css_root)
else:
    print("CSS Root not found!")

# Also fix the h2 headers to be light instead of dark
old_h2 = """h2{font-family:var(--serif);font-weight:800;font-size:clamp(27px,4vw,38px);line-height:1.12;
  letter-spacing:-.01em;margin:0 0 22px;color:var(--ink)}"""
new_h2 = """h2{font-family:var(--serif);font-weight:800;font-size:clamp(27px,4vw,38px);line-height:1.12;
  letter-spacing:-.01em;margin:0 0 22px;color:#fff}"""
content = content.replace(old_h2, new_h2)

# Fix section.alt borders
old_alt = """section.alt{background:var(--paperwarm);border-top:1px solid #efe7c9;border-bottom:1px solid #efe7c9}"""
new_alt = """section.alt{background:var(--paperwarm);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}"""
content = content.replace(old_alt, new_alt)

# Fix drift box
old_drift = """.drift{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin:34px 0 20px;
  background:#fff;border:1px solid #c9d3e6;border-radius:12px;overflow:hidden;box-shadow:0 12px 30px rgba(44,74,120,.08)}"""
new_drift = """.drift{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin:34px 0 20px;
  background:var(--dark2);border:1px solid var(--line);border-radius:12px;overflow:hidden;box-shadow:0 12px 30px rgba(0,0,0,.3)}"""
content = content.replace(old_drift, new_drift)

old_col_eng = """.col.eng{background:#fafafc}"""
new_col_eng = """.col.eng{background:var(--dark)}"""
content = content.replace(old_col_eng, new_col_eng)

old_verdict_eng = """.col.eng .verdict{background:#f0f2f5;color:#6f7787;border-top:1px solid #e2e6ed}"""
new_verdict_eng = """.col.eng .verdict{background:var(--dark);color:#8aa6d4;border-top:1px solid var(--line)}"""
content = content.replace(old_verdict_eng, new_verdict_eng)

old_verdict_can = """.col.can .verdict{background:#f5f8ff;color:var(--blue);border-top:1px solid #c9d3e6;font-weight:600}"""
new_verdict_can = """.col.can .verdict{background:var(--dark2);color:var(--blue);border-top:1px solid var(--line);font-weight:600}"""
content = content.replace(old_verdict_can, new_verdict_can)

old_plate = """.plate{margin:40px 0;border:1px solid var(--line);border-radius:12px;background:#fff;padding:24px 28px;
  box-shadow:0 10px 24px rgba(0,0,0,.03)}"""
new_plate = """.plate{margin:40px 0;border:1px solid var(--line);border-radius:12px;background:var(--dark2);padding:24px 28px;
  box-shadow:0 10px 24px rgba(0,0,0,.3)}"""
content = content.replace(old_plate, new_plate)

old_gl = """table.gl td{border-bottom:1px solid #f0f0f0;padding:12px 0;vertical-align:top}"""
new_gl = """table.gl td{border-bottom:1px solid var(--line);padding:12px 0;vertical-align:top}"""
content = content.replace(old_gl, new_gl)

old_gl_head = """table.gl th{text-align:left;font-family:var(--mono);font-size:11px;letter-spacing:.1em;
  text-transform:uppercase;color:#8b93a1;border-bottom:2px solid #e7e4dc;padding-bottom:8px}"""
new_gl_head = """table.gl th{text-align:left;font-family:var(--mono);font-size:11px;letter-spacing:.1em;
  text-transform:uppercase;color:#8b93a1;border-bottom:2px solid var(--line);padding-bottom:8px}"""
content = content.replace(old_gl_head, new_gl_head)

old_gl_sym = """.gl-sym{font-family:var(--mono);font-size:19px;color:var(--blue);font-weight:700;width:80px}"""
new_gl_sym = """.gl-sym{font-family:var(--mono);font-size:19px;color:var(--blue);font-weight:700;width:80px}"""
content = content.replace(old_gl_sym, new_gl_sym)


with open('/Users/calexander/writing-system-for-ai/index.html', 'w') as f:
    f.write(content)

print("SUCCESS")
