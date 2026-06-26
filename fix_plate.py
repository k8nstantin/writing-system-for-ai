import re

with open('/Users/calexander/writing-system-for-ai/index.html', 'r') as f:
    content = f.read()

start_marker = '<section data-c="purple">'
end_marker = '</section>'

# Find the specific section that starts with Specimen
idx = 0
while True:
    idx = content.find(start_marker, idx)
    if idx == -1: break
    end_idx = content.find(end_marker, idx) + len(end_marker)
    section_content = content[idx:end_idx]
    if 'Specimen · Plate I' in section_content:
        
        new_section = """<section data-c="purple">
  <div class="wrap reveal">
    <p class="lead-eyebrow">The Complete Dictionary</p>
    <h2>Here is the notation</h2>
    <p>About <strong>sixty-five symbols</strong> for the handful of meanings every language already shares — the atoms — plus a grammar of spatial connections and logic signs from math. Sixty-five primes, the way a hundred elements give you all of chemistry: coverage comes from a small generative basis, not an infinite dictionary. You could learn them in an afternoon.</p>
    <p>We have fully realized these 65 primes into a comprehensive visual grammar, categorized by their geometric families (Entities, Actions, Time, Space, Logic).</p>
    <div style="text-align: center; margin-top: 40px; margin-bottom: 40px;">
      <a href="svg_prototypes.html" style="display:inline-block; padding:16px 32px; background:var(--purple); color:#fff; font-weight:bold; font-family: var(--mono); letter-spacing: 0.05em; border-radius:8px; border:none; text-decoration:none; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">View the Full Visual Dictionary &rarr;</a>
    </div>
  </div>
</section>"""
        
        content = content[:idx] + new_section + content[end_idx:]
        break
    idx += len(start_marker)

with open('/Users/calexander/writing-system-for-ai/index.html', 'w') as f:
    f.write(content)

print("SUCCESS fixing plate I section")
