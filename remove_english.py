import re

# Update index.html to remove scrollbar
with open('/Users/calexander/writing-system-for-ai/index.html', 'r') as f:
    idx_content = f.read()
idx_content = idx_content.replace('<iframe src="keyboard_prototype.html"', '<iframe src="keyboard_prototype.html" scrolling="no"')
with open('/Users/calexander/writing-system-for-ai/index.html', 'w') as f:
    f.write(idx_content)

# Update generate_keyboard.py to remove english handles
with open('/Users/calexander/writing-system-for-ai/generate_keyboard.py', 'r') as f:
    content = f.read()

# Remove all <span class="handle">...</span>
content = re.sub(r'<span class="handle">.*?</span>', '', content)

# Replace special keys
content = content.replace('<div class="key wide" style="color:#5d626c; font-size:12px; font-weight:bold;">BACK</div>', '<div class="key wide" style="color:#5d626c; font-size:18px; font-weight:bold;" data-action="BACK">⌫</div>')
content = content.replace('<div class="key wide" style="color:#5d626c; font-size:12px; font-weight:bold;">TAB</div>', '<div class="key wide" style="color:#5d626c; font-size:18px; font-weight:bold;" data-action="TAB">⇥</div>')
content = content.replace('<div class="key wide" style="color:#5d626c; font-size:12px; font-weight:bold;">CAPS</div>', '<div class="key wide" style="color:#5d626c; font-size:18px; font-weight:bold;" data-action="CAPS">⇪</div>')
content = content.replace('<div class="key wide" style="color:#5d626c; font-size:12px; font-weight:bold;">ENTER</div>', '<div class="key wide" style="color:#5d626c; font-size:18px; font-weight:bold;" data-action="ENTER">↵</div>')
content = content.replace('<div class="key wide" style="color:#5d626c; font-size:12px; font-weight:bold;">SHIFT</div>', '<div class="key wide" style="color:#5d626c; font-size:18px; font-weight:bold;" data-action="SHIFT">⇧</div>')

# Update JavaScript logic
js_old = """      const text = key.textContent.trim();
      if (text === 'BACK') {
        if (output.children.length > 1) { // 1 is the cursor
          output.removeChild(output.children[output.children.length - 2]);
        }
        return;
      }
      if (text === 'SPACE' || text === 'SHIFT' || text === 'TAB' || text === 'CAPS' || text === 'ENTER') {
        return; // Ignore modifiers for now
      }"""

js_new = """      const action = key.getAttribute('data-action');
      if (action === 'BACK') {
        if (output.children.length > 1) { // 1 is the cursor
          output.removeChild(output.children[output.children.length - 2]);
        }
        return;
      }
      if (action) {
        return; // Ignore other modifiers for now
      }"""

content = content.replace(js_old, js_new)

with open('/Users/calexander/writing-system-for-ai/generate_keyboard.py', 'w') as f:
    f.write(content)
print("SUCCESS")
