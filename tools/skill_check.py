#import necessary libraries
from tools.roll_dice import run as roll_dice
from tools.game_store import save_skill_check

#schema for skill checks
schema = {
    "type": "function",
    "function": {
        "name": "skill_check",
        "description": "Perform a skill check by rolling dice against a difficulty class (DC).",
        "parameters": {
            "type": "object",
            "properties": {
                "skill": {"type": "string", "description": "Skill being checked e.g. stealth, persuasion, athletics"},
                "difficulty": {"type": "integer", "description": "Difficulty class (DC) to beat e.g. 10, 15, 20"},
                "modifier": {"type": "integer", "description": "Player's modifier for this skill", "default": 0}
            },
            "required": ["skill", "difficulty"]
        }
    }
}

#roll skill check and determine passing
def run(skill: str, difficulty: int, modifier: int = 0) -> str:
    #notify agent of missing required fields
    if not skill:
        return "Missing required skill field: specify the skill being checked"
    if not difficulty:
        return "Missing required difficulty field: determine the difficulty class to beat"
    
    #roll a d20 and apply modifier
    roll_result = roll_dice(sides=20, count=1)
    roll_value = int(roll_result.split("total: ")[1].rstrip(")"))
    total = roll_value + modifier
    success = total >= difficulty
    
    #save skill check for context
    check = {
        "skill":      skill,
        "roll":       roll_value,
        "modifier":   modifier,
        "total":      total,
        "difficulty": difficulty,
        "result":     "SUCCESS" if success else "FAILURE"
    }
    save_skill_check(check)
    return f"Skill check {skill}: rolled {roll_value} + {modifier} = {total} vs DC {difficulty}. {'SUCCESS' if success else 'FAILURE'}."