import re

with open('/Users/calexander/writing-system-for-ai/index.html', 'r') as f:
    content = f.read()

# Replace the specific stroke-width="3" instances in the Schopenhauer quote connectors
content = content.replace('<svg style="width: 16px; height: 16px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#8aa6d4" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M 21 12 A 9 9 0 1 1 12 3 L 12 7 M 12 3 L 16 3" /></svg>', '<svg style="width: 16px; height: 16px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#8aa6d4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M 21 12 A 9 9 0 1 1 12 3 L 12 7 M 12 3 L 16 3" /></svg>')

with open('/Users/calexander/writing-system-for-ai/index.html', 'w') as f:
    f.write(content)

print("SUCCESS")
