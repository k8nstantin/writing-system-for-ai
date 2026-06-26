import re

svgs = {
    'agt': '<svg style="width: 16px; height: 16px; margin-left: auto; stroke: #8aa6d4;" viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="2" y1="12" x2="22" y2="12" /><circle cx="4" cy="12" r="2" fill="#8aa6d4" /><polyline points="18,8 22,12 18,16" /></svg>',
    'pat': '<svg style="width: 16px; height: 16px; margin-left: auto; stroke: #8aa6d4;" viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="2" y1="12" x2="22" y2="12" /><polyline points="18,8 22,12 18,16" /><line x1="22" y1="6" x2="22" y2="18" /></svg>',
    'rec': '<svg style="width: 16px; height: 16px; margin-left: auto; stroke: #8aa6d4;" viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="2" y1="12" x2="22" y2="12" /><polyline points="18,8 22,12 18,16" /><line x1="22" y1="6" x2="22" y2="18" /></svg>',
    'exp': '<svg style="width: 16px; height: 16px; margin-left: auto; stroke: #8aa6d4;" viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="2" y1="12" x2="22" y2="12" /><polyline points="18,8 22,12 18,16" /><line x1="22" y1="6" x2="22" y2="18" /></svg>',
    'res': '<svg style="width: 16px; height: 16px; margin-left: auto; stroke: #8aa6d4;" viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="2" y1="12" x2="22" y2="12" /><polyline points="18,8 22,12 18,16" stroke-width="4" /></svg>',
    'man': '<svg style="width: 16px; height: 16px; margin-left: auto; stroke: #8aa6d4;" viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M 2 12 Q 7 4 12 12 T 22 12" /><polyline points="18,8 22,12 18,16" /></svg>',
    'tim': '<svg style="width: 16px; height: 16px; margin-left: auto; stroke: #8aa6d4;" viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="2" y1="12" x2="22" y2="12" /><line x1="12" y1="8" x2="12" y2="16" /></svg>'
}

def replace_in_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # replace spans with inline style
    for role, svg in svgs.items():
        content = re.sub(
            r'<span style="font-size: 12px; color: #8aa6d4; text-transform: uppercase; letter-spacing: 0\.5px; width: 40px; text-align: right;(?: margin-top: 4px;)?">' + role + r'</span>',
            f'<div style="width: 40px; display: flex; align-items: center; justify-content: flex-end;" title="{role}">{svg}</div>',
            content
        )
        
        content = re.sub(
            r'<span class="role-label">' + role + r'</span>',
            f'<div style="width: 40px; display: flex; align-items: center; justify-content: flex-end; margin-top: 4px;" title="{role}">{svg}</div>',
            content
        )
    
    with open(filepath, 'w') as f:
        f.write(content)

replace_in_file('/Users/calexander/writing-system-for-ai/index.html')
replace_in_file('/Users/calexander/writing-system-for-ai/generate_svgs.py')

print("SUCCESS")
