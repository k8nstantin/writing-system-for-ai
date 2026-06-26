import re

with open('/Users/calexander/writing-system-for-ai/index.html', 'r') as f:
    content = f.read()

# Pattern to match the role labels
pattern = r'<div style="width: 40px; display: flex; align-items: center; justify-content: flex-end;.*?" title=".*?">.*?</div>'

matches = re.findall(pattern, content)
print(f"Found {len(matches)} role labels to remove.")

content = re.sub(pattern, '', content)

with open('/Users/calexander/writing-system-for-ai/index.html', 'w') as f:
    f.write(content)
print("SUCCESS")
