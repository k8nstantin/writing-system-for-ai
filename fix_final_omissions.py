import re

# 1. Update generate_svgs.py
with open('/Users/calexander/writing-system-for-ai/generate_svgs.py', 'r') as f:
    svgs = f.read()

svgs = svgs.replace('<title>Characteristica Reborn - Full Glyph Set</title>', '<title>Alan - Full Glyph Set</title>')
svgs = svgs.replace('<h1>Characteristica Visual Grammar</h1>', '<h1>Alan Visual Grammar</h1>')

svgs = svgs.replace('<div style="background: #eef2f5; padding: 20px; border-radius: 6px; border-left: 4px solid #4a90e2; margin-bottom: 40px;">', '<div style="background: #1b2330; padding: 20px; border-radius: 8px; border-left: 4px solid #8aa6d4; margin-bottom: 40px;">')
svgs = svgs.replace('<h3 style="margin-top: 0; color: #333;">', '<h3 style="margin-top: 0; color: #fff;">')
svgs = svgs.replace('<ul style="color: #444; line-height: 1.6; font-size: 15px; margin-bottom: 0;">', '<ul style="color: #c8cdd6; line-height: 1.6; font-size: 15px; margin-bottom: 0;">')

# Remove Semantic Roles category
role_cat = """    {
        "name": "Semantic Roles (Structural Connections)",
        "glyphs": [
            {"handle": "agt", "desc": "agent / doer", "svg": '<line x1="2" y1="12" x2="22" y2="12" /><circle cx="4" cy="12" r="2" fill="#e2e8f0" /><polyline points="18,8 22,12 18,16" />'},
            {"handle": "pat", "desc": "patient / receiver", "svg": '<line x1="2" y1="12" x2="22" y2="12" /><polyline points="18,8 22,12 18,16" /><line x1="22" y1="6" x2="22" y2="18" />'},
            {"handle": "res", "desc": "result / output", "svg": '<line x1="2" y1="12" x2="22" y2="12" /><polyline points="18,8 22,12 18,16" stroke-width="4" />'},
            {"handle": "man", "desc": "manner / how", "svg": '<path d="M 2 12 Q 7 4 12 12 T 22 12" /><polyline points="18,8 22,12 18,16" />'},
        ]
    }"""
svgs = svgs.replace(",\n" + role_cat, "")

with open('/Users/calexander/writing-system-for-ai/generate_svgs.py', 'w') as f:
    f.write(svgs)

# 2. Update generate_keyboard.py
with open('/Users/calexander/writing-system-for-ai/generate_keyboard.py', 'r') as f:
    kb = f.read()

kb = kb.replace('  .key.role   { border-top: 2px solid #f0f4f8; } /* White/Grey */\n', '')
kb = kb.replace('  <div class="legend-item"><div class="dot" style="background: #f0f4f8;"></div> Semantic Roles</div>\n', '')

old_thumb = """    <!-- Left Thumb Cluster -->
    <div class="thumb-cluster left">
      <div class="key role"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="2" y1="12" x2="22" y2="12" /><circle cx="4" cy="12" r="2" fill="#e2e8f0" /><polyline points="18,8 22,12 18,16" /></svg></div>
      <div class="key role"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="2" y1="12" x2="22" y2="12" /><polyline points="18,8 22,12 18,16" /><line x1="22" y1="6" x2="22" y2="18" /></svg></div>
      <div class="key role"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="2" y1="12" x2="22" y2="12" /><polyline points="18,8 22,12 18,16" stroke-width="4" /></svg></div>
      <div class="key role"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M 2 12 Q 7 4 12 12 T 22 12" /><polyline points="18,8 22,12 18,16" /></svg></div>
      <div class="key wide" style="color:#5d626c; font-size:24px; font-weight:bold;" data-action="FLIP">⇿</div>
      <div class="key logic tall"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><circle cx="12" cy="12" r="10" fill="#e2e8f0" /></svg></div>
    </div>"""

new_thumb = """    <!-- Left Thumb Cluster -->
    <div class="thumb-cluster left">
      <div class="key wide" style="color:#5d626c; font-size:24px; font-weight:bold;" data-action="FLIP">⇿</div>
      <div class="key logic tall"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><circle cx="12" cy="12" r="10" fill="#e2e8f0" /></svg></div>
    </div>"""

kb = kb.replace(old_thumb, new_thumb)

with open('/Users/calexander/writing-system-for-ai/generate_keyboard.py', 'w') as f:
    f.write(kb)

print("SUCCESS")
