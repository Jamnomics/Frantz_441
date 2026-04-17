#file path imports
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

#import necessary libraries
from tools.create_character import create_character

#schema for creating a player character
schema = {
    "type": "function",
    "function": {
        "name": "create_player",
        "description": "Create the player character at the start of a campaign.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Player character's name"},
                "race": {"type": "string", "description": "Character's race e.g. human, elf, dwarf"},
                "char_class": {"type": "string", "description": "Character's class e.g. fighter, rogue, wizard"},
                "level": {"type": "integer", "description": "Starting level", "default": 1},
                "hp": {"type": "integer", "description": "Starting hit points", "default": 10},
                "backstory": {"type": "string", "description": "Brief backstory for the character"}
            },
            "required": ["name", "race", "char_class", "backstory"]
        }
    }
}

#function for creating a player character
def run(name: str, race: str, char_class: str, backstory: str, level: int = 1, hp: int = 10) -> str:
    character = create_character(name, race, char_class, level, hp)
    character["backstory"] = backstory
    character["type"] = "player"
    character["gold"] = 10
    return str(character)