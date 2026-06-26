import os

with open('/Users/calexander/writing-system-for-ai/index.html', 'r') as f:
    content = f.read()

old_hero_section = """    <p class="sub">Here is a sentence — not in English, not in any tongue anyone speaks, but in the writing system this page is about:</p>
    <div class="glyphline-visual" style="display: flex; flex-direction: column; gap: 10px; font-size: 18px; font-family: var(--mono); padding: 14px 0px;">
      <div style="display: flex; align-items: flex-start; gap: 12px;">
        <!-- wnt prime -->
        <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <polygon points="12,2 22,12 12,22 2,12" />
          <line x1="12" y1="12" x2="24" y2="12" />
          <polyline points="20,8 24,12 20,16" />
        </svg>
        <div style="display: flex; flex-direction: column; gap: 6px; border-left: 2px solid #2b3340; padding-left: 12px; margin-top: 4px;">
          <div style="display: flex; align-items: center; gap: 8px;">
            <span style="font-size: 12px; color: #8aa6d4; text-transform: uppercase; letter-spacing: 0.5px; width: 40px; text-align: right;">agt</span>
            <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="10" /><circle cx="12" cy="12" r="4" fill="#fff" /></svg>
          </div>
          <div style="display: flex; align-items: center; gap: 8px;">
            <span style="font-size: 12px; color: #8aa6d4; text-transform: uppercase; letter-spacing: 0.5px; width: 40px; text-align: right;">rec</span>
            <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="10" /><circle cx="12" cy="12" r="4" /></svg>
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
                  <span style="font-size: 12px; color: #8aa6d4; text-transform: uppercase; letter-spacing: 0.5px; width: 40px; text-align: right;">agt</span>
                  <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="10" /><circle cx="12" cy="12" r="4" /></svg>
                </div>
                <div style="display: flex; align-items: center; gap: 8px;">
                  <span style="font-size: 12px; color: #8aa6d4; text-transform: uppercase; letter-spacing: 0.5px; width: 40px; text-align: right;">pat</span>
                  <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><line x1="12" y1="4" x2="12" y2="20" /><polyline points="6,14 12,20 18,14" /></svg>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <p class="ask"><b>Do you know what it means?</b></p>
    <p class="sub">It says: <em>I want you to know this.</em> And it is the only way to write that thought — two people would type it identically, and so would two machines. No dialect, no drift, nothing lost between them. <strong>One meaning, one form.</strong></p>"""

