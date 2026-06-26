import os

with open('/Users/calexander/writing-system-for-ai/index.html', 'r') as f:
    content = f.read()

# Remove the duplicated Leibniz block in the intro section
leibniz_intro_start = '<p class="reveal-line">And it is not only for new sentences. <strong>Anything ever written has one exact form.</strong> Here are three famous lines — first in the new language, then in the words you know:</p>'

if leibniz_intro_start in content:
    idx = content.find(leibniz_intro_start)
    # The end of the Leibniz figure
    end_fig = '<figcaption>— G. W. Leibniz, 1685</figcaption></figure>'
    end_idx = content.find(end_fig, idx) + len(end_fig)
    
    old_block = content[idx:end_idx]
    
    new_block = '<p class="reveal-line">And it is not only for new sentences. <strong>Anything ever written has one exact form.</strong> Here are two famous lines — first in the new language, then in the words you know:</p>'
    
    content = content.replace(old_block, new_block)
    
    with open('/Users/calexander/writing-system-for-ai/index.html', 'w') as f:
        f.write(content)
    print("SUCCESS removing duplicate")
else:
    print("FAILED")
