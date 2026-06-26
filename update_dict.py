import re

with open('/Users/calexander/writing-system-for-ai/generate_svgs.py', 'r') as f:
    svg_py = f.read()

# 1. Update Tru / Not meanings
svg_py = svg_py.replace('"desc": "true"', '"desc": "true / yes"')
svg_py = svg_py.replace('"desc": "not"', '"desc": "not / false / no"')

# 2. Add Deity to Macro Concepts
old_unv = '{"handle": "unv", "desc": "universe / all things", "svg": \'<polygon points="12,2 21,7 21,17 12,22 3,17 3,7" /><circle cx="12" cy="12" r="3" fill="#e2e8f0" />\'},'
# Replace it with EMPTY hex for universe, and add DOT hex for deity
new_unv = """            {"handle": "unv", "desc": "universe / all things", "svg": '<polygon points="12,2 21,7 21,17 12,22 3,17 3,7" />'},
            {"handle": "god", "desc": "deity / creator", "svg": '<polygon points="12,2 21,7 21,17 12,22 3,17 3,7" /><circle cx="12" cy="12" r="3" fill="#e2e8f0" />'},"""
svg_py = svg_py.replace(old_unv, new_unv)

# 3. Redesign Because (bik) so it is NOT a hexagon
# We will use an inverted IF (a Y shape pointing down: multiple causes converging to a single line)
old_bik = '{"handle": "bik", "desc": "because", "svg": \'<polygon points="12,2 21,7 21,17 12,22 3,17 3,7" />\'}'
new_bik = '{"handle": "bik", "desc": "because", "svg": \'<path d="M 12 4 V 12 L 6 20 M 12 12 L 18 20" />\'}'
svg_py = svg_py.replace(old_bik, new_bik)

with open('/Users/calexander/writing-system-for-ai/generate_svgs.py', 'w') as f:
    f.write(svg_py)


# Keyboard Updates
with open('/Users/calexander/writing-system-for-ai/generate_keyboard.py', 'r') as f:
    kb_py = f.read()

# Update Because Key
old_bik_key = '<div class="key logic"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><polygon points="12,2 21,7 21,17 12,22 3,17 3,7" /></svg></div>'
new_bik_key = '<div class="key logic"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M 12 4 V 12 L 6 20 M 12 12 L 18 20" /></svg></div>'
kb_py = kb_py.replace(old_bik_key, new_bik_key)

# Update Universe / God thumb keys
old_thumb = '<div class="key macro tall"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><polygon points="12,2 21,7 21,17 12,22 3,17 3,7" /><circle cx="12" cy="12" r="3" fill="#e2e8f0" /></svg></div>'
new_thumb = '<div class="key macro tall"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><polygon points="12,2 21,7 21,17 12,22 3,17 3,7" /></svg></div>\n      <div class="key macro tall"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><polygon points="12,2 21,7 21,17 12,22 3,17 3,7" /><circle cx="12" cy="12" r="3" fill="#e2e8f0" /></svg></div>'
kb_py = kb_py.replace(old_thumb, new_thumb)

with open('/Users/calexander/writing-system-for-ai/generate_keyboard.py', 'w') as f:
    f.write(kb_py)

print("SUCCESS")
