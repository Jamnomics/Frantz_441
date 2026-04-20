#base interaction logic shared by talk and action tools
def interact_character(character_name: str, interaction_type: str, context: str) -> dict:
    return {
        "character": character_name,
        "interaction_type": interaction_type,
        "context": context,
        "status": "in_progress"
    }