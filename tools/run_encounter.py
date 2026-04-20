#schema for running encounter
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

#create state of encounter
def run(encounter_type: str, location: str, participants: str, objective: str) -> str:
    encounter = {"type": encounter_type, "location": location, "participants": participants, "objective": objective, "status": "active"}
    print(f"\n[ENCOUNTER STARTED]")
    print(f"Type: {encounter_type}")
    print(f"Location: {location}")
    print(f"Participants: {participants}")
    print(f"Objective: {objective}")
    return str(encounter)