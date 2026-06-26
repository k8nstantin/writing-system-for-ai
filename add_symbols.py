import os

with open('/Users/calexander/writing-system-for-ai/index.html', 'r') as f:
    content = f.read()

alan_svg = '''<span style="display:inline-block; position:relative; width:1.1em; height:1.1em; margin-right:4px; vertical-align:-0.2em;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="position:absolute; top:0; left:0; width:100%; height:100%;"><polygon points="12,2 22,9 18,20 6,20 2,9" /></svg><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="position:absolute; top:0; left:0; width:100%; height:100%; transform:scale(0.5); transform-origin: center;"><rect x="9" y="8" width="6" height="8" fill="currentColor" /></svg></span>'''

leibniz_svg = '''<span style="display:inline-block; position:relative; width:1.1em; height:1.1em; margin-right:4px; vertical-align:-0.2em;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="position:absolute; top:0; left:0; width:100%; height:100%;"><polygon points="12,2 21,7 21,17 12,22 3,17 3,7" /></svg><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="position:absolute; top:0; left:0; width:100%; height:100%; transform:scale(0.5); transform-origin: center;"><polygon points="12,6 18,16 6,16" fill="currentColor" /></svg></span>'''

replacements = [
    ("Alan Turing's 1950 paper", f"{alan_svg}Alan Turing's 1950 paper"),
    ("written in Alan, the doctor", f"written in {alan_svg}Alan, the doctor"),
    ("Alan is the staff notation", f"{alan_svg}Alan is the staff notation"),
    ("G. W. Leibniz in 1685", f"{leibniz_svg}G. W. Leibniz in 1685"),
    ("G. W. Leibniz. <em>Characteristica universalis</em>", f"{leibniz_svg}G. W. Leibniz. <em>Characteristica universalis</em>"),
    ("concept Leibniz envisioned", f"concept {leibniz_svg}Leibniz envisioned"),
    ("Gottfried Leibniz —", f"{leibniz_svg}Gottfried Leibniz —"),
    ("Leibniz’s characters", f"{leibniz_svg}Leibniz’s characters")
]

for old, new in replacements:
    content = content.replace(old, new)

with open('/Users/calexander/writing-system-for-ai/index.html', 'w') as f:
    f.write(content)

print("SUCCESS adding inline SVGs")
