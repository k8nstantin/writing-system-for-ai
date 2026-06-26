import re

# 1. Update generate_svgs.py
with open('/Users/calexander/writing-system-for-ai/generate_svgs.py', 'r') as f:
    svgs_content = f.read()

# Change 'is' from horizontal to vertical lines
old_is_svg = '\'{"handle": "is", "desc": "be", "svg": \'<line x1="4" y1="9" x2="20" y2="9" /><line x1="4" y1="15" x2="20" y2="15" />\'}\''
svgs_content = svgs_content.replace('<line x1="4" y1="9" x2="20" y2="9" /><line x1="4" y1="15" x2="20" y2="15" />', '<line x1="9" y1="4" x2="9" y2="20" stroke-width="3" /><line x1="15" y1="4" x2="15" y2="20" stroke-width="3" />')

# Add and/or to Logical category
logic_end = '{"handle": "bik", "desc": "because", "svg": \'<polygon points="12,2 21,7 21,17 12,22 3,17 3,7" />\'},'
logic_new = logic_end + """
            {"handle": "and", "desc": "and", "svg": '<polyline points="6,18 12,6 18,18" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />'},
            {"handle": "or", "desc": "or", "svg": '<polyline points="6,6 12,18 18,6" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />'},"""

svgs_content = svgs_content.replace(logic_end, logic_new)

with open('/Users/calexander/writing-system-for-ai/generate_svgs.py', 'w') as f:
    f.write(svgs_content)


# 2. Update generate_keyboard.py
with open('/Users/calexander/writing-system-for-ai/generate_keyboard.py', 'r') as f:
    kb_content = f.read()

# Replace 'is' key
kb_content = kb_content.replace('<line x1="4" y1="9" x2="20" y2="9" /><line x1="4" y1="15" x2="20" y2="15" />', '<line x1="9" y1="4" x2="9" y2="20" stroke-width="3" /><line x1="15" y1="4" x2="15" y2="20" stroke-width="3" />')

# Add and / or keys to logic row (Row 1)
# Find the end of Row 1 left half
old_row1 = """      <div class="key logic"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="9" y1="4" x2="9" y2="20" stroke-width="3" /><line x1="15" y1="4" x2="15" y2="20" stroke-width="3" /></svg></div>
    </div>"""

new_row1 = """      <div class="key logic"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="9" y1="4" x2="9" y2="20" stroke-width="3" /><line x1="15" y1="4" x2="15" y2="20" stroke-width="3" /></svg></div>
      <div class="key logic"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><polyline points="6,18 12,6 18,18" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" /></svg></div>
      <div class="key logic"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><polyline points="6,6 12,18 18,6" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" /></svg></div>
    </div>"""

kb_content = kb_content.replace(old_row1, new_row1)

with open('/Users/calexander/writing-system-for-ai/generate_keyboard.py', 'w') as f:
    f.write(kb_content)


# 3. Update index.html
with open('/Users/calexander/writing-system-for-ai/index.html', 'r') as f:
    idx_content = f.read()

idx_content = idx_content.replace('<line x1="4" y1="9" x2="20" y2="9" /><line x1="4" y1="15" x2="20" y2="15" />', '<line x1="9" y1="4" x2="9" y2="20" stroke-width="3" /><line x1="15" y1="4" x2="15" y2="20" stroke-width="3" />')

with open('/Users/calexander/writing-system-for-ai/index.html', 'w') as f:
    f.write(idx_content)

print("SUCCESS")
