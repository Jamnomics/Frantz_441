#import necessary libraries
from tools.game_store import save_encounter

#schema for encounter details
schema = {
    "type": "function",
    "function": {
        "name": "run_encounter",
        "description": "Set up and start an encounter with NPCs or enemies.",
        "parameters": {
            "type": "object",
            "properties": {
                "encounter_type": {"type": "string", "description": "Type of encounter e.g. combat, social, exploration"},
                "location": {"type": "string", "description": "Where the encounter takes place"},
                "participants": {"type": "string", "description": "Who is involved in the encounter"},
                "objective": {"type": "string", "description": "What needs to happen to resolve the encounter"}
            },
            "required": ["encounter_type", "location", "participants", "objective"]
        }
    }
}

#create details of encounter state
def run(encounter_type: str, location: str, participants: str, objective: str) -> str:
    #notify agent of missing required fields
    if not encounter_type:
        return "Missing required encounter_type field: describe the type of encounter"
    if not location:
        return "Missing required location field: describe where the encounter takes place"
    if not participants:
        return "Missing required participants field: specify who is involved in the encounter"
    if not objective:
        return "Missing required objective field: describe what needs to happen to resolve the encounter"
    
    #create encounter details
    encounter = {"type": encounter_type, "location": location, "participants": participants, "objective": objective, "status": "active"}
    save_encounter(encounter)
    return str(encounter)