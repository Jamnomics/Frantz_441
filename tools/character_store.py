#file path imports
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

#import necessary libraries
import json
from config import PLAYERS_JSON, PLAYERS_RAG, NPCS_JSON, NPCS_RAG

#save character function and RAG summary builder
def save_character(character: dict) -> str:
    char_type = character.get("type", "npc")
    json_dir = PLAYERS_JSON if char_type == "player" else NPCS_JSON
    rag_dir  = PLAYERS_RAG  if char_type == "player" else NPCS_RAG

    #save as JSON
    name_slug = character["name"].lower().replace(" ", "_")
    with open(json_dir / f"{name_slug}.json", "w") as f:
        json.dump(character, f, indent=2)

    #build text summary
    summary = build_rag_summary(character)
    with open(rag_dir / f"{name_slug}.txt", "w") as f:
        f.write(summary)
        
    #index in RAG store
    from rag.embedder import index_character
    index_character(character["name"], summary)

    print(f"Saved {name_slug} to {json_dir} and {rag_dir}")
    return summary

#helper function for building RAG summaries
def build_rag_summary(character: dict) -> str:
    #convert character dict to a natural language summary
    lines = [
        f"Name: {character['name']}",
        f"Type: {character['type'].upper()}",
        f"Race: {character['race']}",
        f"Class: {character['class']}",
        f"Level: {character['level']}",
        f"HP: {character['hp']}/{character['max_hp']}",
    ]
    if "backstory" in character:
        lines.append(f"Backstory: {character['backstory']}")
    if "role" in character:
        lines.append(f"Role: {character['role']}")
    if "disposition" in character:
        lines.append(f"Disposition: {character['disposition']}")
    if "gold" in character:
        lines.append(f"Gold: {character['gold']}")

    return "\n".join(lines)

#functions for loading characters
def load_all_characters() -> list[dict]:
    characters = []
    for path in list(PLAYERS_JSON.glob("*.json")) + list(NPCS_JSON.glob("*.json")):
        with open(path) as f:
            characters.append(json.load(f))
    return characters

#load character by name function
def load_character(name: str) -> dict | None:
    name_slug = name.lower().replace(" ", "_")
    for directory in [PLAYERS_JSON, NPCS_JSON]:
        path = directory / f"{name_slug}.json"
        if path.exists():
            with open(path) as f:
                return json.load(f)
    return None