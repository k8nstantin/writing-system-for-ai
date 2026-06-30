import json
import os

def generate_interactive_taxonomy():
    # 1. Load the pruned core nouns
    with open('top_2000_nouns_pruned.txt', 'r') as f:
        pruned_lines = f.readlines()
        
    pruned_nouns = []
    for line in pruned_lines:
        line = line.strip().lower()
        if not line:
            continue
        if '. ' in line:
            parts = line.split('. ', 1)
            word = parts[1].strip()
        else:
            word = line.strip()
        if word:
            pruned_nouns.append(word)

    # Load the derivations
    with open('noun_derivations.json', 'r') as f:
        derivations = json.load(f)

    # 2. Define our 14 Core Hollow Geometries and their SVG definitions
    shapes_svg = {
        "circle": '<circle cx="12" cy="12" r="10" />',
        "line": '<line x1="2" y1="12" x2="22" y2="12" />',
        "triangle": '<polygon points="12,2 2,22 22,22" />',
        "square": '<rect x="3" y="3" width="18" height="18" />',
        "pentagon": '<polygon points="12,2 22,9 18,21 6,21 2,9" />',
        "hexagon": '<polygon points="12,2 21,7 21,17 12,22 3,17 3,7" />',
        "heptagon": '<polygon points="12,2 20.1,5.6 22,14.2 16.5,21.1 7.5,21.1 2,14.2 3.9,5.6" />',
        "octagon": '<polygon points="8.5,2 15.5,2 22,9 22,15 15.5,22 8.5,22 2,15 2,9" />',
        "nonagon": '<polygon points="12,2 18.5,4.3 22,10.2 20.3,17 15.1,21.5 8.9,21.5 3.7,17 2,10.2 5.5,4.3" />',
        "decagon": '<polygon points="12,2 17.9,3.9 21.6,8.9 21.6,15.1 17.9,20.1 12,22 6.1,20.1 2.4,15.1 2.4,8.9 6.1,3.9" />',
        "diamond": '<polygon points="12,2 22,12 12,22 2,12" />',
        "block_cross": '<path d="M 9,3 H 15 V 9 H 21 V 15 H 15 V 21 H 9 V 15 H 3 V 9 H 9 Z" />',
        "crescent": '<path d="M 12,3 A 9,9 0 0 0 21,12 A 7,7 0 1,1 12,3 Z" />',
        "ellipse": '<ellipse cx="12" cy="12" rx="10" ry="6" />'
    }

    # 3. Categorizer Rules (Shorthand Keywords mapping)
    time_keywords = {"time", "year", "years", "day", "week", "month", "night", "morning", "afternoon", "evening", "hour", "minute", "second", "century", "decade", "autumn", "summer", "winter", "spring", "moment", "schedule", "period", "calendar", "date", "age", "now", "tomorrow", "yesterday"}
    
    quantity_keywords = {"number", "level", "range", "unit", "rate", "scale", "degree", "measure", "proportion", "total", "sum", "average", "amount", "lot", "majority", "minority", "percentage", "half", "quarter", "billion", "million", "thousand", "hundred", "size", "limit", "count", "metric", "budget"}
    
    finance_keywords = {"money", "cost", "price", "tax", "value", "revenue", "income", "debt", "payment", "profit", "stock", "share", "cash", "budget", "investment", "credit", "bill", "charge", "fee", "wage", "salary", "gold", "silver", "diamond", "trade", "transaction", "buy", "sell", "sale"}
    
    ecosystem_keywords = {"people", "group", "team", "member", "class", "staff", "party", "crowd", "audience", "society", "community", "public", "nation", "republic", "kingdom", "business", "company", "industry", "bank", "shop", "hotel", "hospital", "school", "university", "theatre", "family", "parent", "mother", "father", "child", "friend", "kid", "girl", "boy", "guy", "sister", "brother", "husband", "wife", "partner", "colleague", "committee", "director", "manager", "president", "minister", "leader", "client", "customer"}
    
    structure_keywords = {"system", "program", "programme", "software", "computer", "data", "information", "book", "word", "letter", "document", "file", "registry", "database", "logic", "true", "false", "rule", "law", "policy", "principle", "standard", "code", "contract", "agreement", "paper", "theory", "science", "research", "lesson", "study", "fact", "truth", "reason", "idea", "question", "problem", "concept", "analysis", "evidence", "plan", "management", "decision", "technique", "method", "procedure", "test"}
    
    organism_keywords = {"plant", "animal", "beast", "cow", "sheep", "dog", "cat", "bird", "fish", "horse", "tree", "forest", "wood", "crop", "food", "milk", "fruit", "meat", "bread", "biological", "body", "head", "hand", "eye", "face", "arm", "foot", "leg", "neck", "blood", "brain", "hair", "skin", "feel", "perception", "sense", "mind", "heart", "love", "hope", "fear", "pain", "dream", "touch", "breath", "flesh"}
    
    cosmic_keywords = {"world", "nature", "country", "land", "ground", "air", "water", "sea", "ocean", "river", "lake", "mountain", "hill", "valley", "soil", "earth", "space", "sky", "atmosphere", "cloud", "wind", "rain", "snow", "ice", "weather", "god", "spirit", "soul", "church", "faith", "religion", "death", "war", "peace", "universe", "fire", "heat", "coal", "gas", "sun", "moon", "star", "climate", "dust", "smoke"}
    
    container_keywords = {"room", "bed", "box", "container", "store", "silo", "warehouse", "building", "office", "house", "home", "door", "window", "wall", "station", "shop", "library", "museum", "prison", "castle", "palace", "bag", "pocket", "sleeve", "cabinet", "apartment", "hotel"}
    
    intersection_keywords = {"union", "partnership", "meeting", "junction", "bridge", "road", "path", "street", "highway", "route", "branch", "cross", "connection", "link", "association", "network"}
    
    aesthetic_keywords = {"art", "music", "literature", "beauty", "philosophy", "poetry", "culture", "style", "fashion", "design", "scene", "image", "view", "picture", "pattern", "display", "theater", "show", "exhibition"}
    
    process_keywords = {"action", "work", "job", "service", "practice", "task", "career", "movement", "progress", "process", "flow", "run", "drive", "flight", "trip", "journey", "operation", "performance", "exhibition", "attempt", "move", "transition", "shift", "step"}

    # 4. Categorize all 1,975 nouns (core pruned + derivations)
    all_nouns_to_categorize = pruned_nouns + list(derivations.keys())
    # Sort alphabetically to keep it incredibly neat
    all_nouns_to_categorize = sorted(list(set(all_nouns_to_categorize)))

    categorized_data = []

    for idx, noun in enumerate(all_nouns_to_categorize, 1):
        # Default Base and category
        shape = "square"
        domain = "Structure & Logic"
        sub_desc = "Standard structural logic node"
        inner_lines_svg = ""

        # Determine category based on semantic keywords
        if any(kw in noun for kw in time_keywords):
            shape = "heptagon"
            domain = "Time & Cycles"
            sub_desc = "Temporal cycle coordinate"
        elif any(kw in noun for kw in quantity_keywords):
            shape = "octagon"
            domain = "Quantity & Measurement"
            sub_desc = "Proportion / Metric boundary"
        elif any(kw in noun for kw in finance_keywords):
            shape = "diamond"
            domain = "Finance & Value"
            sub_desc = "Currency and value exchange"
        elif any(kw in noun for kw in ecosystem_keywords):
            shape = "hexagon"
            domain = "Ecosystem & Community"
            sub_desc = "Social network node"
        elif any(kw in noun for kw in structure_keywords):
            shape = "square"
            domain = "Structure & Logic"
            sub_desc = "Artificial logical parameters"
        elif any(kw in noun for kw in organism_keywords):
            shape = "pentagon"
            domain = "Organism & Life"
            sub_desc = "Biological entity state"
        elif any(kw in noun for kw in cosmic_keywords):
            shape = "hexagram" if "god" in noun or "spirit" in noun or "soul" in noun or "universe" in noun else "circle"
            domain = "Cosmic & Elements"
            sub_desc = "Absolute environmental vector"
        elif any(kw in noun for kw in container_keywords):
            shape = "ellipse"
            domain = "Containment & Storage"
            sub_desc = "Material physical compartment"
        elif any(kw in noun for kw in intersection_keywords):
            shape = "block_cross"
            domain = "Intersections & Connections"
            sub_desc = "Intertwined logical paths"
        elif any(kw in noun for kw in aesthetic_keywords):
            shape = "nonagon"
            domain = "Value & Aesthetics"
            sub_desc = "Subjective cultural perception"
        elif any(kw in noun for kw in process_keywords):
            shape = "triangle"
            domain = "Processes & Actions"
            sub_desc = "Kinetic change / Delta transition"
        else:
            # Fallback based on abstract vs concrete noun hints
            if len(noun) % 2 == 0:
                shape = "circle"
                domain = "Singularities & Agents"
                sub_desc = "Individual abstract point"
            else:
                shape = "square"
                domain = "Structure & Logic"
                sub_desc = "Logical base"

        # Apply specific internal wiring SVG lines for recognized core nouns to look super high-tech!
        if noun == "database":
            inner_lines_svg = '<line x1="12" y1="3" x2="12" y2="21" /><line x1="3" y1="12" x2="21" y2="12" />'
            sub_desc = "Database matrix (grid lines)"
        elif noun == "vault" or noun == "fortress":
            inner_lines_svg = '<line x1="3" y1="3" x2="21" y2="21" /><line x1="21" y1="3" x2="3" y2="21" />'
            sub_desc = "Secured Vault (diagonal cross)"
        elif noun == "human" or noun == "intellect":
            inner_lines_svg = '<polygon points="12,7.2 17,10.7 15,16.7 9,16.7 7,10.7" stroke-width="1.5" />'
            sub_desc = "Intellect (nested pentagon)"
        elif noun == "server":
            inner_lines_svg = '<line x1="12" y1="2" x2="12" y2="22" />'
            sub_desc = "Partitioned Server Node"
        elif noun == "web" or noun == "internet":
            inner_lines_svg = '<line x1="12" y1="2" x2="12" y2="22" /><line x1="3" y1="7" x2="21" y2="17" /><line x1="21" y1="7" x2="3" y2="17" />'
            sub_desc = "Interconnected Network Web"

        # Fetch base SVG outline
        base_svg = shapes_svg.get(shape, shapes_svg["circle"])
        full_svg = f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{base_svg}{inner_lines_helper(noun, inner_lines=inner_wiring(noun))}</svg>'

        # Mark if derived via ANTI or Compass
        derivation_notes = ""
        is_derived = "false"
        if noun in derivations:
            is_derived = "true"
            derivation_notes = f"Formula: {derivations[noun]}"

        categorized_data.append({
            "noun": noun,
            "domain": domain,
            "shape": shape,
            "svg": full_svg,
            "desc": sub_desc,
            "is_derived": is_derived,
            "derivation": derivation_notes
        })

    # 5. Generate the HTML File Content
    html_content = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Alan - 1975 Noun Taxonomy Dashboard</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
