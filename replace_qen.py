import re

with open('/Users/calexander/writing-system-for-ai/index.html', 'r') as f:
    content = f.read()

# The string to replace
old_string = '<span style="font-weight:bold; font-size: 16px; margin-top:2px; font-family: monospace;">⟦qen⟧↺</span>'

# The new geometric SVG representing "the aforementioned someone"
new_string = """<div style="display:flex; align-items:center; gap:6px;" title="The aforementioned someone">
  <svg style="width: 24px; height: 24px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="10" /></svg>
  <svg style="width: 16px; height: 16px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#8aa6d4" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M 21 12 A 9 9 0 1 1 12 3 L 12 7 M 12 3 L 16 3" /></svg>
</div>"""

content = content.replace(old_string, new_string)

with open('/Users/calexander/writing-system-for-ai/index.html', 'w') as f:
    f.write(content)

print("SUCCESS")
