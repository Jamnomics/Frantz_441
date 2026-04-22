#import necessary libraries
from tools.interact_character import interact_character
from tools.character_store import load_character
from tools.game_store import save_talk

#schema for character interaction details
schema = {
    "type": "function",
    "function": {
        "name": "talk_to_character",
        "description": "Initiate a conversation with an NPC.",
        "parameters": {
            "type": "object",
            "properties": {
                "character_name": {"type": "string", "description": "Name of the NPC to talk to"},
                "topic": {"type": "string", "description": "What the player wants to talk about"},
                "context": {"type": "string", "description": "Current situation or relevant recent events"}
            },
            "required": ["character_name", "topic", "context"]
        }
    }
}

#run interaction with a character
def run(character_name: str, topic: str, context: str) -> str:
    #notify agent of missing required fields
    if not character_name:
        return "Missing required character_name field: specify the name of the NPC to talk to"
    if not topic:
        return "Missing required topic field: describe what the player wants to talk about"
    if not context:
        return "Missing required context field: describe the current situation or relevant recent events"
    
    #create character
    interaction = interact_character(character_name, "dialogue", context)
    interaction["topic"] = topic

    #load character from RAG for context
    character = load_character(character_name)
    if character:
        interaction["disposition"] = character.get("disposition", "neutral")
        interaction["role"] = character.get("role", "unknown")

    print(f"\n[TALKING TO {character_name.upper()}]")
    print(f"Topic: {topic}")
    print(f"Context: {context}")
    
    #save interaction for context
    save_talk(interaction)
    return str(interaction)