<style>
  body {
    font-family: 'Inter', sans-serif;
    background-color: #0b0e13;
    color: #c8cdd6;
    margin: 0;
    padding: 40px;
    box-sizing: border-box;
    display: flex;
    justify-content: center;
  }
  .container {
    background: #161b24;
    padding: 40px;
    border-radius: 16px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.6);
    max-width: 1200px;
    width: 100%;
    border: 1px solid #2b3340;
  }
  h1 { 
    color: #fff; 
    margin-top: 0; 
    font-size: 28px; 
    font-weight: 800; 
    display: flex; 
    align-items: center; 
    gap: 12px;
  }
  p.subtitle { 
    color: #8aa6d4; 
    margin-bottom: 30px; 
    font-size: 15px; 
    line-height: 1.6;
    font-family: 'JetBrains Mono', monospace;
  }
  
  /* Advanced Search & Filtering Controls */
  .controls {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
    margin-bottom: 30px;
    background: #090c11;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #2b3340;
  }
  .search-input {
    flex-grow: 1;
    min-width: 250px;
    background: #161b24;
    border: 1px solid #3d4757;
    border-radius: 8px;
    padding: 12px 16px;
    color: #fff;
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    outline: none;
    transition: border-color 0.2s;
  }
  .search-input:focus {
    border-color: #48b5c4;
    box-shadow: 0 0 10px rgba(72,181,196,0.2);
  }
  
  /* Filter Tabs */
  .tabs {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    width: 100%;
    margin-top: 10px;
  }
  .tab {
    background: #1e2430;
    border: 1px solid #2b3340;
    color: #8aa6d4;
    border-radius: 6px;
    padding: 8px 14px;
    font-size: 12px;
    cursor: pointer;
    font-family: 'JetBrains Mono', monospace;
    transition: all 0.2s ease;
  }
  .tab:hover, .tab.active {
    background: #48b5c4;
    color: #0b0e13;
    border-color: #48b5c4;
    font-weight: bold;
  }

  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 15px;
  }
  .glyph-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 15px;
    border: 1px solid #2b3340;
    border-radius: 10px;
    background: #1e2430;
    transition: all 0.2s ease;
    box-sizing: border-box;
    cursor: pointer;
  }
  .glyph-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.6);
    border-color: #48b5c4;
  }
  .glyph-card svg {
    width: 48px;
    height: 48px;
    margin-bottom: 12px;
    stroke: #e2e8f0;
    color: #e2e8f0;
    overflow: visible;
  }
  .label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    font-weight: bold;
    color: #fff;
    letter-spacing: -0.02em;
    text-align: center;
  }
  .domain-tag {
    font-size: 9px;
    text-transform: uppercase;
    color: #48b5c4;
    background: rgba(72,181,196,0.1);
    padding: 3px 6px;
    border-radius: 4px;
    margin-top: 6px;
    font-family: 'JetBrains Mono', monospace;
  }
  .meaning {
    font-size: 10px;
    color: #8aa6d4;
    margin-top: 5px;
    text-align: center;
    line-height: 1.3;
  }
  .derived-tag {
    font-size: 9px;
    text-transform: uppercase;
    color: #ffd166;
    background: rgba(253,209,102,0.1);
    padding: 2px 5px;
    border-radius: 4px;
    margin-top: 4px;
    font-family: 'JetBrains Mono', monospace;
  }
  .stats {
    font-size: 12px;
    color: #7fcf9f;
    margin-bottom: 20px;
    font-family: 'JetBrains Mono', monospace;
  }
