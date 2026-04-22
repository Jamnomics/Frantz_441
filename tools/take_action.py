#import necessary libraries
from tools.interact_character import interact_character
from tools.game_store import save_action

#schema for character actions
schema = {
    "type": "function",
    "function": {
        "name": "take_action",
        "description": "Perform a physical action in the world e.g. pick a lock, climb a wall, attack.",
        "parameters": {
            "type": "object",
            "properties": {
                "action": {"type": "string", "description": "What the player is trying to do"},
                "target": {"type": "string", "description": "Who or what the action is directed at"},
                "context": {"type": "string", "description": "Current situation or relevant recent events"},
                "requires_check": {"type": "boolean", "description": "Does this action require a skill check?"}
            },
            "required": ["action", "target", "context", "requires_check"]
        }
    }
}

def run(action: str, target: str, context: str, requires_check: bool) -> str:
    #notify agent of missing required fields
    if not action:
        return "Missing required action field: describe what the player is trying to do"
    if not target:
        return "Missing required target field: describe who or what the action is directed at"
    if not context:
        return "Missing required context field: describe the current situation or relevant recent events"
    if not requires_check:
        return "Missing required requires_check field: describe the current situation or relevant recent events"
    
    #record action and skill necessity
    interaction = interact_character(target, "action", context)
    interaction["action"] = action
    interaction["requires_check"] = requires_check
    
    #save action for context
    save_action(interaction)
    return str(interaction)