new_hero_section = """    <p class="sub">Here is a thought — not written in English, not in any tongue anyone speaks, but in the writing system this page is about:</p>
    <div class="glyphline-visual" style="display: flex; flex-direction: column; gap: 10px; font-size: 18px; font-family: var(--mono); padding: 14px 0px;">
      <div style="display: flex; align-items: flex-start; gap: 12px;">
        <!-- sai prime -->
        <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><polygon points="8,4 8,20 20,12" /></svg>
        <div style="display: flex; flex-direction: column; gap: 6px; border-left: 2px solid #2b3340; padding-left: 12px; margin-top: 4px;">
          <div style="display: flex; align-items: center; gap: 8px;">
            <span style="font-size: 12px; color: #8aa6d4; text-transform: uppercase; letter-spacing: 0.5px; width: 40px; text-align: right;">agt</span>
            <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="10" /><circle cx="12" cy="12" r="4" fill="#fff" /></svg>
          </div>
          <div style="display: flex; align-items: flex-start; gap: 8px;">
            <span style="font-size: 12px; color: #8aa6d4; text-transform: uppercase; letter-spacing: 0.5px; width: 40px; text-align: right; margin-top: 4px;">pat</span>
            <div style="background: #161b24; border-radius: 6px; padding: 10px 15px; border: 1px solid #2b3340; display: flex; align-items: flex-start; gap: 12px;">
              <!-- wnt prime -->
              <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12,2 22,12 12,22 2,12" /><line x1="12" y1="12" x2="24" y2="12" /><polyline points="20,8 24,12 20,16" /></svg>
              <div style="display: flex; flex-direction: column; gap: 6px; border-left: 2px solid #2b3340; padding-left: 12px; margin-top: 4px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                  <span style="font-size: 12px; color: #8aa6d4; text-transform: uppercase; letter-spacing: 0.5px; width: 40px; text-align: right;">agt</span>
                  <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="10" /><circle cx="12" cy="12" r="4" fill="#fff" /></svg>
                </div>
                <div style="display: flex; align-items: flex-start; gap: 8px;">
                  <span style="font-size: 12px; color: #8aa6d4; text-transform: uppercase; letter-spacing: 0.5px; width: 40px; text-align: right; margin-top: 4px;">pat</span>
                  <div style="background: #1b2330; border-radius: 6px; padding: 10px 15px; border: 1px solid #3d4757; display: flex; align-items: flex-start; gap: 12px;">
                    <!-- tnk prime -->
                    <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12,2 22,12 12,22 2,12" /><circle cx="12" cy="12" r="2" fill="#fff" /></svg>
                    <div style="display: flex; flex-direction: column; gap: 6px; border-left: 2px solid #4a5669; padding-left: 12px; margin-top: 4px;">
                      <div style="display: flex; align-items: center; gap: 8px;">
                        <span style="font-size: 12px; color: #8aa6d4; text-transform: uppercase; letter-spacing: 0.5px; width: 40px; text-align: right;">agt</span>
                        <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="10" /><circle cx="12" cy="12" r="4" fill="#fff" /></svg>
                      </div>
                      <div style="display: flex; align-items: flex-start; gap: 8px;">
                        <span style="font-size: 12px; color: #8aa6d4; text-transform: uppercase; letter-spacing: 0.5px; width: 40px; text-align: right; margin-top: 4px;">pat</span>
                        <div style="background: #232d3d; border-radius: 6px; padding: 10px 15px; border: 1px solid #4a5669; display: flex; align-items: flex-start; gap: 12px;">
                          <!-- can prime -->
                          <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M 12 4 A 6 6 0 0 1 18 10 V 20 M 12 4 A 6 6 0 0 0 6 10 V 12 M 6 16 V 20" /></svg>
                          <div style="display: flex; flex-direction: column; gap: 6px; border-left: 2px solid #5a6980; padding-left: 12px; margin-top: 4px;">
                            <div style="display: flex; align-items: center; gap: 8px;">
                              <span style="font-size: 12px; color: #8aa6d4; text-transform: uppercase; letter-spacing: 0.5px; width: 40px; text-align: right;">agt</span>
                              <div style="position:relative; width:28px; height:28px;" title="MACHINE"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><polygon points="12,2 22,9 18,20 6,20 2,9" /></svg><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" style="position:absolute; top:0; left:0; transform:scale(0.5); transform-origin: center;"><polygon points="12,2 2,20 22,20" /></svg></div> <!-- MACHINE (sys + do) -->
                            </div>
                            <div style="display: flex; align-items: flex-start; gap: 8px;">
                              <span style="font-size: 12px; color: #8aa6d4; text-transform: uppercase; letter-spacing: 0.5px; width: 40px; text-align: right; margin-top: 4px;">pat</span>
                              <div style="background: #2b384a; border-radius: 6px; padding: 10px 15px; border: 1px solid #5a6980; display: flex; align-items: flex-start; gap: 12px;">
                                <!-- tnk prime -->
                                <svg style="width: 28px; height: 28px; flex-shrink: 0;" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12,2 22,12 12,22 2,12" /><circle cx="12" cy="12" r="2" fill="#fff" /></svg>
                                <div style="display: flex; flex-direction: column; gap: 6px; border-left: 2px solid #6b7a94; padding-left: 12px; margin-top: 4px;">
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
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <p class="ask"><b>Do you know what it means?</b></p>
    <p class="sub">It says: <em>"I propose to consider the question, 'Can machines think?'"</em> — the opening line of Alan Turing's 1950 paper. And it is the only way to write that thought — two people would type it identically, and so would two machines. No dialect, no drift, nothing lost between them. <strong>One meaning, one form.</strong></p>"""

if old_hero_section in content:
    content = content.replace(old_hero_section, new_hero_section)
    with open('/Users/calexander/writing-system-for-ai/index.html', 'w') as f:
        f.write(content)
    print("SUCCESS")
else:
    print("FAILED TO FIND OLD SECTION")
