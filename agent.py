#file path imports
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

#import necessary libraries
from util.llm_utils import run_console_chat

#run console chat with dungeon master agent
run_console_chat(template_file="util/templates/dm_chat.json")