#file path imports
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

#import necessary libraries
from tools.create_character import create_character
from tools.character_store import save_character

#schema for creating an npc character
schema = {
    "type": "function",
    "function": {
        "name": "create_npc",
        "description": "Create a non-player character (NPC) with a role and disposition.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "NPC's name"},
                "race": {"type": "string", "description": "NPC's race e.g. human, elf, orc"},
                "char_class": {"type": "string", "description": "NPC's class e.g. merchant, guard, wizard"},
                "level": {"type": "integer", "description": "NPC's level", "default": 1},
                "hp": {"type": "integer", "description": "NPC's hit points", "default": 10},
                "role": {"type": "string", "description": "NPC's role in the world e.g. shopkeeper, villain, quest giver"},
                "disposition": {"type": "string", "description": "NPC's attitude and personality e.g. friendly, hostile, neutral"}
            },
            "required": ["name", "race", "char_class", "role", "disposition"]
        }
    }
}

#function for creating an npc character
def run(name: str, race: str, char_class: str, role: str, disposition: str, level: int = 1, hp: int = 10) -> str:
    #notify agent of missing required fields
    if not name:
        return "Missing required name field: specify the NPC's name"
    if not race:
        return "Missing required race field: specify the NPC's race"
    if not char_class:
        return "Missing required char_class field: specify the NPC's class"
    if not role:
        return "Missing required role field: describe the NPC's role in the world"
    if not disposition:
        return "Missing required disposition field: describe the NPC's attitude and personality"
    
    #create the non-playable character
    character = create_character(name, race, char_class, level, hp)
    character["role"] = role
    character["disposition"] = disposition
    character["type"] = "npc"
    save_character(character)
    return str(character)