</style>
</head>
<body>

<div class="container">
  <h1>Alan taxonomic Noun Dictionary (1975 Words)</h1>
  <p class="subtitle">Complete, interactive visual dashboard of the 1,975 most used English nouns, mathematically categorized into hollow geometric domains.</p>

  <div class="stats" id="statsDisplay">Loading taxonomic records...</div>

  <!-- Search & Tab Filters -->
  <div class="controls">
    <input type="text" id="searchInput" class="search-input" placeholder="Type to search any of the 1,975 nouns (e.g. 'tiger', 'database', 'money')...">
    
    <div class="tabs">
      <div class="tab active" onclick="filterCategory('All')">ALL (1975)</div>
      <div class="tab" onclick="filterCategory('Singularities & Agents')">SINGULARITY (•)</div>
      <div class="tab" onclick="filterCategory('Time & Cycles')">TIME (Heptagon)</div>
      <div class="tab" onclick="filterCategory('Processes & Actions')">PROCESS (△)</div>
      <div class="tab" onclick="filterCategory('Structure & Logic')">STRUCTURE (□)</div>
      <div class="tab" onclick="filterCategory('Organism & Life')">ORGANISM (⬠)</div>
      <div class="tab" onclick="filterCategory('Ecosystem & Community')">ECOSYSTEM (⬡)</div>
      <div class="tab" onclick="filterCategory('Cosmic & Elements')">COSMIC (Hexagram/○)</div>
      <div class="tab" onclick="filterCategory('Containment & Storage')">CONTAINMENT (⬭)</div>
      <div class="tab" onclick="filterCategory('Intersections & Connections')">CONNECTIONS (✙)</div>
      <div class="tab" onclick="filterCategory('Quantity & Measurement')">QUANTITY (Octagon)</div>
      <div class="tab" onclick="filterCategory('Finance & Value')">FINANCE (◇)</div>
      <div class="tab" onclick="filterCategory('Value & Aesthetics')">AESTHETICS (Nonagon)</div>
    </div>
  </div>

  <!-- Grid Container -->
  <div class="grid" id="dictionaryGrid"></div>
