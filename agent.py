#file path imports
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

#import necessary libraries
from util.llm_utils import run_console_chat
from tools.character_store import load_all_characters

#find existing player characters
characters = load_all_characters()
players = [c for c in characters if c.get("type") == "player"]

#set prompt variables based on existence of player characters
if players:
    player = players[0]
    existing_player = f"A player character already exists: {player}. Do NOT call create_player. Greet them by name and continue their adventure."
    first_message   = f"Continue {player['name']}'s adventure."
else:
    existing_player = "No player character exists yet. Ask the user for details and create one."
    first_message   = "Ask for details about my player character. After my response, create my player character. After creating my player character, start the campaign."

#run console chat with dungeon master agent
run_console_chat(template_file="util/templates/dm_chat.json", existing_player=existing_player, first_message=first_message)