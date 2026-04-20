#schema for the reason tool
schema = {
    "type": "function",
    "function": {
        "name": "reason",
        "description": "Think through the current situation step by step before responding. Use this to plan your next narrative move, consider player actions, and decide on consequences.",
        "parameters": {
            "type": "object",
            "properties": {
                "situation": {"type": "string", "description": "What is currently happening in the campaign?"},
                "player_intent": {"type": "string", "description": "What is the player trying to do?"},
                "possible_outcomes": {"type": "string", "description": "What are the possible outcomes of the player's action?"},
                "chosen_outcome": {"type": "string", "description": "What outcome will you go with and why?"},
                "next_narrative": {"type": "string", "description": "How will you narrate this to the player?"}
            },
            "required": ["situation", "player_intent", "possible_outcomes", "chosen_outcome", "next_narrative"]
        }
    }
}

#run function for reasoning components
def run(situation: str, player_intent: str, possible_outcomes: str, chosen_outcome: str, next_narrative: str) -> str:
    #log the reasoning chain for inspection
    print(f"\n[REASONING]")
    print(f"Situation: {situation}")
    print(f"Player intent: {player_intent}")
    print(f"Possible outcomes: {possible_outcomes}")
    print(f"Chosen outcome: {chosen_outcome}")
    print(f"Next narrative: {next_narrative}\n")
    return f"Reasoning complete. Proceed with: {next_narrative}"