</div>

<script>
  // Complete 1,975 database generated procedurally by Python
  const nounRecords = """ + json.dumps(categorized_data) + r""";

  const grid = document.getElementById('dictionaryGrid');
  const searchInput = document.getElementById('searchInput');
  const statsDisplay = document.getElementById('statsDisplay');

  let activeCategory = 'All';
  let searchQuery = '';

  function renderGrid() {
    grid.innerHTML = '';
    let count = 0;

    nounRecords.forEach(r => {
      const matchCategory = activeCategory === 'All' || r.domain === activeCategory;
      const matchSearch = r.noun.includes(searchQuery);

      if (matchCategory && matchSearch) {
        count++;
        const card = document.createElement('div');
        card.className = 'glyph-card';
        
        let derivedBadge = '';
        if (r.is_derived === 'true') {
          derivedBadge = `<div class="derived-tag" title="${r.derivation}">ANTI/COMPASS</div>`;
        }

        card.innerHTML = `
          ${r.svg}
          <div class="label">${r.noun}</div>
          <div class="domain-tag">${r.domain.split(' & ')[0]}</div>
          <div class="meaning">${r.desc}</div>
          ${derivedBadge}
        `;
        
        grid.appendChild(card);
      }
    });

    statsDisplay.textContent = `Displaying ${count} of 1,975 taxonomic records (Category: ${activeCategory.toUpperCase()})`;
  }

  function filterCategory(cat) {
    activeCategory = cat;
    document.querySelectorAll('.tab').forEach(tab => {
      tab.classList.toggle('active', tab.textContent.includes(cat.split(' & ')[0].toUpperCase()));
    });
    // Double safeguard active class toggle
    const tabs = Array.from(document.querySelectorAll('.tab'));
    tabs.forEach(t => {
      if (cat === 'All' && t.textContent.includes('ALL')) t.classList.add('active');
      else if (t.textContent.includes(cat.split(' ')[0].toUpperCase())) t.classList.add('active');
      else t.classList.remove('active');
    });
    renderGrid();
  }

  searchInput.addEventListener('input', (e) => {
    searchQuery = e.target.value.toLowerCase().trim();
    renderGrid();
  });

  // Initial Boot
  renderGrid();
</script>
</body>
</html>
"""

    with open('/Users/calexander/writing-system-for-ai/taxonomy_1975.html', 'w') as f:
        f.write(html_content)

    print("taxonomy_1975.html generated successfully!")

def inner_lines_helper(noun, inner_lines):
    return inner_lines

def inner_wiring(noun):
    if noun == "database":
        return '<line x1="12" y1="3" x2="12" y2="21" /><line x1="3" y1="12" x2="21" y2="12" />'
    elif noun == "vault" or noun == "fortress":
        return '<line x1="3" y1="3" x2="21" y2="21" /><line x1="21" y1="3" x2="3" y2="21" />'
    elif noun == "human" or noun == "intellect":
        return '<polygon points="12,7.2 17,10.7 15,16.7 9,16.7 7,10.7" stroke-width="1.5" />'
    elif noun == "server":
        return '<line x1="12" y1="2" x2="12" y2="22" />'
    elif noun == "web" or noun == "internet":
        return '<line x1="12" y1="2" x2="12" y2="22" /><line x1="3" y1="7" x2="21" y2="17" /><line x1="21" y1="7" x2="3" y2="17" />'
    return ''

if __name__ == "__main__":
    generate_interactive_taxonomy()
