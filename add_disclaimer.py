import re

with open('/Users/calexander/writing-system-for-ai/index.html', 'r') as f:
    content = f.read()

# Add a prominent conceptual disclaimer box right under the hero section, before the quotes
target = '<div class="quotes">'

disclaimer = """<div style="background: rgba(255, 209, 102, 0.1); border-left: 4px solid var(--gold); padding: 20px; border-radius: 8px; max-width: 680px; margin: 0 auto 40px auto;">
      <h3 style="color: var(--gold); margin-top: 0; font-family: var(--mono); font-size: 14px; letter-spacing: 0.1em; text-transform: uppercase;">Note on this Project</h3>
      <p style="margin-bottom: 0; font-size: 16px; line-height: 1.5; color: #d6dae2;">Alan is currently a <strong>conceptual prototype</strong> and an architectural sketch. It is not a finished, production-ready product. It is presented here as an open provocation to the AI and linguistics communities: a proof-of-concept that a universal, layout-driven visual grammar is mathematically possible. We invite collaboration to refine the dictionary, build the parsers, and test the limits of this foundation.</p>
    </div>
    """

if target in content:
    content = content.replace(target, disclaimer + target)
    with open('/Users/calexander/writing-system-for-ai/index.html', 'w') as f:
        f.write(content)
    print("SUCCESS")
else:
    print("FAILED")
