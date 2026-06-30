import json

def prune_and_map_nouns():
    # 1. Load the 2,000 raw nouns
    with open('top_2000_nouns.txt', 'r') as f:
        raw_lines = f.readlines()
    
    # Extract clean words, removing numbering if present
    raw_words = []
    for line in raw_lines:
        line = line.strip().lower()
        if not line:
            continue
        # Split on dot if numbered (e.g., "1. time" -> "time")
        if '. ' in line:
            parts = line.split('. ', 1)
            word = parts[1].strip()
        else:
            word = line.strip()
        
        # Clean any extra characters
        word = ''.join(c for c in word if c.isalnum() or c in " -_")
        
        # GRAMMATICAL PLURAL-TO-SINGULAR LEMMATIZATION ENGINE
        # Safeguard native singular terms that end with s
        safeguards = {"species", "series", "business", "address", "process", "congress", "class", "basis", "crisis", "analysis", "mass", "pass", "glass", "press", "dismiss", "loss", "compass"}
        if word not in safeguards:
            if word.endswith('ies'):
                word = word[:-3] + 'y'
            elif word.endswith('ves'):
                word = word[:-3] + 'f'
            elif word.endswith('es') and not word.endswith('ces') and not word.endswith('ses') and not word.endswith('tes') and not word.endswith('nes') and not word.endswith('kes') and not word.endswith('ges') and not word.endswith('des') and not word.endswith('les'):
                word = word[:-2]
            elif word.endswith('s') and not word.endswith('ss') and not word.endswith('us') and word != 'is' and word != 'us':
                word = word[:-1]

        if word:
            raw_words.append(word)

    # Remove duplicates while preserving frequency order
    seen = set()
    nouns_list = []
    for w in raw_words:
        if w not in seen:
            seen.add(w)
            nouns_list.append(w)

    # 2. Define the Universal Compression & Derivation Maps
    
    # A. COMPASS SPACE VECTORS: Nouns that are represented purely as Base Space + Compass Direction
    compass_derivations = {
        "north": "place + above (Compass)",
        "south": "place + below (Compass)",
        "east": "place + right (Compass)",
        "west": "place + left (Compass)",
        "top": "place + above (Compass)",
        "bottom": "place + below (Compass)",
        "inside": "place + in (Compass)",
        "outside": "place + out (Compass)",
        "front": "place + forward (Compass)",
        "back": "place + backward (Compass)",
        "center": "place + center (Compass)",
        "centre": "place + center (Compass)",
        "side": "place + left/right (Compass)",
        "edge": "place + extreme (Compass)",
        "corner": "place + corner (Compass)",
        "middle": "place + center (Compass)"
    }

    # B. COMPASS TIME VECTORS: Nouns represented as Base Time + Compass Direction
    time_derivations = {
        "before": "time + left (Compass Past)",
        "past": "time + left (Compass Past)",
        "history": "time + left (Compass Past)",
        "after": "time + right (Compass Future)",
        "future": "time + right (Compass Future)"
    }

    # C. ANTONYM DEVIATIONS: Nouns represented purely as ANTI + Positive Base Noun
    antonym_derivations = {
        "death": "ANTI + life",
        "loss": "ANTI + product",
        "disease": "ANTI + health",
        "illness": "ANTI + health",
        "sickness": "ANTI + health",
        "cancer": "ANTI + health",
        "injury": "ANTI + health",
        "war": "ANTI + peace",
        "conflict": "ANTI + peace",
        "battle": "ANTI + peace",
        "fight": "ANTI + peace",
        "attack": "ANTI + protect",
        "argument": "ANTI + agreement",
        "disagreement": "ANTI + agreement",
        "dispute": "ANTI + agreement",
        "division": "ANTI + union",
        "separation": "ANTI + union",
        "chaos": "ANTI + order",
        "disorder": "ANTI + order",
        "confusion": "ANTI + order",
        "lie": "ANTI + truth",
        "falsehood": "ANTI + truth",
        "incorrect": "ANTI + truth",
        "danger": "ANTI + security",
        "risk": "ANTI + security",
        "threat": "ANTI + security",
        "failure": "ANTI + success",
        "defeat": "ANTI + success",
        "absence": "ANTI + presence",
        "lack": "ANTI + presence",
        "deficit": "ANTI + money",
        "debt": "ANTI + money",
        "bankruptcy": "ANTI + money",
        "waste": "ANTI + product",
        "scarcity": "ANTI + more",
        "unemployment": "ANTI + employment",
        "difficulty": "ANTI + ease",
        "weakness": "ANTI + strength",
        "hate": "ANTI + love",
        "dislike": "ANTI + love",
        "bad": "ANTI + good",
        "evil": "ANTI + good",
        "wrong": "ANTI + right",
        "decay": "ANTI + grow",
        "rot": "ANTI + grow",
        "destruction": "ANTI + build",
        "demolition": "ANTI + build",
        "silence": "ANTI + words",
        "darkness": "ANTI + light",
        "night": "ANTI + light",
        "winter": "ANTI + summer",
        "recession": "ANTI + production",
        "error": "ANTI + truth",
        "mistake": "ANTI + truth",
        "noise": "ANTI + music",
        "female": "ANTI + male"  # Formally added female as the exact opposite of male!
    }

    # Combine all derivations
    all_derivations = {}
    all_derivations.update(compass_derivations)
    all_derivations.update(time_derivations)
    all_derivations.update(antonym_derivations)

    # 3. Perform the Pruning
    pruned_nouns = []
    removed_nouns = []

    for noun in nouns_list:
        if noun in all_derivations:
            removed_nouns.append(noun)
        else:
            pruned_nouns.append(noun)

    # 4. Save the results
    # Save the pruned list (keeping numbering)
    with open('top_2000_nouns_pruned.txt', 'w') as f:
        for idx, word in enumerate(pruned_nouns, 1):
            f.write(f"{idx}. {word}\n")

    # Save the derivations mapping as JSON
    with open('noun_derivations.json', 'w') as f:
        json.dump(all_derivations, f, indent=2)

    print(f"Pruning complete!")
    print(f"Original unique nouns: {len(nouns_list)}")
    print(f"Nouns pruned via ANTI/Compass: {len(removed_nouns)}")
    print(f"Remaining core positive nouns: {len(pruned_nouns)}")
    print(f"Compression ratio: {len(removed_nouns) / len(nouns_list) * 100:.1f}%")

if __name__ == "__main__":
    print("Re-evaluating antonym engine on active branch...")
    prune_and_map_nouns()
