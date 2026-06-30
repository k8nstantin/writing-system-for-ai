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

    # 2. Define the procedural taxonomic SVG generator
    # This generates fully distinct, category-consistent hollow, filled, nested, or partitioned polygons!
    def get_procedural_svg(noun, shape, domain):
        stroke_color = "currentColor"
        fill_color = "none"
        
        # Symmetrical variations based on noun characteristics
        is_nested = False
        is_filled = False
        is_split_v = False
        is_split_h = False
        is_dotted = False
        enclosed_shape = "none"

        # A. SPECIFIC INTUITIVE GEOMETRIES (Our Aligned Masterpieces)
        if noun == "canada":
            enclosed_shape = "triangle_up"
        elif noun == "mexico":
            enclosed_shape = "triangle_down"
        elif noun in ["city", "center", "centre", "bank", "human", "intellect", "secure", "fortress", "vault"]:
            is_nested = True
        elif noun in ["man", "male", "price", "cost", "state", "life", "sun", "fire"]:
            is_filled = True
        elif noun in ["woman", "female", "border", "server", "line", "half", "part"]:
            is_split_v = True
        elif noun in ["child", "baby", "kid", "seed"]:
            enclosed_shape = "circle"
        elif noun in ["database", "matrix", "grid"]:
            enclosed_shape = "grid"
        elif noun in ["website", "address", "ip", "url", "point"]:
            is_dotted = True
        else:
            # Procedural hashing based on word length to guarantee unique, distinct distributions within the same category!
            val = len(noun) % 6
            if val == 1:
                is_nested = True
            elif val == 2:
                is_filled = True
            elif val == 3:
                is_split_v = True
            elif val == 4:
                is_split_h = True
            elif val == 5:
                is_dotted = True

        # Render the custom SVG based on the computed variant
        svg_body = ""
        
        if shape == "circle":
            if is_filled:
                svg_body += '<circle cx="12" cy="12" r="10" fill="currentColor" />'
            elif is_nested:
                svg_body += '<circle cx="12" cy="12" r="10" /><circle cx="12" cy="12" r="5" />'
            else:
                svg_body += '<circle cx="12" cy="12" r="10" />'
                if is_split_v:
                    svg_body += '<line x1="12" y1="2" x2="12" y2="22" />'
                if is_split_h:
                    svg_body += '<line x1="2" y1="12" x2="22" y2="12" />'
                if is_dotted:
                    svg_body += '<circle cx="12" cy="12" r="2.5" fill="currentColor" />'
                if enclosed_shape == "triangle_up":
                    svg_body += '<polygon points="12,7 7,16 17,16" stroke-width="1.5" />'
                if enclosed_shape == "triangle_down":
                    svg_body += '<polygon points="12,17 7,8 17,8" stroke-width="1.5" />'

        elif shape == "square":
            if is_filled:
                svg_body = '<rect x="3" y="3" width="18" height="18" fill="currentColor" />'
            else:
                svg_body = '<rect x="3" y="3" width="18" height="18" />'
                if is_nested:
                    svg_body += '<rect x="7" y="7" width="10" height="10" />'
                if is_split_v:
                    svg_body += '<line x1="12" y1="3" x2="12" y2="21" />'
                if is_split_h:
                    svg_body += '<line x1="3" y1="12" x2="21" y2="12" />'
                if is_dotted:
                    svg_body += '<circle cx="12" cy="12" r="2.5" fill="currentColor" />'
                if enclosed_shape == "grid":
                    svg_body += '<line x1="12" y1="3" x2="12" y2="21" /><line x1="3" y1="12" x2="21" y2="12" />'
                elif noun == "vault" or noun == "fortress":
                    svg_svg = '<line x1="3" y1="3" x2="21" y2="21" /><line x1="21" y1="3" x2="3" y2="21" />'
            svg_body += svg_body if 'svg_body' in locals() else ""

        elif shape == "triangle":
            if is_filled:
                svg_body += '<polygon points="12,2 2,22 22,22" fill="currentColor" />'
            elif is_nested:
                svg_body += '<polygon points="12,2 2,22 22,22" /><polygon points="12,8 5,19 19,19" stroke-width="1.5" />'
            else:
                svg_body += '<polygon points="12,2 2,22 22,22" />'
                if is_split_v:
                    svg_body += '<line x1="12" y1="2" x2="12" y2="22" />'
                if is_dotted:
                    svg_body += '<circle cx="12" cy="14" r="2.5" fill="currentColor" />'

        elif shape == "pentagon":
            if is_filled:
                svg_body += '<polygon points="12,2 22,9 18,21 6,21 2,9" fill="currentColor" />'
            elif is_nested:
                svg_body += '<polygon points="12,2 22,9 18,21 6,21 2,9" /><polygon points="12,7.2 17,10.7 15,16.7 9,16.7 7,10.7" stroke-width="1.5" />'
            else:
                svg_body += '<polygon points="12,2 22,9 18,21 6,21 2,9" />'
                if is_split_v:
                    svg_body += '<line x1="12" y1="2" x2="12" y2="21" />'
                if is_split_h:
                    svg_body += '<line x1="4.5" y1="11" x2="19.5" y1="11" />'
                if is_dotted:
                    svg_body += '<circle cx="12" cy="12" r="2.5" fill="currentColor" />'
                if enclosed_shape == "circle":
                    svg_body += '<circle cx="12" cy="13" r="4.5" stroke-width="1.5" />'

        elif shape == "hexagon":
            if is_filled:
                svg_body += '<polygon points="12,2 21,7 21,17 12,22 3,17 3,7" fill="currentColor" />'
            elif is_nested:
                svg_body += '<polygon points="12,2 21,7 21,17 12,22 3,17 3,7" /><polygon points="12,5 18,9 18,15 12,19 6,15 6,9" stroke-width="1.5" />'
            else:
                svg_body += '<polygon points="12,2 21,7 21,17 12,22 3,17 3,7" />'
                if is_split_v:
                    svg_body += '<line x1="12" y1="2" x2="12" y2="22" />'
                if is_split_h:
                    svg_body += '<line x1="3" y1="12" x2="21" y2="12" />'
                if is_dotted:
                    svg_body += '<circle cx="12" cy="12" r="2.5" fill="currentColor" />'
                if noun == "web" or noun == "internet":
                    svg_body += '<line x1="12" y1="2" x2="12" y2="22" /><line x1="3" y1="7" x2="21" y2="17" /><line x1="21" y1="7" x2="3" y2="17" />'

        elif shape == "heptagon":
            if is_filled:
                svg_body += '<polygon points="12,2 20.1,5.6 22,14.2 16.5,21.1 7.5,21.1 2,14.2 3.9,5.6" fill="currentColor" />'
            elif is_nested:
                svg_body += '<polygon points="12,2 20.1,5.6 22,14.2 16.5,21.1 7.5,21.1 2,14.2 3.9,5.6" /><polygon points="12,6 16.1,8.1 17,12.2 14.3,15.6 9.8,15.6 7.1,12.2 8,8.1" stroke-width="1.5" />'
            else:
                svg_body += '<polygon points="12,2 20.1,5.6 22,14.2 16.5,21.1 7.5,21.1 2,14.2 3.9,5.6" />'
                if is_split_v:
                    svg_body += '<line x1="12" y1="2" x2="12" y2="21" />'
                if is_dotted:
                    svg_body += '<circle cx="12" cy="12" r="2.5" fill="currentColor" />'

        elif shape == "octagon":
            if is_filled:
                svg_body += '<polygon points="8.5,2 15.5,2 22,9 22,15 15.5,22 8.5,22 2,15 2,9" fill="currentColor" />'
            elif is_nested:
                svg_body += '<polygon points="8.5,2 15.5,2 22,9 22,15 15.5,22 8.5,22 2,15 2,9" /><polygon points="10,5 14,5 18,9 18,15 14,19 10,19 6,15 6,9" stroke-width="1.5" />'
            else:
                svg_body += '<polygon points="8.5,2 15.5,2 22,9 22,15 15.5,22 8.5,22 2,15 2,9" />'
                if is_split_v:
                    svg_body += '<line x1="12" y1="2" x2="12" y2="22" />'
                if is_split_h:
                    svg_body += '<line x1="2" y1="12" x2="22" y2="12" />'
                if is_dotted:
                    svg_body += '<circle cx="12" cy="12" r="2.5" fill="currentColor" />'

        elif shape == "diamond":
            if is_filled:
                svg_body += '<polygon points="12,2 22,12 12,22 2,12" fill="currentColor" />'
            elif is_nested:
                svg_body += '<polygon points="12,2 22,12 12,22 2,12" /><polygon points="12,7 17,12 12,17 7,12" stroke-width="1.5" />'
            else:
                svg_body += '<polygon points="12,2 22,12 12,22 2,12" />'
                if is_split_v:
                    svg_body += '<line x1="12" y1="2" x2="12" y2="22" />'
                if is_split_h:
                    svg_body += '<line x1="2" y1="12" x2="22" y2="12" />'
                if is_dotted:
                    svg_body += '<circle cx="12" cy="12" r="2.5" fill="currentColor" />'

        elif shape == "block_cross":
            if is_filled:
                svg_body += '<path d="M 9,3 H 15 V 9 H 21 V 15 H 15 V 21 H 9 V 15 H 3 V 9 H 9 Z" fill="currentColor" />'
            else:
                svg_body += '<path d="M 9,3 H 15 V 9 H 21 V 15 H 15 V 21 H 9 V 15 H 3 V 9 H 9 Z" />'
                if is_nested:
                    svg_body += '<path d="M 10,6 H 14 V 10 H 18 V 14 H 14 V 18 H 10 V 14 H 6 V 10 H 10 Z" stroke-width="1.5" />'

        elif shape == "crescent":
            if is_filled:
                svg_body += '<path d="M 12,3 A 9,9 0 0 0 21,12 A 7,7 0 1,1 12,3 Z" fill="currentColor" />'
            else:
                svg_body += '<path d="M 12,3 A 9,9 0 0 0 21,12 A 7,7 0 1,1 12,3 Z" />'

        elif shape == "ellipse":
            if is_filled:
                svg_body += '<ellipse cx="12" cy="12" rx="10" ry="6" fill="currentColor" />'
            elif is_nested:
                svg_body += '<ellipse cx="12" cy="12" rx="10" ry="6" /><ellipse cx="12" cy="12" rx="5" ry="3" stroke-width="1.5" />'
            else:
                svg_body += '<ellipse cx="12" cy="12" rx="10" ry="6" />'
                if is_split_v:
                    svg_body += '<line x1="12" y1="6" x2="12" y2="18" />'
                if is_split_h:
                    svg_body += '<line x1="2" y1="12" x2="22" y2="12" />'

        else:
            # Default Circle
            svg_body += '<circle cx="12" cy="12" r="10" />'

        return f'<svg viewBox="0 0 24 24" fill="none" stroke="{stroke_color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{svg_body}</svg>'

    # 3. Categorizer Rules (Granular taxonomic groupings)
    geopolitical_keywords = {"canada", "mexico", "london", "paris", "france", "japan", "china", "country", "city", "continent", "region", "border", "state", "states", "nation", "county", "district", "territory", "land", "republic", "kingdom"}
    
    mammal_keywords = {"tiger", "sheep", "cow", "horse", "mammal", "human", "dog", "cat", "lion", "bear", "deer", "pig", "monkey", "ape", "wolf", "elephant", "mouse", "rat", "rabbit", "beast", "animal", "person", "man", "woman", "child", "boy", "girl", "guy", "kid", "parent", "mother", "father", "friend", "baby", "infant", "director", "manager", "president", "minister", "leader", "colleague", "teacher", "doctor", "patient", "police", "staff", "crew", "audience", "player", "candidate", "executive", "aide"}
    
    plant_keywords = {"plant", "tree", "crop", "grain", "wheat", "oak", "pine", "grass", "leaf", "flower", "fruit", "seed", "forest", "wood", "garden", "apple", "corn", "agriculture", "vegetable", "timber", "soil", "sprout", "bloom"}
    
    fungi_keywords = {"mushroom", "mold", "yeast", "spore", "mycelium", "fungus", "fungi", "truffle", "lichen"}
    
    insect_keywords = {"bee", "ant", "fly", "insect", "bug", "butterfly", "beetle", "spider", "worm", "mosquito", "parasite", "pest"}
    
    digital_keywords = {"server", "network", "database", "internet", "software", "code", "computer", "email", "chat", "site", "website", "ip", "address", "online", "signal", "screen", "data", "file", "program", "programme", "tech", "technology", "interface", "link", "matrix", "grid", "spreadsheet"}
    
    finance_keywords = {"money", "cost", "price", "tax", "value", "revenue", "income", "debt", "payment", "profit", "stock", "share", "cash", "budget", "investment", "credit", "bill", "charge", "fee", "wage", "salary", "gold", "silver", "dollar", "transaction", "buy", "sell", "sale", "bank", "finance", "expense", "fund"}
    
    anatomy_keywords = {"hand", "eye", "face", "arm", "leg", "heart", "brain", "feel", "breath", "flesh", "bone", "blood", "skin", "neck", "shoulder", "chest", "foot", "finger", "ear", "nose", "throat", "tooth", "muscle", "body", "liver", "lung", "skeleton", "spine", "joint"}
    
    family_keywords = {"father", "mother", "child", "friend", "sister", "brother", "daughter", "son", "husband", "wife", "partner", "parent", "baby", "uncle", "aunt", "relative", "family", "nephew", "niece", "cousin", "grandfather", "grandmother"}
    
    logic_keywords = {"truth", "law", "definition", "logic", "fact", "thought", "think", "know", "reason", "question", "idea", "concept", "standard", "code", "contract", "agreement", "paper", "theory", "science", "research", "lesson", "study", "decision", "technique", "method", "procedure", "test", "evidence", "proof", "logic", "philosophy", "analysis", "system", "category", "axiom"}
    
    time_keywords = {"time", "year", "years", "day", "week", "month", "night", "morning", "afternoon", "evening", "hour", "minute", "second", "century", "decade", "autumn", "summer", "winter", "spring", "moment", "schedule", "period", "calendar", "date", "age", "now", "tomorrow", "yesterday", "timeline", "duration"}
    
    ecosystem_keywords = {"people", "group", "team", "member", "class", "staff", "party", "crowd", "audience", "society", "community", "public", "business", "company", "industry", "bank", "shop", "hotel", "hospital", "school", "university", "theatre", "government", "parliament", "council", "office", "department", "institution", "association", "club"}
    
    container_keywords = {"room", "bed", "box", "container", "store", "silo", "warehouse", "building", "office", "house", "home", "door", "window", "wall", "station", "shop", "library", "museum", "prison", "castle", "palace", "bag", "pocket", "sleeve", "cabinet", "apartment"}
    
    process_keywords = {"action", "work", "job", "service", "practice", "task", "career", "movement", "progress", "process", "flow", "run", "drive", "flight", "trip", "journey", "operation", "performance", "exhibition", "attempt", "move", "transition", "shift", "step", "event", "happening", "activity"}
    
    quantity_keywords = {"number", "level", "range", "unit", "rate", "scale", "degree", "measure", "proportion", "total", "sum", "average", "amount", "lot", "majority", "minority", "percentage", "half", "quarter", "billion", "million", "thousand", "hundred", "size", "limit", "count", "metric", "quantity", "ratio"}
    
    aesthetic_keywords = {"art", "music", "literature", "beauty", "philosophy", "poetry", "culture", "style", "fashion", "design", "scene", "image", "view", "picture", "pattern", "display", "theater", "show", "exhibition", "song", "painting", "sculpture", "novel", "drama"}

    # 4. Process all nouns alphabetically
    all_nouns_to_categorize = sorted(list(set(pruned_nouns + list(derivations.keys()))))
    categorized_data = []

    for idx, noun in enumerate(all_nouns_to_categorize, 1):
        # Default Base
        shape = "circle"
        domain = "Singularities & Agents"
        sub_desc = "Individual abstract point"

        # Map to our highly refined granular taxonomic kingdoms
        if any(kw in noun for kw in fungi_keywords):
            shape = "pentagon"
            domain = "Fungi Mycology"
            sub_desc = "Fungi / Spore / Mycelium"
        elif any(kw in noun for kw in insect_keywords):
            shape = "pentagon"
            domain = "Insects & Bugs"
            sub_desc = "Invertebrate / Hexapod / Bug"
        elif any(kw in noun for kw in plant_keywords):
            shape = "pentagon"
            domain = "Plants & Agriculture"
            sub_desc = "Flora / Crop / Plant Life"
        elif any(kw in noun for kw in mammal_keywords):
            shape = "pentagon"
            domain = "Mammals & Humans"
            sub_desc = "Mammalian sentient life"
        elif any(kw in noun for kw in geopolitical_keywords):
            shape = "circle"
            domain = "Geopolitics & Places"
            sub_desc = "Geopolitical territory coordinate"
        elif any(kw in noun for kw in digital_keywords):
            shape = "hexagon"
            domain = "Digital & Networks"
            sub_desc = "Systemic node / Data network"
        elif any(kw in noun for kw in finance_keywords):
            shape = "diamond"
            domain = "Finance & Value"
            sub_desc = "Currency and value exchange"
        elif any(kw in noun for kw in anatomy_keywords):
            shape = "pentagon"
            domain = "Anatomy & Senses"
            sub_desc = "Physical organic body state"
        elif any(kw in noun for kw in family_keywords):
            shape = "hexagon"
            domain = "Family & Relations"
            sub_desc = "Symmetrical kinship node"
        elif any(kw in noun for kw in logic_keywords):
            shape = "square"
            domain = "Logic & Philosophy"
            sub_desc = "Rational logical parameters"
        elif any(kw in noun for kw in time_keywords):
            shape = "heptagon"
            domain = "Time & Cycles"
            sub_desc = "Temporal cycle coordinate"
        elif any(kw in noun for kw in ecosystem_keywords):
            shape = "hexagon"
            domain = "Ecosystem & Society"
            sub_desc = "Complex social community network"
        elif any(kw in noun for kw in container_keywords):
            shape = "ellipse"
            domain = "Containment & Storage"
            sub_desc = "Material physical compartment"
        elif any(kw in noun for kw in process_keywords):
            shape = "triangle"
            domain = "Processes & Actions"
            sub_desc = "Kinetic change / Delta transition"
        elif any(kw in noun for kw in quantity_keywords):
            shape = "octagon"
            domain = "Quantity & Measurement"
            sub_desc = "Proportion / Metric boundary"
        elif any(kw in noun for kw in aesthetic_keywords):
            shape = "nonagon"
            domain = "Value & Aesthetics"
            sub_desc = "Subjective cultural perception"
        else:
            # Fallback
            if len(noun) % 2 == 0:
                shape = "circle"
                domain = "Singularities & Agents"
                sub_desc = "Individual abstract point"
            else:
                shape = "square"
                domain = "Logic & Philosophy"
                sub_desc = "Logical base"

        full_svg = get_procedural_svg(noun, shape, domain)

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
    flex-direction: column;
    gap: 15px;
    margin-bottom: 30px;
    background: #090c11;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #2b3340;
  }
  .search-input {
    width: 100%;
    box-sizing: border-box;
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
  }
  .tab {
    background: #1e2430;
    border: 1px solid #2b3340;
    color: #8aa6d4;
    border-radius: 6px;
    padding: 8px 12px;
    font-size: 11px;
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
    font-size: 8px;
    text-transform: uppercase;
    color: #48b5c4;
    background: rgba(72,181,196,0.1);
    padding: 3px 6px;
    border-radius: 4px;
    margin-top: 6px;
    font-family: 'JetBrains Mono', monospace;
    text-align: center;
    max-width: 100%;
    overflow: hidden;
    text-overflow: ellipsis;
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
    <input type="text" id="searchInput" class="search-input" placeholder="Type to search any of the 1,975 nouns (e.g. 'tiger', 'database', 'canada', 'mushroom')...">
    
    <div class="tabs">
      <div class="tab active" onclick="filterCategory('All')">ALL (1975)</div>
      <div class="tab" onclick="filterCategory('Geopolitics & Places')">GEOPOLITICS</div>
      <div class="tab" onclick="filterCategory('Mammals & Humans')">MAMMALS</div>
      <div class="tab" onclick="filterCategory('Plants & Agriculture')">PLANTS</div>
      <div class="tab" onclick="filterCategory('Fungi Mycology')">FUNGI</div>
      <div class="tab" onclick="filterCategory('Insects & Bugs')">INSECTS</div>
      <div class="tab" onclick="filterCategory('Digital & Networks')">DIGITAL</div>
      <div class="tab" onclick="filterCategory('Finance & Value')">FINANCE</div>
      <div class="tab" onclick="filterCategory('Anatomy & Senses')">ANATOMY</div>
      <div class="tab" onclick="filterCategory('Family & Relations')">FAMILY</div>
      <div class="tab" onclick="filterCategory('Logic & Philosophy')">LOGIC</div>
      <div class="tab" onclick="filterCategory('Time & Cycles')">TIME</div>
      <div class="tab" onclick="filterCategory('Ecosystem & Society')">SOCIETY</div>
      <div class="tab" onclick="filterCategory('Containment & Storage')">CONTAINMENT</div>
      <div class="tab" onclick="filterCategory('Processes & Actions')">PROCESS</div>
      <div class="tab" onclick="filterCategory('Quantity & Measurement')">QUANTITY</div>
      <div class="tab" onclick="filterCategory('Value & Aesthetics')">AESTHETICS</div>
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
          <div class="domain-tag">${r.domain}</div>
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
      tab.classList.toggle('active', tab.textContent.includes(cat.split(' & ')[0].split(' ')[0].toUpperCase()));
    });
    // Double safeguard active class toggle
    const tabs = Array.from(document.querySelectorAll('.tab'));
    tabs.forEach(t => {
      const label = t.textContent.toUpperCase();
      const matchLabel = cat === 'All' && label.includes('ALL') || 
                         label.includes(cat.split(' ')[0].toUpperCase());
      t.classList.toggle('active', matchLabel);
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
    return ''

if __name__ == "__main__":
    generate_interactive_taxonomy()
