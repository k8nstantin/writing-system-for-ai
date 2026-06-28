import os

html_start = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Alan Universal Writing System - Interactive Tutorial</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
  body {
    background-color: #0b0e13;
    color: #c8cdd6;
    font-family: 'JetBrains Mono', monospace;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    min-height: 100vh;
    margin: 0;
    padding: 20px;
    box-sizing: border-box;
    overflow-y: auto;
  }
  
  .header {
    text-align: center;
    margin-bottom: 20px;
    width: 100%;
    max-width: 850px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  
  .header h1 {
    font-size: 22px;
    color: #fff;
    margin: 0;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .header a {
    color: #48b5c4;
    text-decoration: none;
    border-bottom: 1px dashed #48b5c4;
    font-size: 14px;
    transition: all 0.2s ease;
  }
  .header a:hover {
    color: #7fcf9f;
    border-color: #7fcf9f;
  }

  /* Tutorial Panel */
  .tutorial-panel {
    background: #161b24;
    border: 1px solid #2b3340;
    border-radius: 12px;
    width: 100%;
    max-width: 850px;
    padding: 20px;
    margin-bottom: 20px;
    box-sizing: border-box;
    position: relative;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
  }

  .lesson-title {
    color: #ffd166;
    font-size: 18px;
    font-weight: bold;
    margin-top: 0;
    margin-bottom: 15px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .lesson-progress {
    font-size: 12px;
    color: #8aa6d4;
    background: #0f131a;
    padding: 4px 10px;
    border-radius: 20px;
    border: 1px solid #2b3340;
  }

  .lesson-tabs {
    display: flex;
    gap: 10px;
    margin-bottom: 15px;
    border-bottom: 1px solid #2b3340;
    padding-bottom: 10px;
    flex-wrap: wrap;
  }
  .tab-btn {
    background: #0f131a;
    color: #8aa6d4;
    border: 1px solid #2b3340;
    padding: 6px 14px;
    border-radius: 6px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    cursor: pointer;
    transition: all 0.2s ease;
  }
  .tab-btn:hover {
    color: #fff;
    border-color: #48b5c4;
  }
  .tab-btn.active {
    background: #48b5c4;
    color: #0b0e13;
    border-color: #48b5c4;
    font-weight: bold;
  }

  .target-phrase-box {
    background: rgba(255, 209, 102, 0.08);
    border: 1px solid rgba(255, 209, 102, 0.2);
    border-radius: 6px;
    padding: 10px 15px;
    margin-bottom: 15px;
    font-size: 15px;
    color: #fff;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .instructions {
    font-size: 14px;
    line-height: 1.6;
    color: #d6dae2;
    margin-bottom: 15px;
  }

  .hint-box {
    background: rgba(72, 181, 196, 0.1);
    border-left: 4px solid #48b5c4;
    padding: 10px 15px;
    font-size: 13px;
    color: #a7ddec;
    border-radius: 0 8px 8px 0;
    margin-bottom: 15px;
  }

  /* Non-blocking success banner */
  .success-banner {
    display: none;
    padding: 12px 15px;
    background: rgba(127, 207, 159, 0.12);
    border-left: 4px solid #7fcf9f;
    border-radius: 0 8px 8px 0;
    color: #a6f2be;
    font-size: 14px;
    margin-bottom: 15px;
    align-items: center;
    justify-content: space-between;
    animation: slide-down 0.3s ease;
  }
  @keyframes slide-down {
    from { opacity: 0; transform: translateY(-5px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .btn-next {
    background: #7fcf9f;
    color: #0b0e13;
    border: none;
    padding: 8px 16px;
    font-family: 'JetBrains Mono', monospace;
    font-weight: bold;
    font-size: 13px;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s ease;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .btn-next:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 12px rgba(127,207,159,0.3);
  }

  /* Output Display */
  .output-display {
    display: flex;
    flex-direction: column;
    align-items: stretch;
    justify-content: flex-start;
    min-height: 140px;
    max-height: 200px;
    overflow-y: auto;
    width: 100%;
    max-width: 850px;
    padding: 15px;
    box-shadow: inset 0 4px 15px rgba(0,0,0,0.6);
    background: #090c11;
    border: 1px solid #2b3340;
    border-radius: 12px;
    margin-bottom: 20px;
    box-sizing: border-box;
  }

  .line {
    display: flex;
    align-items: center;
    gap: 12px;
    min-height: 40px;
    margin-top: 4px;
    border-left: 2px solid transparent;
    transition: all 0.2s ease;
    box-sizing: border-box;
  }
  .line[data-indent="1"] { border-left-color: #2b3340; }
  .line[data-indent="2"] { border-left-color: #3d4757; }
  .line[data-indent="3"] { border-left-color: #4a5669; }
  .line[data-indent="4"] { border-left-color: #5a6980; }

  .line .spacer {
    width: 16px;
    height: 32px;
    flex-shrink: 0;
    position: relative;
  }
  .line .spacer::after {
    content: '·';
    color: #ffffff;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    font-size: 20px;
    font-weight: bold;
  }

  .line svg {
    width: 28px;
    height: 28px;
    stroke: #e2e8f0;
  }

  .cursor {
    width: 2px;
    height: 28px;
    background: #48b5c4;
    animation: blink-anim 1s step-end infinite;
  }
  
  @keyframes blink-anim { 50% { opacity: 0; } }

  /* Keyboard Style */
  .split-keyboard {
    display: flex;
    justify-content: center;
    gap: 30px;
    align-items: flex-end;
  }

  .half {
    background: #161b24;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #2b3340;
    box-shadow: 0 15px 30px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.05);
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .half.left { transform: rotate(2deg); }
  .half.right { transform: rotate(-2deg); }

  .row {
    display: flex;
    gap: 6px;
    justify-content: center;
  }

  .key {
    width: 48px;
    height: 48px;
    background: linear-gradient(180deg, #2b3340 0%, #1e2430 100%);
    border-radius: 8px;
    border: 1px solid #0b0e13;
    box-shadow: 0 4px 0 #0b0e13, inset 0 1px 1px rgba(255,255,255,0.1);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    position: relative;
    cursor: pointer;
    transition: all 0.1s ease;
  }
  
  .key:active {
    transform: translateY(4px);
    box-shadow: 0 0px 0 #0b0e13, inset 0 1px 2px rgba(0,0,0,0.5);
  }

  .key svg {
    width: 20px;
    height: 20px;
    stroke: #e2e8f0;
  }
  
  .key .handle {
    position: absolute;
    bottom: 3px;
    font-size: 8px;
    color: #5d626c;
    letter-spacing: 0.05em;
  }
  
  /* Category Colors */
  .key.entity { border-top: 2px solid #7fcf9f; }
  .key.action { border-top: 2px solid #ff8a6b; }
  .key.mental { border-top: 2px solid #a388ed; }
  .key.space  { border-top: 2px solid #8aa6d4; }
  .key.desc   { border-top: 2px solid #f67280; }
  .key.logic  { border-top: 2px solid #ffd166; }
  .key.time   { border-top: 2px solid #48b5c4; }
  .key.num    { border-top: 2px solid #e2e8f0; }

  .key.wide { width: 75px; }
  .key.tall { height: 104px; }
  
  .thumb-cluster {
    display: flex;
    gap: 8px;
    margin-top: 8px;
  }
  .thumb-cluster.left { justify-content: flex-end; padding-right: 10px; }
  .thumb-cluster.right { justify-content: flex-start; padding-left: 10px; }

  /* Highlighting Pulsing key */
  .key.highlight {
    animation: pulse-border 1.5s infinite alternate;
    box-shadow: 0 0 15px rgba(72,181,196,0.6);
    border-color: #48b5c4 !important;
  }
  @keyframes pulse-border {
    0% { transform: scale(1); }
    100% { transform: scale(1.05); background: #1e2d3d; }
  }

  /* Flippable Modifier Styles */
  .flipped .key[data-flip="Y"] svg {
    transform: scaleY(-1);
    stroke: #ff8a6b !important;
  }
  .flipped .key[data-flip="X"] svg {
    transform: scaleX(-1);
    stroke: #ff8a6b !important;
  }
  .key.modifier.active {
    background: #2b384a;
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.8);
    border-top-color: #a388ed !important;
  }

  svg.flipped-Y {
    transform: scaleY(-1);
    stroke: #ff8a6b !important;
  }
  svg.flipped-X {
    transform: scaleX(-1);
    stroke: #ff8a6b !important;
  }

  /* Responsive Design */
  @media (max-width: 1000px) {
    .split-keyboard {
      gap: 20px;
      transform: scale(0.85);
    }
  }
</style>
</head>
<body>

<div class="header">
  <h1>
    <span style="display:inline-block; position:relative; width:1.1em; height:1.1em; vertical-align:-0.2em;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="position:absolute; top:0; left:0; width:100%; height:100%;"><polygon points="12,2 22,9 18,20 6,20 2,9" /></svg><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="position:absolute; top:0; left:0; width:100%; height:100%; transform:scale(0.5); transform-origin: center;"><rect x="9" y="8" width="6" height="8" fill="currentColor" /></svg></span>
    Alan: Interactive Tutorial
  </h1>
  <a href="keyboard_prototype.html">Back to Keyboard Sandbox &rarr;</a>
</div>

<div class="tutorial-panel">
  <div class="lesson-title">
    <span id="lessonTitle">Lesson 1: The Self &amp; Thought</span>
    <span class="lesson-progress" id="lessonProgress">Rung 1/6</span>
  </div>

  <div class="lesson-tabs" id="lessonTabs"></div>

  <!-- Symmetrical Warm Gold Target Box -->
  <div class="target-phrase-box">
    <span style="font-size: 11px; text-transform: uppercase; color: #ffd166; background: rgba(255,209,102,0.15); padding: 2px 6px; border-radius: 4px; font-weight: bold;">English Target:</span>
    <strong id="lessonTargetPhrase" style="font-size: 16px; color: #fff;">"I think"</strong>
  </div>

  <div class="instructions" id="lessonInstructions">
    In Alan, diamonds represent mental states, and circles represent entities. Let's write the core thought: <strong>"I think"</strong>.
  </div>

  <div class="success-banner" id="successBanner">
    <span>✓ Perfect representation! Feel free to play around, or click "Next Lesson" when you are ready.</span>
    <button class="btn-next" id="btnNext">Next Lesson &rarr;</button>
  </div>

  <div class="checklist" id="checklist" style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 15px; font-size: 13px; color: #8aa6d4;"></div>

  <div class="hint-box" id="lessonHint">
    Hint: Press the purple Diamond key (think), then SPACE on your left thumb, then the green Circle-with-Dot key (me).
  </div>
</div>

<div class="output-display" id="output">
  <div class="line" data-indent="0">
    <div class="cursor" id="cursor"></div>
  </div>
</div>

<div class="split-keyboard">

  <!-- LEFT HALF: Logic, Mental, Entities, Time -->
  <div class="half left">
    <!-- Row 0: Numbers -->
    <div class="row" style="padding-left: 20px;">
      <div class="key num" data-handle="1"><svg viewBox="0 0 24 24"><text x="12" y="16" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle" fill="#e2e8f0">1</text></svg></div>
      <div class="key num" data-handle="2"><svg viewBox="0 0 24 24"><text x="12" y="16" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle" fill="#e2e8f0">2</text></svg></div>
      <div class="key num" data-handle="3"><svg viewBox="0 0 24 24"><text x="12" y="16" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle" fill="#e2e8f0">3</text></svg></div>
      <div class="key num" data-handle="4"><svg viewBox="0 0 24 24"><text x="12" y="16" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle" fill="#e2e8f0">4</text></svg></div>
      <div class="key num" data-handle="5"><svg viewBox="0 0 24 24"><text x="12" y="16" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle" fill="#e2e8f0">5</text></svg></div>
      <div class="key num" data-handle="add"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19" stroke-width="3" /><line x1="5" y1="12" x2="19" y2="12" stroke-width="3" /></svg></div>
      <div class="key num" data-handle="sub"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12" stroke-width="3" /></svg></div>
    </div>
    <!-- Row 1: Logic -->
    <div class="row" style="padding-left: 0px;">
      <div class="key logic" data-handle="not"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><rect x="4" y="4" width="16" height="16" /><line x1="4" y1="4" x2="20" y2="20" /></svg></div>
      <div class="key logic" data-handle="if"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M 12 20 V 12 L 6 4 M 12 12 L 18 4" /></svg></div>
      <div class="key logic" data-handle="can"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M 12 4 A 6 6 0 0 1 18 10 V 20 M 12 4 A 6 6 0 0 0 6 10 V 12 M 6 16 V 20" /></svg></div>
      <div class="key logic" data-handle="may"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M 6 12 Q 9 6 12 12 T 18 12" /></svg></div>
      <div class="key logic" data-handle="bik"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M 12 4 V 12 L 6 20 M 12 12 L 18 20" /></svg></div>
      <div class="key logic" data-handle="is"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="9" y1="4" x2="9" y2="20" stroke-width="3" /><line x1="15" y1="4" x2="15" y2="20" stroke-width="3" /></svg></div>
      <div class="key logic" data-handle="and"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><polyline points="6,18 12,6 18,18" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" /></svg></div>
      <div class="key logic" data-handle="or"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><polyline points="6,6 12,18 18,6" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" /></svg></div>
      <div class="key logic" data-handle="andor"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><polyline points="6,18 12,6 18,18" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" /><polyline points="6,6 12,18 18,6" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" /></svg></div>
    </div>
    <!-- Row 2: Mental -->
    <div class="row" style="padding-left: 20px;">
      <div class="key mental" data-handle="think"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><polygon points="12,2 22,12 12,22 2,12" /><circle cx="12" cy="12" r="2" fill="#e2e8f0" /></svg><span class="handle">think</span></div>
      <div class="key mental" data-handle="know"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><polygon points="12,2 22,12 12,22 2,12" fill="#e2e8f0"/></svg><span class="handle">know</span></div>
      <div class="key mental" data-handle="want"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><polygon points="12,2 22,12 12,22 2,12" /><line x1="12" y1="12" x2="24" y2="12" /><polyline points="20,8 24,12 20,16" /></svg><span class="handle">want</span></div>
      <div class="key mental" data-handle="feel"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><polygon points="12,2 22,12 12,22 2,12" /><path d="M 8 12 Q 10 8 12 12 T 16 12" /></svg><span class="handle">feel</span></div>
      <div class="key mental" data-handle="see"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><polygon points="12,2 22,12 12,22 2,12" /><path d="M 7 12 Q 12 7 17 12 Q 12 17 7 12" /></svg><span class="handle">see</span></div>
      <div class="key mental" data-handle="hear"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><polygon points="12,2 22,12 12,22 2,12" /><path d="M 12 8 A 4 4 0 0 1 12 16 M 9 10 A 2 2 0 0 1 9 14" /></svg><span class="handle">hear</span></div>
    </div>
    <!-- Row 3: Entities -->
    <div class="row" style="padding-left: 10px;">
      <div class="key entity" data-handle="me"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><circle cx="12" cy="12" r="10" /><circle cx="12" cy="12" r="4" fill="#e2e8f0" /></svg><span class="handle">me</span></div>
      <div class="key entity" data-handle="you"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><circle cx="12" cy="12" r="10" /><circle cx="12" cy="12" r="4" /></svg><span class="handle">you</span></div>
      <div class="key entity" data-handle="someone"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><circle cx="12" cy="12" r="10" /></svg><span class="handle">someone</span></div>
      <div class="key entity" data-handle="something"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><circle cx="12" cy="12" r="10" /><line x1="6" y1="12" x2="18" y2="12" /></svg><span class="handle">thing</span></div>
      <div class="key entity" data-handle="people"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><circle cx="12" cy="12" r="10" /><circle cx="12" cy="7" r="1.5" fill="#e2e8f0"/><circle cx="8" cy="14" r="1.5" fill="#e2e8f0"/><circle cx="16" cy="14" r="1.5" fill="#e2e8f0"/></svg><span class="handle">people</span></div>
      <div class="key entity" data-handle="body"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><circle cx="12" cy="12" r="10" /><line x1="12" y1="2" x2="12" y2="22" /></svg><span class="handle">body</span></div>
    </div>
    <!-- Row 4: Time -->
    <div class="row" style="padding-left: 30px;">
      <div class="key time" data-handle="time"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="2" y1="12" x2="22" y2="12" /><line x1="12" y1="8" x2="12" y2="16" /></svg></div>
      <div class="key time" data-handle="now"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="2" y1="12" x2="22" y2="12" /><line x1="12" y1="6" x2="12" y2="18" stroke-width="4" /></svg></div>
      <div class="key time" data-handle="before" data-flip="X"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="2" y1="12" x2="22" y2="12" /><line x1="12" y1="8" x2="12" y2="16" /><polyline points="10,12 6,12" /><polyline points="8,10 6,12 8,14" /></svg></div>
      <div class="key time" data-handle="long"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="4" y1="12" x2="20" y2="12" /><polyline points="6,9 2,12 6,15" /><polyline points="18,9 22,12 18,15" /></svg></div>
      <div class="key time" data-handle="moment"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="12" y1="6" x2="12" y2="18" stroke-width="4" /></svg></div>
    </div>
    <!-- Left Thumb Cluster -->
    <div class="thumb-cluster left">
      <div class="key wide modifier" data-action="FLIP" style="color: #ffd166; font-size: 16px; font-weight: bold;" title="Hold/Toggle to flip symbols to opposites">⇿ ANTI</div>
      <div class="key tall space" data-action="SPACE" title="Space (Horizontal Word Gap)"><svg viewBox="0 0 24 24" fill="none" stroke="#8aa6d4" stroke-width="2"><path d="M 4 8 V 16 H 20 V 8" stroke-width="3" /></svg></div>
      <div class="key tall action" data-action="INDENT" title="Step Right (Indent)"><svg viewBox="0 0 24 24" fill="none" stroke="#7fcf9f" stroke-width="2"><line x1="4" y1="12" x2="20" y2="12" stroke-width="3" /><polyline points="14,6 20,12 14,18" stroke-width="3" /></svg></div>
    </div>
  </div>


  <!-- RIGHT HALF: Quantifiers, Actions, Descriptors, Space -->
  <div class="half right">
    <!-- Row 0: Numbers -->
    <div class="row" style="padding-right: 20px;">
      <div class="key num" data-handle="6"><svg viewBox="0 0 24 24"><text x="12" y="16" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle" fill="#e2e8f0">6</text></svg></div>
      <div class="key num" data-handle="7"><svg viewBox="0 0 24 24"><text x="12" y="16" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle" fill="#e2e8f0">7</text></svg></div>
      <div class="key num" data-handle="8"><svg viewBox="0 0 24 24"><text x="12" y="16" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle" fill="#e2e8f0">8</text></svg></div>
      <div class="key num" data-handle="9"><svg viewBox="0 0 24 24"><text x="12" y="16" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle" fill="#e2e8f0">9</text></svg></div>
      <div class="key num" data-handle="0"><svg viewBox="0 0 24 24"><text x="12" y="16" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle" fill="#e2e8f0">0</text></svg></div>
      <div class="key num" data-handle="mul"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="6" y1="6" x2="18" y2="18" stroke-width="3" /><line x1="18" y1="6" x2="6" y2="18" stroke-width="3" /></svg></div>
      <div class="key num" data-handle="div"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12" stroke-width="3" /><circle cx="12" cy="6" r="2" fill="#e2e8f0" /><circle cx="12" cy="18" r="2" fill="#e2e8f0" /></svg></div>
      <div class="key num" data-handle="eql"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="5" y1="9" x2="19" y2="9" stroke-width="3" /><line x1="5" y1="15" x2="19" y2="15" stroke-width="3" /></svg></div>
    </div>
    <!-- Row 1: Quantifiers -->
    <div class="row" style="padding-right: 0px;">
      <div class="key logic" data-handle="one"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><circle cx="12" cy="12" r="2" fill="#e2e8f0" /></svg></div>
      <div class="key logic" data-handle="two"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><circle cx="8" cy="12" r="2" fill="#e2e8f0" /><circle cx="16" cy="12" r="2" fill="#e2e8f0" /></svg></div>
      <div class="key logic" data-handle="few"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><circle cx="12" cy="8" r="1.5" fill="#e2e8f0" /><circle cx="7" cy="15" r="1.5" fill="#e2e8f0" /><circle cx="17" cy="15" r="1.5" fill="#e2e8f0" /></svg></div>
      <div class="key logic" data-handle="som"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><circle cx="12" cy="12" r="10" stroke-dasharray="4,4" /></svg></div>
      <div class="key logic" data-handle="mor"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><circle cx="6" cy="6" r="1.5" fill="#e2e8f0" /><circle cx="12" cy="6" r="1.5" fill="#e2e8f0" /><circle cx="18" cy="6" r="1.5" fill="#e2e8f0" /><circle cx="6" cy="12" r="1.5" fill="#e2e8f0" /><circle cx="12" cy="12" r="1.5" fill="#e2e8f0" /><circle cx="18" cy="12" r="1.5" fill="#e2e8f0" /><circle cx="6" cy="18" r="1.5" fill="#e2e8f0" /><circle cx="12" cy="18" r="1.5" fill="#e2e8f0" /><circle cx="18" cy="18" r="1.5" fill="#e2e8f0" /></svg></div>
      <div class="key logic" data-handle="al"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><circle cx="12" cy="12" r="10" fill="#e2e8f0" /></svg></div>
    </div>
    <!-- Row 2: Actions & Comm -->
    <div class="row" style="padding-right: 20px;">
      <div class="key action" data-handle="do"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><polygon points="12,2 2,20 22,20" /></svg><span class="handle">do</span></div>
      <div class="key action" data-handle="mov"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="4" y1="12" x2="20" y2="12" /><polyline points="10,6 4,12 10,18" /><polyline points="14,6 20,12 14,18" /></svg><span class="handle">move</span></div>
      <div class="key action" data-handle="liv" data-flip="Y"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><polygon points="12,2 2,20 22,20" /><circle cx="12" cy="14" r="2" fill="#e2e8f0"/></svg><span class="handle">live</span></div>
      <div class="key action" data-handle="sai"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><polygon points="8,4 8,20 20,12" /></svg><span class="handle">say</span></div>
      <div class="key action" data-handle="wrd"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><circle cx="12" cy="12" r="10" /><line x1="8" y1="9" x2="16" y2="9" /><line x1="8" y1="12" x2="16" y2="12" /><line x1="8" y1="15" x2="12" y2="15" /></svg><span class="handle">words</span></div>
    </div>
    <!-- Row 3: Descriptors -->
    <div class="row" style="padding-right: 10px;">
      <div class="key desc" data-handle="gud" data-flip="Y"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><rect x="4" y="4" width="16" height="16" /><polyline points="8,14 12,9 16,14" /></svg><span class="handle">good</span></div>
      <div class="key desc" data-handle="big" data-flip="Y"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><rect x="4" y="4" width="16" height="16" /><polygon points="8,16 16,16 18,7 6,7" fill="#e2e8f0" /></svg><span class="handle">big</span></div>
      <div class="key desc" data-handle="les" data-flip="X"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><polyline points="15,5 9,12 15,19" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" /></svg><span class="handle">less</span></div>
      <div class="key desc" data-handle="tru"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><rect x="4" y="4" width="16" height="16" fill="#e2e8f0" /></svg><span class="handle">true</span></div>
      <div class="key desc" data-handle="lik"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><rect x="4" y="4" width="16" height="16" /><polyline points="8,13 12,8 16,13" /><polyline points="8,18 12,13 16,18" /></svg><span class="handle">like</span></div>
      <div class="key desc" data-handle="part"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><rect x="4" y="4" width="12" height="12" /><rect x="8" y="8" width="12" height="12" /></svg><span class="handle">part</span></div>
    </div>
    <!-- Row 4: Space -->
    <div class="row" style="padding-right: 30px;">
      <div class="key space" data-handle="place"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="2" y1="20" x2="22" y2="20" /><line x1="12" y1="20" x2="12" y2="2" /><circle cx="12" cy="12" r="3" fill="#e2e8f0" /></svg></div>
      <div class="key space" data-handle="above" data-flip="Y"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="2" y1="18" x2="22" y2="18" /><polyline points="8,10 12,4 16,10" /><line x1="12" y1="4" x2="12" y2="14" /></svg></div>
      <div class="key space" data-handle="left" data-flip="X"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="12" y1="2" x2="12" y2="22" /><rect x="4" y="8" width="6" height="8" fill="#e2e8f0" /></svg></div>
      <div class="key space" data-handle="in"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><rect x="4" y="4" width="16" height="16" /><rect x="9" y="9" width="6" height="6" fill="#e2e8f0" /></svg></div>
      <div class="key space" data-handle="out"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><rect x="2" y="8" width="14" height="14" /><rect x="16" y="2" width="6" height="6" fill="#e2e8f0" /></svg></div>
    </div>
    <!-- Right Thumb Cluster -->
    <div class="thumb-cluster right">
      <div class="key tall action" data-action="OUTDENT" title="Step Left (Outdent)"><svg viewBox="0 0 24 24" fill="none" stroke="#7fcf9f" stroke-width="2"><line x1="20" y1="12" x2="4" y2="12" stroke-width="3" /><polyline points="10,6 4,12 10,18" stroke-width="3" /></svg></div>
      <div class="key tall action" data-action="DOWN" title="Step Down (Newline / Sibling)"><svg viewBox="0 0 24 24" fill="none" stroke="#ff8a6b" stroke-width="2"><path d="M 20 6 V 14 H 6 M 12 8 L 6 14 L 12 20" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" /></svg></div>
      <div class="key wide action" data-action="BACK" style="color: #f67280; font-size: 16px; font-weight: bold;" title="Backspace">⌫ BACK</div>
    </div>
  </div>

</div>

<script>
  const output = document.getElementById('output');
  let activeLine = output.querySelector('.line');
  let cursor = document.getElementById('cursor');
  let currentIndent = 0;
  let isFlipped = false;

  const successBanner = document.getElementById('successBanner');
  const btnNext = document.getElementById('btnNext');

  const lessonTitleEl = document.getElementById('lessonTitle');
  const lessonProgressEl = document.getElementById('lessonProgress');
  const lessonInstructionsEl = document.getElementById('lessonInstructions');
  const lessonHintEl = document.getElementById('lessonHint');
  const lessonTargetPhraseEl = document.getElementById('lessonTargetPhrase');

  const lessons = [
    {
      title: "Lesson 1: The Self & Thought",
      progress: "Rung 1/6",
      targetPhrase: "I think",
      instructions: "In Alan, diamonds represent mental states, and circles represent entities. Let's write the core semantic thought: <strong>'I think'</strong>.",
      hint: "Press the purple Diamond key (think), then SPACE on your left thumb, then the green Circle-with-Dot key (me).",
      targetKeys: ["think", "SPACE", "me"],
      validate: (line) => {
        const elements = Array.from(line.children).filter(el => el.id !== 'cursor');
        if (elements.length !== 3) return false;
        return elements[0].getAttribute('data-handle') === 'think' &&
               elements[1].className === 'spacer' &&
               elements[2].getAttribute('data-handle') === 'me';
      }
    },
    {
      title: "Lesson 2: Matter & Anti-Matter (Flipping Opposites)",
      progress: "Rung 2/6",
      targetPhrase: "I live, I die",
      instructions: "We don't need separate keys for semantic opposites. We vertically or horizontally reflect existing ones! Let's write: <strong>'live'</strong>, then step-down, then use the <strong>ANTI</strong> modifier to type <strong>'die'</strong>.",
      hint: "Press 'live'. Press STEP-DOWN on your right thumb. Press ANTI on your left thumb. Now press the inverted 'die' key (which was 'live')!",
      targetKeys: ["liv", "DOWN", "FLIP", "liv"],
      validate: (out) => {
        const lines = Array.from(out.querySelectorAll('.line'));
        if (lines.length < 2) return false;
        
        const l0_el = Array.from(lines[0].children).filter(el => el.id !== 'cursor');
        const hasLiv = l0_el.length === 1 && l0_el[0].getAttribute('data-handle') === 'liv';
        
        const l1_el = Array.from(lines[1].children).filter(el => el.id !== 'cursor');
        const hasDie = l1_el.length === 1 && l1_el[0].getAttribute('data-flipped') === 'true' && l1_el[0].getAttribute('data-handle') === 'liv';
        
        return hasLiv && hasDie;
      }
    },
    {
      title: "Lesson 3: The Cascading Step-Ladder",
      progress: "Rung 3/6",
      targetPhrase: "I want you",
      instructions: "In Alan, we write in steps (right, then down) to build a logical tree. Let's write the cascade: <strong>'I want you'</strong>. Indent to nest the receiver ('you') under the action ('want').",
      hint: "Press 'want'. Press STEP-RIGHT (Indent) on your left thumb. Press STEP-DOWN to start the nested line, then type 'you'!",
      targetKeys: ["want", "INDENT", "DOWN", "you"],
      validate: (out) => {
        const lines = Array.from(out.querySelectorAll('.line'));
        if (lines.length < 2) return false;
        
        const l0_el = Array.from(lines[0].children).filter(el => el.id !== 'cursor');
        const hasWant = l0_el.length === 1 && l0_el[0].getAttribute('data-handle') === 'want';
        const l0_ind = parseInt(lines[0].getAttribute('data-indent') || '0', 10) === 0;
        
        const l1_el = Array.from(lines[1].children).filter(el => el.id !== 'cursor');
        const hasYou = l1_el.length === 1 && l1_el[0].getAttribute('data-handle') === 'you';
        const l1_ind = parseInt(lines[1].getAttribute('data-indent') || '0', 10) === 1;
        
        return hasWant && l0_ind && hasYou && l1_ind;
      }
    },
    {
      title: "Lesson 4: Temporal Specification",
      progress: "Rung 4/6",
      targetPhrase: "I know now",
      instructions: "Let's ground our thoughts in time. Primes like 'now' specify when an event or state occurs. Let's write the cascade: <strong>'I know now'</strong> by nesting 'now' under 'know'.",
      hint: "Press 'know' (purple Diamond). Press STEP-RIGHT (Indent) on your left thumb, then STEP-DOWN, and press 'now' (cyan double vertical line).",
      targetKeys: ["know", "INDENT", "DOWN", "now"],
      validate: (out) => {
        const lines = Array.from(out.querySelectorAll('.line'));
        if (lines.length < 2) return false;
        
        const l0_el = Array.from(lines[0].children).filter(el => el.id !== 'cursor');
        const hasKnow = l0_el.length === 1 && l0_el[0].getAttribute('data-handle') === 'know';
        const l0_ind = parseInt(lines[0].getAttribute('data-indent') || '0', 10) === 0;
        
        const l1_el = Array.from(lines[1].children).filter(el => el.id !== 'cursor');
        const hasNow = l1_el.length === 1 && l1_el[0].getAttribute('data-handle') === 'now';
        const l1_ind = parseInt(lines[1].getAttribute('data-indent') || '0', 10) === 1;
        
        return hasKnow && l0_ind && hasNow && l1_ind;
      }
    },
    {
      title: "Lesson 5: Cause & Effect (Because)",
      progress: "Rung 5/6",
      targetPhrase: "I know because I see",
      instructions: "Let's build a logical argument using the connective prime 'because' (bik). We'll write: <strong>'I know because I see'</strong>. Each logical step cascades deeper into the tree.",
      hint: "Type 'know'. Press INDENT + STEP-DOWN and type 'because' (bik, the branch-like logic key). Then press INDENT + STEP-DOWN again and type 'see'!",
      targetKeys: ["know", "INDENT", "DOWN", "bik", "INDENT", "DOWN", "see"],
      validate: (out) => {
        const lines = Array.from(out.querySelectorAll('.line'));
        if (lines.length < 3) return false;
        
        const l0_el = Array.from(lines[0].children).filter(el => el.id !== 'cursor');
        const hasKnow = l0_el.length === 1 && l0_el[0].getAttribute('data-handle') === 'know';
        const l0_ind = parseInt(lines[0].getAttribute('data-indent') || '0', 10) === 0;
        
        const l1_el = Array.from(lines[1].children).filter(el => el.id !== 'cursor');
        const hasBik = l1_el.length === 1 && l1_el[0].getAttribute('data-handle') === 'bik';
        const l1_ind = parseInt(lines[1].getAttribute('data-indent') || '0', 10) === 1;

        const l2_el = Array.from(lines[2].children).filter(el => el.id !== 'cursor');
        const hasSee = l2_el.length === 1 && l2_el[0].getAttribute('data-handle') === 'see';
        const l2_ind = parseInt(lines[2].getAttribute('data-indent') || '0', 10) === 2;
        
        return hasKnow && l0_ind && hasBik && l1_ind && hasSee && l2_ind;
      }
    },
    {
      title: "Lesson 6: Spatial Location (Move Here)",
      progress: "Rung 6/6",
      targetPhrase: "I move here",
      instructions: "To specify where an action happens, we nest a spatial prime under it. Let's write the action: <strong>'I move here'</strong> by nesting 'place' under 'move'!",
      hint: "Press 'move' (orange double arrow). Press INDENT + STEP-DOWN on your thumbs, then press 'place' (blue vertical line with center dot).",
      targetKeys: ["mov", "INDENT", "DOWN", "place"],
      validate: (out) => {
        const lines = Array.from(out.querySelectorAll('.line'));
        if (lines.length < 2) return false;
        
        const l0_el = Array.from(lines[0].children).filter(el => el.id !== 'cursor');
        const hasMov = l0_el.length === 1 && l0_el[0].getAttribute('data-handle') === 'mov';
        const l0_ind = parseInt(lines[0].getAttribute('data-indent') || '0', 10) === 0;
        
        const l1_el = Array.from(lines[1].children).filter(el => el.id !== 'cursor');
        const hasPlace = l1_el.length === 1 && l1_el[0].getAttribute('data-handle') === 'place';
        const l1_ind = parseInt(lines[1].getAttribute('data-indent') || '0', 10) === 1;
        
        return hasMov && l0_ind && hasPlace && l1_ind;
      }
    }
  ];

  let currentLessonIdx = 0;
  let currentStep = 0;

  function loadLesson(idx) {
    currentLessonIdx = idx;
    const l = lessons[idx];
    lessonTitleEl.textContent = l.title;
    lessonProgressEl.textContent = l.progress;
    lessonInstructionsEl.innerHTML = l.instructions;
    lessonHintEl.innerHTML = l.hint;
    lessonTargetPhraseEl.textContent = `"${l.targetPhrase}"`;
    
    // Update active tab button style
    document.querySelectorAll('.tab-btn').forEach((btn, i) => {
      btn.classList.toggle('active', i === idx);
    });
    
    resetWorkspace();
  }

  function resetWorkspace() {
    // Clear Output Display
    output.innerHTML = '<div class="line" data-indent="0"><div class="cursor" id="cursor"></div></div>';
    activeLine = output.querySelector('.line');
    cursor = document.getElementById('cursor');
    currentIndent = 0;
    
    currentStep = 0;
    isFlipped = false;
    document.querySelector('.split-keyboard').classList.remove('flipped');
    const flipKey = document.querySelector('.key[data-action="FLIP"]');
    if (flipKey) flipKey.classList.remove('active');
    
    successBanner.style.display = 'none';
    highlightNextKey();
    updateChecklist();
  }

  // Generate tab buttons dynamically based on lessons array
  const tabsContainer = document.getElementById('lessonTabs');
  tabsContainer.innerHTML = '';
  lessons.forEach((l, idx) => {
    const btn = document.createElement('button');
    btn.className = `tab-btn ${idx === 0 ? 'active' : ''}`;
    btn.id = `tab${idx}`;
    btn.textContent = `Rung ${idx + 1}`;
    btn.addEventListener('click', () => loadLesson(idx));
    tabsContainer.appendChild(btn);
  });

  function highlightNextKey() {
    document.querySelectorAll('.key').forEach(k => k.classList.remove('highlight'));
    
    const l = lessons[currentLessonIdx];
    if (!l || currentStep >= l.targetKeys.length) return;
    
    const target = l.targetKeys[currentStep];
    let keyEl = document.querySelector(`.key[data-action="${target}"]`) || 
                document.querySelector(`.key[data-handle="${target}"]`);
                
    if (keyEl) {
      keyEl.classList.add('highlight');
    }
  }

  function updateChecklist() {
    const l = lessons[currentLessonIdx];
    const checklistEl = document.getElementById('checklist');
    checklistEl.innerHTML = '';
    
    l.targetKeys.forEach((keyName, i) => {
      const item = document.createElement('div');
      item.style.display = 'flex';
      item.style.alignItems = 'center';
      item.style.gap = '8px';
      
      const check = document.createElement('span');
      check.innerHTML = i < currentStep ? '✓' : '○';
      check.style.color = i < currentStep ? '#7fcf9f' : '#5d626c';
      check.style.fontWeight = 'bold';
      
      const text = document.createElement('span');
      let displayKeyName = keyName;
      if (keyName === 'liv') displayKeyName = isFlipped ? 'die (flipped live)' : 'live';
      if (keyName === 'want') displayKeyName = 'want';
      if (keyName === 'think') displayKeyName = 'think';
      if (keyName === 'FLIP') displayKeyName = 'anti';
      
      text.textContent = `Step ${i+1}: press ${displayKeyName.toUpperCase()}`;
      text.style.color = i < currentStep ? '#7fcf9f' : (i === currentStep ? '#fff' : '#5d626c');
      if (i === currentStep) text.style.textDecoration = 'underline';
      
      item.appendChild(check);
      item.appendChild(text);
      checklistEl.appendChild(item);
    });
  }

  function checkLessonProgress() {
    const l = lessons[currentLessonIdx];
    const passed = l.validate(currentLessonIdx === 0 ? activeLine : output);
    
    if (passed) {
      document.querySelectorAll('.key').forEach(k => k.classList.remove('highlight'));
      
      // Update success banner next button label
      if (currentLessonIdx === lessons.length - 1) {
        btnNext.textContent = "Finish & Return";
      } else {
        btnNext.textContent = "Next Lesson ➔";
      }
      
      successBanner.style.display = 'flex';
    }
  }

  btnNext.addEventListener('click', () => {
    if (currentLessonIdx === lessons.length - 1) {
      window.location.href = "keyboard_prototype.html";
    } else {
      currentLessonIdx++;
      loadLesson(currentLessonIdx);
    }
  });


  const keys = document.querySelectorAll('.key');

  keys.forEach(key => {
    key.addEventListener('click', () => {
      const action = key.getAttribute('data-action');
      const handle = key.getAttribute('data-handle');
      
      const l = lessons[currentLessonIdx];
      const target = l.targetKeys[currentStep];

      const pressedId = action || handle;
      if (pressedId === target) {
        currentStep++;
      } else if (pressedId === 'BACK') {
        currentStep = Math.max(currentStep - 1, 0);
      }

      if (action === 'FLIP') {
        isFlipped = !isFlipped;
        document.querySelector('.split-keyboard').classList.toggle('flipped', isFlipped);
        key.classList.toggle('active', isFlipped);
        highlightNextKey();
        updateChecklist();
        return;
      }

      if (action === 'INDENT') {
        currentIndent = Math.min(currentIndent + 1, 4);
        activeLine.setAttribute('data-indent', currentIndent);
        activeLine.style.paddingLeft = `${currentIndent * 40}px`;
        highlightNextKey();
        updateChecklist();
        checkLessonProgress();
        return;
      }

      if (action === 'OUTDENT') {
        currentIndent = Math.max(currentIndent - 1, 0);
        activeLine.setAttribute('data-indent', currentIndent);
        activeLine.style.paddingLeft = `${currentIndent * 40}px`;
        highlightNextKey();
        updateChecklist();
        checkLessonProgress();
        return;
      }

      if (action === 'DOWN') {
        const newLine = document.createElement('div');
        newLine.className = 'line';
        newLine.setAttribute('data-indent', currentIndent);
        newLine.style.paddingLeft = `${currentIndent * 40}px`;
        
        cursor.remove();
        newLine.appendChild(cursor);
        
        output.appendChild(newLine);
        activeLine = newLine;
        output.scrollTop = output.scrollHeight;
        highlightNextKey();
        updateChecklist();
        checkLessonProgress();
        return;
      }

      if (action === 'SPACE') {
        const spacer = document.createElement('div');
        spacer.className = 'spacer';
        activeLine.insertBefore(spacer, cursor);
        highlightNextKey();
        updateChecklist();
        checkLessonProgress();
        return;
      }

      if (action === 'BACK') {
        const prev = cursor.previousElementSibling;
        if (prev) {
          prev.remove();
        } else {
          const prevLine = activeLine.previousElementSibling;
          if (prevLine) {
            cursor.remove();
            prevLine.appendChild(cursor);
            activeLine.remove();
            activeLine = prevLine;
            currentIndent = parseInt(activeLine.getAttribute('data-indent') || '0', 10);
            output.scrollTop = output.scrollHeight;
          }
        }
        highlightNextKey();
        updateChecklist();
        checkLessonProgress();
        return;
      }

      // Default: typing a symbol
      const svg = key.querySelector('svg');
      if (svg) {
        const clone = svg.cloneNode(true);
        const flipType = key.getAttribute('data-flip');
        if (isFlipped && flipType) {
          clone.classList.add(`flipped-${flipType}`);
          clone.setAttribute('data-flipped', 'true');
        }
        if (handle) {
          clone.setAttribute('data-handle', handle);
        }
        
        activeLine.insertBefore(clone, cursor);
        
        // Auto reset flip after typing if it was a flippable key
        if (isFlipped && flipType) {
          isFlipped = false;
          document.querySelector('.split-keyboard').classList.remove('flipped');
          const flipKey = document.querySelector('.key[data-action="FLIP"]');
          if (flipKey) flipKey.classList.remove('active');
        }
      }
      
      highlightNextKey();
      updateChecklist();
      checkLessonProgress();
    });
  });

  // Start tutorial
  loadLesson(0);
</script>
</body>
</html>
"""

with open('/Users/calexander/writing-system-for-ai/tutorial.html', 'w') as f:
    f.write(html_start)

print("Tutorial generated successfully!")
