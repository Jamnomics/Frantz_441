#file path imports
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

#import necessary libraries
import random

#schema for rolling dice tool
schema = {
    "type": "function",
    "function": {
        "name": "roll_dice",
        "description": "Roll one or more dice of a given number of sides.",
        "parameters": {
            "type": "object",
            "properties": {
                "sides": {"type": "integer", "description": "Number of sides on the die (e.g. 6, 20)"},
                "count": {"type": "integer", "description": "Number of dice to roll", "default": 1}
            },
            "required": ["sides"]
        }
    }
}

#function for executing dice roll
def run(sides: int, count: int = 1) -> str:
    #notify agent of missing required fields
    if not sides:
        return "Missing required sides field: specify number of sides on the die"
    
    #check sides and count are positive integers
    if not isinstance(sides, int) or sides <= 0:
        return "Incorrect required sides field: number of sides must be a positive integer"
    if not isinstance(count, int) or count <= 0:
        return "Incorrect required count field: number of dice to roll must be a positive integer"

    #generate random rolls between 1 and sides repeated count times
    rolls = [random.randint(1, sides) for _ in range(count)]
    
    #return formatted result including individual rolls and total
    return f"Rolled {count}d{sides}: {rolls} (total: {sum(rolls)})"