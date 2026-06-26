import re

with open('/Users/calexander/writing-system-for-ai/index.html', 'r') as f:
    content = f.read()

old_not = '<svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#8aa6d4" stroke-width="2"><line x1="4" y1="4" x2="20" y2="20" stroke-width="3" /><line x1="20" y1="4" x2="4" y2="20" stroke-width="3" /></svg>'
new_not = '<svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#8aa6d4" stroke-width="2"><rect x="4" y="4" width="16" height="16" /><line x1="4" y1="4" x2="20" y2="20" /></svg>'

content = content.replace(old_not, new_not)

# Also update the white version of the not icon inside the layouts
old_not_white = '<svg class="prime-icon" viewBox="0 0 24 24" fill="none" stroke="#333" stroke-width="2"><line x1="4" y1="4" x2="20" y2="20" stroke-width="3" /><line x1="20" y1="4" x2="4" y2="20" stroke-width="3" /></svg>'
new_not_white = '<svg class="prime-icon" viewBox="0 0 24 24" fill="none" stroke="#333" stroke-width="2"><rect x="4" y="4" width="16" height="16" /><line x1="4" y1="4" x2="20" y2="20" /></svg>'
content = content.replace(old_not_white, new_not_white)

with open('/Users/calexander/writing-system-for-ai/index.html', 'w') as f:
    f.write(content)

print("SUCCESS updating NOT symbols in index")
