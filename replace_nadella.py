import os

with open('/Users/calexander/writing-system-for-ai/index.html', 'r') as f:
    content = f.read()

start_marker = '    <div class="glyphline-visual" style="display: flex; flex-direction: column; gap: 10px; font-size: 18px; font-family: var(--mono); padding: 14px 0px;">\n      <div style="display: flex; align-items: flex-start; gap: 12px;">\n        <!-- ex (there is) -->'
end_marker = '— Satya Nadella, Microsoft, 2025</figcaption></figure>'

if start_marker in content and end_marker in content:
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker) + len(end_marker)
    
    old_section = content[start_idx:end_idx]
    
    new_section = """    <div class="glyphline-visual" style="display: flex; flex-direction: column; gap: 10px; font-size: 18px; font-family: var(--mono); padding: 14px 0px;">
      <!-- can -->
      <div style="display: flex; align-items: flex-start; gap: 12px;">
        <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M 12 4 A 6 6 0 0 1 18 10 V 20 M 12 4 A 6 6 0 0 0 6 10 V 12 M 6 16 V 20" /></svg>
        <div style="display: flex; flex-direction: column; gap: 6px; border-left: 2px solid #2b3340; padding-left: 12px; margin-top: 4px;">
          <div style="display: flex; align-items: center; gap: 8px;">
            <span style="font-size: 12px; color: #8aa6d4; text-transform: uppercase; letter-spacing: 0.5px; width: 40px; text-align: right;">agt</span>
            <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="10" /></svg>
          </div>
          <div style="display: flex; align-items: flex-start; gap: 8px;">
            <span style="font-size: 12px; color: #8aa6d4; text-transform: uppercase; letter-spacing: 0.5px; width: 40px; text-align: right; margin-top: 4px;">pat</span>
            <div style="background: #161b24; border-radius: 6px; padding: 10px 15px; border: 1px solid #2b3340; display: flex; align-items: flex-start; gap: 12px;">
              <!-- do -->
              <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><polygon points="12,2 2,20 22,20" /></svg>
              <div style="display: flex; flex-direction: column; gap: 6px; border-left: 2px solid #2b3340; padding-left: 12px; margin-top: 4px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                  <span style="font-size: 12px; color: #8aa6d4; text-transform: uppercase; letter-spacing: 0.5px; width: 40px; text-align: right;">agt</span>
                  <span style="font-weight:bold; font-size: 16px; margin-top:2px; font-family: monospace;">⟦qen⟧↺</span>
                </div>
                <div style="display: flex; align-items: flex-start; gap: 8px;">
                  <span style="font-size: 12px; color: #8aa6d4; text-transform: uppercase; letter-spacing: 0.5px; width: 40px; text-align: right; margin-top: 4px;">pat</span>
                  <div style="background: #1b2330; border-radius: 6px; padding: 10px 15px; border: 1px solid #3d4757; display: flex; align-items: flex-start; gap: 12px;">
                    <!-- wnt -->
                    <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12,2 22,12 12,22 2,12" /><line x1="12" y1="12" x2="24" y2="12" /><polyline points="20,8 24,12 20,16" /></svg>
                    <div style="display: flex; flex-direction: column; gap: 6px; border-left: 2px solid #4a5669; padding-left: 12px; margin-top: 4px;">
                      <div style="display: flex; align-items: center; gap: 8px;">
                        <span style="font-size: 12px; color: #8aa6d4; text-transform: uppercase; letter-spacing: 0.5px; width: 40px; text-align: right;">agt</span>
                        <span style="font-weight:bold; font-size: 16px; margin-top:2px; font-family: monospace;">⟦qen⟧↺</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div style="display: flex; align-items: center; justify-content: center; width: 28px; font-size: 14px; font-weight: bold; color: #8aa6d4;">AND NOT</div>
      <div style="display: flex; align-items: flex-start; gap: 12px;">
        <!-- can -->
        <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M 12 4 A 6 6 0 0 1 18 10 V 20 M 12 4 A 6 6 0 0 0 6 10 V 12 M 6 16 V 20" /></svg>
        <div style="display: flex; flex-direction: column; gap: 6px; border-left: 2px solid #2b3340; padding-left: 12px; margin-top: 4px;">
          <div style="display: flex; align-items: center; gap: 8px;">
            <span style="font-size: 12px; color: #8aa6d4; text-transform: uppercase; letter-spacing: 0.5px; width: 40px; text-align: right;">agt</span>
            <span style="font-weight:bold; font-size: 16px; margin-top:2px; font-family: monospace;">⟦qen⟧↺</span>
          </div>
          <div style="display: flex; align-items: flex-start; gap: 8px;">
            <span style="font-size: 12px; color: #8aa6d4; text-transform: uppercase; letter-spacing: 0.5px; width: 40px; text-align: right; margin-top: 4px;">pat</span>
            <div style="background: #161b24; border-radius: 6px; padding: 10px 15px; border: 1px solid #2b3340; display: flex; align-items: flex-start; gap: 12px;">
              <!-- wnt -->
              <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12,2 22,12 12,22 2,12" /><line x1="12" y1="12" x2="24" y2="12" /><polyline points="20,8 24,12 20,16" /></svg>
              <div style="display: flex; flex-direction: column; gap: 6px; border-left: 2px solid #2b3340; padding-left: 12px; margin-top: 4px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                  <span style="font-size: 12px; color: #8aa6d4; text-transform: uppercase; letter-spacing: 0.5px; width: 40px; text-align: right;">agt</span>
                  <span style="font-weight:bold; font-size: 16px; margin-top:2px; font-family: monospace;">⟦qen⟧↺</span>
                </div>
                <div style="display: flex; align-items: flex-start; gap: 8px;">
                  <span style="font-size: 12px; color: #8aa6d4; text-transform: uppercase; letter-spacing: 0.5px; width: 40px; text-align: right; margin-top: 4px;">pat</span>
                  <div style="background: #1b2330; border-radius: 6px; padding: 10px 15px; border: 1px solid #3d4757; display: flex; align-items: flex-start; gap: 12px;">
                    <!-- wnt -->
                    <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12,2 22,12 12,22 2,12" /><line x1="12" y1="12" x2="24" y2="12" /><polyline points="20,8 24,12 20,16" /></svg>
                    <div style="display: flex; flex-direction: column; gap: 6px; border-left: 2px solid #4a5669; padding-left: 12px; margin-top: 4px;">
                      <div style="display: flex; align-items: center; gap: 8px;">
                        <span style="font-size: 12px; color: #8aa6d4; text-transform: uppercase; letter-spacing: 0.5px; width: 40px; text-align: right;">agt</span>
                        <span style="font-weight:bold; font-size: 16px; margin-top:2px; font-family: monospace;">⟦qen⟧↺</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <figure class="epi now"><blockquote>Man can do what he wills but he cannot will what he wills.</blockquote><figcaption>— Arthur Schopenhauer, 1839</figcaption></figure>"""
    
    content = content.replace(old_section, new_section)
    
    # Also we need to remove Nadella's name from "The stakes" section.
    old_nadella_ref = "Satya Nadella has begun describing a workday where each person oversees not one model but <strong>millions of agents</strong> — a “new inbox” of agents delegating, summarizing, and acting on one another’s words.<sup><a href=\"#s17\">17</a></sup>"
    new_nadella_ref = "We are entering a workday where each person oversees not one model but <strong>millions of agents</strong> delegating, summarizing, and acting on one another’s words."
    content = content.replace(old_nadella_ref, new_nadella_ref)
    
    with open('/Users/calexander/writing-system-for-ai/index.html', 'w') as f:
        f.write(content)
    print("SUCCESS")
else:
    print("FAILED")
