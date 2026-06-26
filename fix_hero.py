import os

with open('/Users/calexander/writing-system-for-ai/index.html', 'r') as f:
    content = f.read()

start_marker = '<p class="sub">Here is a simple thought — not written in English'
end_marker = '<p class="sub" style="margin-bottom: 40px;">It says: <em>"I want you to know this."</em> And it is the only way to write that thought — two people would type it identically, and so would two machines.</p>'

if start_marker in content and end_marker in content:
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker) + len(end_marker)
    
    old_section = content[start_idx:end_idx]
    
    new_section = """<p class="sub">Here is a thought — not written in English, not in any tongue anyone speaks, but in the writing system this page is about:</p>
    <div class="glyphline-visual" style="display: flex; flex-direction: column; gap: 10px; font-size: 18px; font-family: var(--mono); padding: 14px 0px;">
      <div style="display: flex; align-items: flex-start; gap: 12px;">
        <!-- CALC prime (Pentagon + tnk) -->
        <div style="position:relative; width:28px; height:28px;" title="CALCULATE">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><polygon points="12,2 22,9 18,20 6,20 2,9" /></svg>
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" style="position:absolute; top:0; left:0; transform:scale(0.5); transform-origin: center;"><polygon points="12,2 22,12 12,22 2,12" /><circle cx="12" cy="12" r="2" fill="#fff" /></svg>
        </div>
        <div style="display: flex; flex-direction: column; gap: 6px; border-left: 2px solid #2b3340; padding-left: 12px; margin-top: 4px;">
          <div style="display: flex; align-items: center; gap: 8px;">
            <span style="font-size: 12px; color: #8aa6d4; text-transform: uppercase; letter-spacing: 0.5px; width: 40px; text-align: right;">agt</span>
            <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="10" /></svg>
          </div>
          <div style="display: flex; align-items: flex-start; gap: 8px;">
            <span style="font-size: 12px; color: #8aa6d4; text-transform: uppercase; letter-spacing: 0.5px; width: 40px; text-align: right; margin-top: 4px;">res</span>
            <div style="background: #161b24; border-radius: 6px; padding: 10px 15px; border: 1px solid #2b3340; display: flex; align-items: flex-start; gap: 12px;">
              <!-- noe prime -->
              <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polygon points="12,2 22,12 12,22 2,12" fill="#fff"/>
              </svg>
              <div style="display: flex; flex-direction: column; gap: 6px; border-left: 2px solid #2b3340; padding-left: 12px; margin-top: 4px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                  <span style="font-size: 12px; color: #8aa6d4; text-transform: uppercase; letter-spacing: 0.5px; width: 40px; text-align: right;">pat</span>
                  <div style="display: flex; align-items: center; gap: 8px;">
                    <svg style="width: 20px; height: 20px;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="10" /></svg>
                    <svg style="width: 20px; height: 20px;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><line x1="4" y1="9" x2="20" y2="9" /><line x1="4" y1="15" x2="20" y2="15" /></svg>
                    <svg style="width: 20px; height: 20px;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><rect x="4" y="4" width="16" height="16" fill="#fff" /></svg>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <p class="ask" style="margin-bottom: 5px;"><b>Do you know what it means?</b></p>
    <p class="sub" style="margin-bottom: 40px;">It says: <em>"Let us calculate, to see who is right."</em> — the words of G. W. Leibniz in 1685. And it is the only way to write that thought — two people would type it identically, and so would two machines.</p>"""

    content = content.replace(old_section, new_section)
    with open('/Users/calexander/writing-system-for-ai/index.html', 'w') as f:
        f.write(content)
    print("SUCCESS replacing I want you to know this with Leibniz quote")
else:
    print("FAILED TO FIND OLD SECTION")

